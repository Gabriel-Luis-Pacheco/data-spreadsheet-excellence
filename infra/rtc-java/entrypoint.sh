#!/bin/sh
set -eu

: "${RTC_ENGINE_SHARED_KEY:?RTC_ENGINE_SHARED_KEY deve ser configurada}"
PORT="${PORT:-10000}"
case "$PORT" in
  *[!0-9]*|"") echo "PORT invalida" >&2; exit 1 ;;
esac
# Nginx authentication secret is runtime-only and never part of the Docker image.
envsubst '${PORT} ${RTC_ENGINE_SHARED_KEY}' < /srv/rtc/nginx.conf.template > /etc/nginx/conf.d/rtc.conf
nginx -t
# The Spring server stays on loopback. Only nginx is reachable via the Render port.
java -Xms48m -Xmx260m -XX:MaxMetaspaceSize=130m -XX:+UseSerialGC \
  -Dspring.profiles.active=offline \
  -Dserver.address=127.0.0.1 -Dserver.port=8080 \
  -Dmanagement.server.address=127.0.0.1 \
  -Dmanagement.tracing.enabled=false \
  -jar /srv/rtc/app.jar &
java_pid=$!
trap 'kill "$java_pid" 2>/dev/null || true' EXIT INT TERM
nginx -g 'daemon off;'
