# whatsapp-cloud

Plugin do catálogo do Chimera para a **WhatsApp Cloud API oficial da Meta**. Só instruções: não
traz servidor MCP, hooks nem scripts, e não envia nada sozinho.

| Componente | O que ensina |
|---|---|
| skill `whatsapp-cloud-api` | envio (texto, mídia, botões, listas, templates), tokens, ids, erros, limites, a janela de 24 h |
| skill `whatsapp-webhooks` | verificação `hub.challenge`, assinatura `X-Hub-Signature-256`, payload, deduplicação, resposta rápida |
| skill `whatsapp-templates` | categorias, variáveis, aprovação, versionamento, o que leva a rejeição |
| skill `whatsapp-compliance-br` | opt-in, opt-out, registro de consentimento e LGPD na prática (não é parecer jurídico) |
| comando `/whatsapp-review` | revisa a integração do repositório contra os checklists, só leitura |

Por que não há servidor MCP: a Meta não publica um servidor MCP oficial para o WhatsApp. Quando o
catálogo de conectores do Chimera tiver a Cloud API como conector de API, ele entra lá, com o token
guardado pelo Chimera — não neste plugin.

Fora de escopo de propósito: whatsapp-web.js, Baileys e qualquer cliente que automatize o WhatsApp
Web — violam os termos do WhatsApp e derrubam o número.

---

## English

Chimera catalog plugin for Meta's **official WhatsApp Cloud API**. Instructions only: no MCP
server, no hooks, no scripts; it never sends anything by itself. Four skills (sending, webhooks,
templates, Brazil opt-in/LGPD) and a read-only `/whatsapp-review` command. Facts reflect Meta's
public developer documentation as of October 2026; prices, limits and error codes change, so the
skills tell the agent to confirm numbers on developers.facebook.com rather than quote them.

License: Apache-2.0 (this repository).
