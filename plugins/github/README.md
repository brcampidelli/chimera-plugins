# github

Liga o **servidor MCP remoto oficial do GitHub** (`api.githubcopilot.com`, mantido em
[github/github-mcp-server](https://github.com/github/github-mcp-server), MIT). Este plugin é só o
endereço e o cabeçalho de autenticação — escrito por nós; nenhum arquivo foi copiado.

| Servidor | Endereço | Para quê |
|---|---|---|
| `github-readonly` | `https://api.githubcopilot.com/mcp/readonly` | ler repositórios, issues, PRs, Actions — comece por este |
| `github` | `https://api.githubcopilot.com/mcp/` | também escreve (abrir issue, comentar, editar) — adicione só quando quiser |

No Chimera os servidores de um plugin entram só quando você pede; nada liga sozinho.

**Token:** crie um *fine-grained personal access token* em github.com › Settings › Developer settings,
limitado aos repositórios que o agente pode ver, com escopos de leitura (e de escrita só se for usar o
servidor `github`). O Chimera guarda o valor; ele vai só no cabeçalho `Authorization` para
`api.githubcopilot.com`.

## English

Points at GitHub's official remote MCP server. Two servers: read-only (start here) and read-write
(add it only when you want the agent to change things). Authenticates with a fine-grained PAT you
provide through the plugin's `github_token` option; the token is sent only in the `Authorization`
header to `api.githubcopilot.com`. Written by us; nothing copied. License: Apache-2.0.
