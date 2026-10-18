# chimera-plugins

Marketplace de plugins curado para o [Chimera](https://github.com/brcampidelli/chimera-agent), no
formato do Claude Code (`.claude-plugin/marketplace.json`). Traz plugins escritos por nós e cópias,
com atribuição, de plugins de terceiros sob licença permissiva — cada um com a licença lida, a
fonte fixada num commit e uma revisão de segurança registrada.

## Como instalar no Chimera

Pelo terminal, fixando o commit do catálogo:

```bash
chimera plugin marketplace add github:brcampidelli/chimera-plugins@<sha-de-40-caracteres>
chimera plugin marketplace list
chimera plugin install whatsapp-cloud@chimera-plugins
chimera plugin enable whatsapp-cloud      # só depois de revisar
```

Pelo app: **Configurações › Plugins** (no grupo Personalização), *Descobrir*, adicionar este
marketplace e instalar.

O comando `chimera plugin` existe a partir do Chimera 0.69.0.

## Modelo de segurança

- **Instalar não liga.** Todo plugin entra **pendente**; nada chega ao agente até você ativar.
- **Hooks e `bin/` ficam inertes.** O Chimera nunca executa hooks de plugin. A revisão de cada item
  diz o que se perde com isso.
- **Servidores MCP entram só quando você pede**, e o cartão de cada plugin diz o que ele executa
  (instruções, rede, processo local, scripts).
- **Fonte sempre fixada:** pasta deste repositório, ou GitHub com o sha de 40 caracteres. Nada de
  branch, tag, `url` solta, npm sem versão, `@latest` ou `curl | sh` em servidor MCP.
- **Licença lida em cada item.** Só copiamos MIT, Apache-2.0, BSD, ISC, MPL-2.0 e CC0; o resto é
  reescrito do zero ou fica de fora.
- **Nenhum número inventado.** Não há "mais instalados" nem contagem de instalações (ninguém publica
  esse dado). A popularidade aparece só como estrelas do GitHub do repositório de origem, com a data
  da leitura — e, num monorepo, rotulada como estrelas do repositório inteiro.

## O que tem aqui

| Pasta | Conteúdo |
|---|---|
| `plugins/` | nossos plugins (Apache-2.0): `whatsapp-cloud`, `github`, `playwright`, `hostinger` |
| `vendor/` | cópias de plugins permissivos, com `LICENSE` e `UPSTREAM.json` (repo, caminho, commit, licença, data); `MODIFICATIONS.md` quando algo mudou |
| `ports/` | plugins de Codex e Cursor portados para o formato do Claude Code, com `PORT.md` dizendo o que mudou |
| `catalog/` | vitrine: categoria (as 26 de `categories.yaml`), até 3 secundárias, tags, destaque, o que executa, estrelas com data |
| `reviews/` | uma revisão por item: quem, qual commit, quando, e o checklist de segurança |
| `categories.yaml` | as 26 categorias canônicas, iguais nos catálogos de plugins, skills e conectores |
| `scripts/check.py` | a verificação que o CI roda (só biblioteca padrão; não executa nada dos plugins) |

Lista completa, com licença, origem e categoria: `.claude-plugin/marketplace.json` e `catalog/`.
Atribuições: [`NOTICE`](NOTICE).

## Contribuir

Veja [CONTRIBUTING.md](CONTRIBUTING.md).

---

## English

A curated plugin marketplace for the [Chimera](https://github.com/brcampidelli/chimera-agent) agent,
in Claude Code's format. It holds our own plugins (Apache-2.0) and attributed copies of permissively
licensed third-party plugins; every item has its license read, its source pinned to a commit and a
recorded security review.

**Install in Chimera (0.69.0+):** `chimera plugin marketplace add
github:brcampidelli/chimera-plugins@<40-hex sha>`, then `chimera plugin install
<name>@chimera-plugins` and `chimera plugin enable <name>` after reviewing it — or in the app under
Settings › Plugins.

**Safety model:** installs arrive disabled (pending) until you enable them; plugin hooks and `bin/`
are never run by Chimera; MCP servers are added only on request; every source is a folder in this
repository or a GitHub commit pinned by its full sha — no branches, no `@latest`, no unpinned npm, no
`curl | sh`; only MIT, Apache-2.0, BSD, ISC, MPL-2.0 and CC0 content is copied; popularity is shown
only as GitHub stars of the source repository with the date read, never as install counts.

Licensing: our content is Apache-2.0 ([LICENSE](LICENSE)); third-party copies keep their own
licenses ([NOTICE](NOTICE)).
