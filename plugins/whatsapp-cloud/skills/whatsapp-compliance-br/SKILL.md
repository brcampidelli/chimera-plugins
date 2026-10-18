---
name: whatsapp-compliance-br
description: Use when designing opt-in, opt-out, consent records, data retention or marketing campaigns for WhatsApp in Brazil — WhatsApp Business Messaging Policy plus LGPD (Lei 13.709/2018) practicalities. Not legal advice.
---

# WhatsApp in Brazil: opt-in, opt-out and LGPD

This is engineering guidance, not legal advice. When the user is about to launch a campaign or
process sensitive data, recommend that their DPO (encarregado) or lawyer review the flow.

## What WhatsApp's policy requires

- **Opt-in before business-initiated messages.** The user must have agreed to receive WhatsApp
  messages from this business, and the opt-in must say it is WhatsApp and name the business. A
  phone number collected for something else (an invoice, a delivery) is not an opt-in for
  marketing.
- **Honour opt-out immediately**, through any reasonable wording ("parar", "sair", "não quero
  mais"), not only an exact keyword.
- **Do not send what the user did not ask for** — quality ratings and messaging limits fall when
  users block or report.
- Some content is prohibited outright by WhatsApp's commerce and business policies (check the
  current list before a campaign in a regulated sector).

## LGPD in practice

| Topic | What to build |
|---|---|
| Legal basis (art. 7) | Marketing on WhatsApp: rely on **consent**, captured in a specific, unticked checkbox or an explicit reply. Transactional messages about a contract the user signed can rest on contract performance — keep the two purposes separate |
| Proof | Store per `wa_id`: purpose, wording shown, channel, timestamp, source (form, chat, checkout), and the policy version. Without a record there is no consent |
| Revocation (art. 8 §5) | As easy as giving consent. One message opts the user out of marketing; record the timestamp; stop all scheduled marketing for that number |
| Data subject rights (art. 18) | A path to confirm, access, correct and delete what you hold about a number, including chat history |
| Minimisation | Keep only the messages you need for the purpose; define a retention period and delete or anonymise after it |
| Sensitive data (art. 11) | Health, religion, biometrics, etc. need a stronger basis. Do not ask for them over WhatsApp unless the flow was designed for it |
| Children | Messages to minors need care; marketing aimed at children is a red flag |
| Processors | Meta and any BSP or CRM you use are processors/operators: list them in the privacy notice and keep the contracts |
| International transfer | Messages pass through Meta's infrastructure outside Brazil; the privacy notice should say so |
| Security | Access tokens and app secrets in a secret store; chat logs access-controlled; incidents reported (ANPD) when they create relevant risk |

## Data model sketch

```sql
create table whatsapp_consents (
  id            uuid primary key default gen_random_uuid(),
  wa_id         text not null,
  purpose       text not null check (purpose in ('marketing', 'transactional', 'support')),
  granted_at    timestamptz not null,
  revoked_at    timestamptz,
  source        text not null,          -- 'checkout', 'form:landing-x', 'chat'
  wording       text not null,          -- exactly what the user saw
  policy_version text not null
);
create index on whatsapp_consents (wa_id, purpose) where revoked_at is null;
```

Check consent in the sending path (the code that picks the template), not only in the UI that
schedules a campaign. With Supabase or any multi-tenant database, enable row-level security on this
table and scope it to the tenant.

## Review questions to ask about a flow

1. Where exactly did each recipient opt in, and can we show the record?
2. Is the opt-in specific to WhatsApp and to this purpose?
3. What happens, end to end, when someone replies "sair"? How long until the last message stops?
4. How long are messages kept, and who can read them?
5. Does any message or prompt ask for sensitive data?
6. Is the sender an unattended job? Then who approved this campaign, and where is that recorded?
