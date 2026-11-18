# Motor RTC (Receita Federal, MIT) - Java 21 + SQLite (read-only) + Nginx auth.
# Build pinned to an audited public commit rather than moving main.
FROM maven:3.9.11-eclipse-temurin-21 AS builder
RUN apt-get update && apt-get install -y --no-install-recommends git ca-certificates && rm -rf /var/lib/apt/lists/*
RUN git clone https://github.com/ReceitaFederal/calculadora-rtc-regime-regular.git /source
WORKDIR /source
ARG RTC_SOURCE_COMMIT=150cccbe414d4a5edea703e4f7a424af5aa222c7
RUN git checkout --detach "$RTC_SOURCE_COMMIT" && test "$(git rev-parse HEAD)" = "$RTC_SOURCE_COMMIT"
RUN mkdir -p ./calculadora/db
RUN mvn -B -ntp flyway:migrate -Dflyway.configFiles=./flyway/flyway-pro.conf
RUN test -s ./calculadora/db/calculadora-pro.db
RUN mvn -B -ntp -DskipTests clean package
RUN test -s target/api-regime-geral.jar

FROM eclipse-temurin:21-jre-jammy
RUN apt-get update && apt-get install -y --no-install-recommends nginx gettext-base ca-certificates && rm -rf /var/lib/apt/lists/* && rm -f /etc/nginx/sites-enabled/default
WORKDIR /srv/rtc
COPY --from=builder /source/target/api-regime-geral.jar /srv/rtc/app.jar
COPY --from=builder /source/calculadora/db/ /srv/rtc/calculadora/db/
COPY --from=builder /source/LICENSE /srv/rtc/LICENSE
COPY infra/rtc-java/entrypoint.sh /srv/rtc/entrypoint.sh
COPY infra/rtc-java/nginx.conf.template /srv/rtc/nginx.conf.template
RUN chmod 0555 /srv/rtc/entrypoint.sh && test -s /srv/rtc/calculadora/db/calculadora-pro.db
ENV PORT=10000 SPRING_PROFILES_ACTIVE=offline
EXPOSE 10000
CMD ["/srv/rtc/entrypoint.sh"]
