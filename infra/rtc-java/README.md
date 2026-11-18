# Motor Java da Receita Federal na Render

Implantação isolada do componente de código aberto:
https://github.com/ReceitaFederal/calculadora-rtc-regime-regular

- Commit oficial fixado: `150cccbe414d4a5edea703e4f7a424af5aa222c7` (v1.6.1).
- Java 21 / Maven / Flyway / SQLite read-only.
- Nginx recebe o tráfego na porta do Render e exige o cabeçalho `X-RTC-Engine-Key` para `/api/**`. O Java escuta somente no loopback 127.0.0.1:8080.
- A única rota pública sem autenticação é `/health` (status técnico).
- `RTC_ENGINE_SHARED_KEY` é um segredo de ambiente, **não** deve aparecer neste repositório.
- O proxy da Vercel deve enviar `X-RTC-Engine-Key`, com o mesmo segredo, para a API Render e exigir seu próprio `RTC_BRIDGE_TOKEN` dos clientes.
- Nenhuma operação é persistida pela interface web; a aplicação Java lê sua base de referência a partir do SQLite na imagem.
- O código-fonte da Receita é licenciado MIT; avisos de licença são preservados na imagem.

## Limites
O plano Free da Render possui recursos limitados e hiberna por inatividade. O motor oficial pode exceder os recursos do plano, caso em que a hospedagem deverá ser alterada para um tamanho adequado (sujeito a aprovação antes de qualquer custo). Sem homologação de segurança e fiscal, usar apenas com cenários de teste.
