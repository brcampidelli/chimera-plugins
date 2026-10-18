---
name: whatsapp-templates
description: Use when drafting, submitting, versioning or debugging WhatsApp message templates for the Cloud API — categories (marketing, utility, authentication), variables, buttons, language codes, approval status, rejections and paused templates.
---

# WhatsApp message templates

A template is the only message a business may send to start a conversation or to write after the
24-hour customer service window has closed. Meta reviews each template before it can be used.

## Categories

| Category | For | Notes |
|---|---|---|
| `UTILITY` | A transaction or account event the user already triggered: order confirmed, shipped, payment due, appointment reminder | Must be specific to that user and that event. Promotional wording inside a utility template gets it recategorised as marketing |
| `MARKETING` | Promotions, offers, re-engagement, newsletters, anything not strictly transactional | Needs marketing opt-in; most exposed to blocks and quality drops |
| `AUTHENTICATION` | One-time passwords | Fixed format with a code and optional copy-code / one-tap button; no URLs, media or emojis in the body |

Pick the category honestly. Meta can change a template's category after review, and the price
follows the category.

## Anatomy

- `name`: lowercase letters, digits and underscores (`pedido_enviado_v2`). Version by name — an
  approved template cannot be freely edited in place, so plan `_v2`, `_v3`.
- `language`: one template per language code (`pt_BR`, `en_US`, `es`). Sending `pt` when only
  `pt_BR` exists fails with `132001`.
- Components: optional `HEADER` (text, image, video, document or location), required `BODY`,
  optional `FOOTER`, optional `BUTTONS` (quick reply, URL, phone number, copy code).
- Variables: positional `{{1}}`, `{{2}}`… in the body (named parameters are also supported in
  recent API versions — use one style per template). Submit **example values** for every variable;
  missing examples are a common rejection reason.
- Do not start or end the body with a variable, and do not place two variables side by side with
  nothing between them — both are rejection patterns.

## Creating one through the API

```http
POST https://graph.facebook.com/v{VERSION}/{WABA_ID}/message_templates
Authorization: Bearer {TOKEN with whatsapp_business_management}

{
  "name": "pedido_enviado",
  "language": "pt_BR",
  "category": "UTILITY",
  "components": [
    { "type": "BODY",
      "text": "Olá, {{1}}! Seu pedido {{2}} foi enviado e chega até {{3}}.",
      "example": { "body_text": [["Maria", "#1234", "sexta-feira"]] } },
    { "type": "FOOTER", "text": "Responda SAIR para não receber mais mensagens." }
  ]
}
```

Statuses: `PENDING` → `APPROVED` or `REJECTED`; an approved template can later be `PAUSED` or
`DISABLED` when users block or report it. Subscribe the webhook to `message_template_status_update`
to learn about changes instead of polling, and fall back gracefully when a template stops being
usable.

## Writing templates that get approved (and do not get blocked)

- Say who is writing and why the user is receiving it, in the first line.
- One purpose per template. A shipping notice with a coupon is marketing.
- No ALL CAPS, no misleading urgency, no requests for passwords, card numbers or full documents.
- URL buttons point to your own domain; avoid link shorteners.
- Give an easy way out in marketing templates (a "Parar promoções" quick reply or "Responda SAIR").
- Write in the user's language and register a template per language you actually serve.

## When drafting for the user

Produce, for each template: name, category with the reason, language, every component, the
variables with an example value each, and the trigger in their system that sends it (which event,
which opt-in it relies on). Mark anything that could be read as promotional inside a utility
template. Submitting the template is an action on the user's Meta account — prepare the request
and let the user (or an approved step) send it.
