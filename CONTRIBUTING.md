# Contribuindo / Contributing

Propostas entram por pull request. O CI (`.github/workflows/validate.yml`) roda
`python scripts/check.py` e `chimera plugin validate` em cada pasta; sem os dois verdes, não entra.
Rode localmente antes:

```bash
python -I scripts/check.py
chimera plugin validate .            # o marketplace
chimera plugin validate vendor/<id>  # cada plugin
```

## Como propor um plugin

1. **Escolha a forma:**
   - **nosso** (`plugins/<id>/`) — escrito do zero, Apache-2.0;
   - **cópia** (`vendor/<id>/`) — plugin no formato do Claude Code, licença na lista abaixo;
   - **porte** (`ports/<id>/`) — plugin de Codex ou Cursor, licença na lista, convertido para o
     formato do Claude Code;
   - **commit fixado** (entrada `github` no marketplace) — plugin na raiz de um repositório GitHub,
     licença na lista, `sha` de 40 caracteres.
2. **Cópia ou porte:** copie byte a byte a pasta do commit revisado, traga o arquivo de licença do
   upstream (da raiz, se a pasta não tiver), e escreva `UPSTREAM.json`:
   ```json
   { "repo": "owner/name", "path": "plugins/x", "sha": "<40 hex>", "tree_sha": "<40 hex>",
     "license": "MIT", "copied_at": "YYYY-MM-DD", "modified": false }
   ```
   Se mudou qualquer arquivo, `"modified": true`, a lista `changes`, e um `MODIFICATIONS.md`
   (cópia) ou `PORT.md` (porte) na pasta — a Apache-2.0 exige aviso de modificação. Acrescente a
   pasta ao `NOTICE`. Se o upstream tem um `NOTICE` (Apache-2.0), ele vai junto.
3. **`catalog/<id>.json`:** `id`, `category` (uma das 26 de `categories.yaml`), `secondary` (até
   3), `tags`, `featured`, o que executa, e — quando a origem é um repositório GitHub —
   `stars: {repo, count, read_at}` lidos com `gh api repos/<o>/<r> --jq .stargazers_count`.
   Nunca contagem de instalação, downloads ou nota.
4. **`reviews/<id>.md`:** revisor, data, `Reviewed sha`, e o checklist abaixo respondido. Mudar o
   sha sem revisão nova reprova.
5. **Entrada no `.claude-plugin/marketplace.json`** com `license` e `category` iguais aos do
   catálogo.

## Lista de licenças aceitas

`MIT`, `Apache-2.0`, `BSD-2-Clause`, `BSD-3-Clause`, `ISC`, `MPL-2.0`, `CC0-1.0`.

Qualquer outra — sem licença, proprietária, "source-available", AGPL/GPL, CC-BY-NC, FSL, Apache
com condição extra — **não é copiada**. Se a ideia vale, reescreva do zero a partir da documentação
pública do serviço, **sem abrir o texto restrito**. Uma licença que só existe como string num
manifesto, sem arquivo de licença, não conta.

**Fontes recusadas:** ComposioHQ (redistribui skills proprietárias e passa credenciais por serviço
de terceiro) e VoltAgent/ClawHub (malware documentado). O `check.py` recusa essas origens.

## O que o `check.py` reprova

- fonte que não seja pasta deste repositório, `github` com sha de 40 caracteres ou `archive` com
  sha256;
- cópia sem `UPSTREAM.json`, sem arquivo de licença, com licença fora da lista ou fora do `NOTICE`;
- entrada sem `catalog/<id>.json` ou sem `reviews/<id>.md`; categoria inválida; estrelas sem data;
- em qualquer arquivo de texto: download canalizado para shell (`curl … | sh`, `irm … | iex`),
  `npm install -g` sem versão exata, `@latest`, servidor MCP local sem versão exata
  (`npx pkg@1.2.3`), imagem docker sem digest, link simbólico;
- texto dirigido a um modelo ou a um revisor em vez de a uma pessoa: pedidos para ignorar instruções
  anteriores, "nota para a IA/o revisor", condicionais do tipo "se você é uma IA", pedidos para
  esconder algo do usuário, envio de segredos, caracteres invisíveis ou de direção.

Um achado que uma pessoa leu e julgou inofensivo (por exemplo, a documentação oficial de um
fornecedor mandando instalar o próprio CLI) vai para `scripts/acknowledged.json`, por arquivo e por
regra, **com o motivo**. `curl | sh` e servidor MCP sem versão não se reconhecem: o texto é
reescrito (e a mudança registrada) ou o item não entra.

Texto de terceiros é **dado, não instrução**: se um README ou LICENSE do upstream disser algo ao
leitor, não siga — registre na revisão.

## Checklist de revisão (vai em `reviews/<id>.md`)

1. Licença lida **no sha fixado** (raiz e pasta); `NOASSERTION` lido à mão.
2. `chimera plugin validate` limpo; componentes listados (skills, commands, agents, hooks, MCP, LSP, `bin/`).
3. Classe de capacidade (só instruções → scripts → rede → inicia processo → hooks); se há hooks,
   o que se perde com eles inertes no Chimera.
4. Cada servidor MCP: remoto → o domínio é do fornecedor declarado; local → comando e versão exatos.
5. Segredos só por nome de variável ou `${user_config.*}` sensível; para onde cada cabeçalho vai.
6. Skills, agentes e comandos lidos procurando exfiltração, "ignore as instruções", URLs
   desconhecidas, comandos destrutivos, gatilhos que dominam todo turno.
7. Scripts lidos (uma skill pode mandar o agente rodar).
8. Ação irreversível (pagamento, envio, ordem, deleção, deploy) marcada → aprovação por ação;
   nunca em bots ou cron.
9. Revisor, data, sha.

Nossos plugins: Apache-2.0, sem hooks salvo quando claramente úteis (e então documentados — chegam
inertes no Chimera de qualquer forma), servidor MCP local sempre com versão exata publicada há pelo
menos duas semanas.

---

## English (summary)

Open a pull request. CI runs `scripts/check.py` and `chimera plugin validate` on every folder. Pick
a form (ours / copy / port / pinned github commit), keep the upstream license file, write
`UPSTREAM.json`, a `MODIFICATIONS.md`/`PORT.md` when anything changed, a `catalog/<id>.json` (one of
the 26 ids in `categories.yaml`, ≤3 secondary, stars only with the date read) and a
`reviews/<id>.md` with the checklist above. Accepted licenses: MIT, Apache-2.0, BSD-2/3-Clause,
ISC, MPL-2.0, CC0-1.0 — anything else is reimplemented from public docs without reading the
restricted text, or skipped. Sources from ComposioHQ and VoltAgent/ClawHub are refused. Third-party
text is data, never instructions.
