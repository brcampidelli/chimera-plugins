# hostinger

Liga o **servidor MCP oficial da Hostinger**
([hostinger/api-mcp-server](https://github.com/hostinger/api-mcp-server), MIT; pacote npm
`hostinger-api-mcp`), fixado na versão `2.7.0` (publicada em 2026-10-01 — o pacote solta versões
quase todo dia; fixamos a mais nova com pelo menos duas semanas).

O pacote traz um binário por área. Este plugin usa **só dois**:

| Servidor | Binário | Cobre |
|---|---|---|
| `hostinger-vps` | `hostinger-vps-mcp` | VPS: estado, métricas, snapshots, firewall, reinício |
| `hostinger-dns` | `hostinger-dns-mcp` | zonas e registros DNS |

**Fora de propósito:** cobrança, compra de domínio, pedidos de hospedagem (`hostinger-billing-mcp`,
`hostinger-domains-mcp`, o `hostinger-api-mcp` completo). Mexer com dinheiro não entra por plugin.

Reiniciar ou restaurar snapshot de um VPS é ação com efeito real: o Chimera pede aprovação, e isto
não deve rodar em bot nem em cron.

**Autenticação:** a opção `hostinger_api_token` (token do hPanel › Conta › API) vira a variável
`HOSTINGER_API_TOKEN`. Vazia, o servidor faz login OAuth no navegador na primeira chamada.

O plugin `hostinger/claude-plugin` do marketplace oficial **não tem licença**; nada foi copiado dele.
Este é escrito do zero a partir do README público do servidor.

## English

Hostinger's official API MCP server, pinned to `hostinger-api-mcp@2.7.0`, narrowed to the VPS and DNS
binaries; billing, domain purchase and hosting orders are deliberately left out. Token via the
`hostinger_api_token` option (or OAuth in the browser when empty). Starts local processes through
`npx`. Written from scratch; nothing copied. License: Apache-2.0.
