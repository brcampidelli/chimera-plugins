# playwright

Liga o **servidor MCP oficial do Playwright**, da Microsoft
([microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp), Apache-2.0), fixado na
versão exata `@playwright/mcp@0.0.83` (publicada em 2026-09-28) — o plugin equivalente do marketplace
oficial usa `@latest`, que muda por baixo de quem instalou.

O que faz: abre um navegador real, navega, clica, digita, lê o *snapshot* de acessibilidade e tira
capturas — para testar ponta a ponta o front-end. Roda `npx` na sua máquina (**inicia processo**) e
baixa o pacote do npm na primeira vez. `--isolated` mantém o perfil do navegador em memória, sem
gravar cookies em disco.

Atualizar a versão = novo PR com a versão nova, publicada há pelo menos duas semanas, e nova revisão.

## English

Microsoft's Playwright MCP server pinned to `@playwright/mcp@0.0.83`, run with `--isolated` so the
browser profile stays in memory. Starts a local process through `npx` and downloads the package from
npm on first use. Written by us (the `.mcp.json` is a fact about the package); nothing copied.
License: Apache-2.0.
