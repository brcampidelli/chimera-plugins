---
name: whatsapp-cloud-api
description: Use when writing or debugging code that sends WhatsApp messages through Meta's official WhatsApp Cloud API (graph.facebook.com /{phone-number-id}/messages) — text, media, interactive buttons and lists, templates, read receipts, media upload and download, access tokens, error codes. Not for whatsapp-web.js, Baileys or other unofficial clients.
---

# WhatsApp Cloud API — sending and receiving

The Cloud API is Meta's hosted WhatsApp Business Platform API, called through the Graph API. It is
the only supported way to automate a WhatsApp Business number (the On-Premises API was retired).
Unofficial clients that drive WhatsApp Web (whatsapp-web.js, Baileys, venom) break the WhatsApp
terms and get numbers banned — if the code uses one, say so and propose the Cloud API instead.

Facts below come from Meta's public developer documentation as the author knows it. Meta changes
limits, prices and error codes; when a number matters (price, rate limit, tier), tell the user to
confirm it on developers.facebook.com and in WhatsApp Manager rather than trusting this file.

## The objects and ids

| Thing | What it is | Where it comes from |
|---|---|---|
| Meta app | Holds the WhatsApp product, the app secret and the webhook config | developers.facebook.com |
| WABA id | WhatsApp Business Account; owns templates and phone numbers | WhatsApp Manager / API |
| Phone number id | The sender. Every send is `POST /{phone-number-id}/messages` | WhatsApp Manager / `GET /{waba-id}/phone_numbers` |
| `wa_id` | The user's WhatsApp id, digits only | Webhook `contacts[].wa_id` |
| `wamid.…` | Message id | Send response and webhooks |

Graph API base: `https://graph.facebook.com/v{VERSION}/`. Pin the version in one config value and
upgrade on purpose — each Graph version has an end-of-life date, and behaviour can change between
versions. Never hard-code the version in several places.

## Authentication

- Production uses a **System User access token** created in Meta Business Settings, with the
  `whatsapp_business_messaging` permission (sending) and `whatsapp_business_management`
  (templates, phone numbers). The temporary token on the app dashboard expires in about a day and
  is for testing only.
- Send it as `Authorization: Bearer <token>`. Keep it in a server-side secret store or environment
  variable read at runtime; never in client code, never in the repository, never in logs.
- Token errors come back as Graph error code `190` — rotate the token, do not retry in a loop.

## Sending messages

Every send is the same endpoint with a different `type`:

```http
POST https://graph.facebook.com/v{VERSION}/{PHONE_NUMBER_ID}/messages
Authorization: Bearer {TOKEN}
Content-Type: application/json
```

Text (only inside an open customer service window — see below):

```json
{
  "messaging_product": "whatsapp",
  "recipient_type": "individual",
  "to": "5511987654321",
  "type": "text",
  "text": { "preview_url": false, "body": "Seu pedido foi enviado." }
}
```

Reply to a specific message: add `"context": { "message_id": "wamid.…" }`.

Template (the only way to start a conversation or write after the window closed):

```json
{
  "messaging_product": "whatsapp",
  "to": "5511987654321",
  "type": "template",
  "template": {
    "name": "pedido_enviado",
    "language": { "code": "pt_BR" },
    "components": [
      { "type": "body", "parameters": [ { "type": "text", "text": "Maria" }, { "type": "text", "text": "#1234" } ] }
    ]
  }
}
```

The number and order of `parameters` must match the approved template exactly; a mismatch is
error `132000`. See the `whatsapp-templates` skill for creating and versioning templates.

Interactive reply buttons (up to 3 buttons, short titles):

```json
{
  "messaging_product": "whatsapp",
  "to": "5511987654321",
  "type": "interactive",
  "interactive": {
    "type": "button",
    "body": { "text": "Confirma a entrega amanhã?" },
    "action": { "buttons": [
      { "type": "reply", "reply": { "id": "confirm_yes", "title": "Sim" } },
      { "type": "reply", "reply": { "id": "confirm_no", "title": "Não" } }
    ] }
  }
}
```

Interactive list: `"type": "list"` with `action.button` (the label that opens the list) and
`action.sections[].rows[]` (`id`, `title`, optional `description`). Lists hold at most 10 rows in
total. The button or row `id` comes back in the webhook as `interactive.button_reply.id` or
`interactive.list_reply.id` — route on the id, never on the visible title.

Media: either `{"type": "image", "image": {"link": "https://…"}}` with a public HTTPS URL, or upload
first and send the id:

```http
POST /{PHONE_NUMBER_ID}/media      (multipart/form-data: messaging_product=whatsapp, file=@…, type=image/jpeg)
→ { "id": "<MEDIA_ID>" }
```

Types: `image`, `video`, `audio`, `document` (add `filename`), `sticker`. Each type has size and
format limits; check them before uploading rather than after a failure.

Mark as read (shows the blue ticks): `{"messaging_product": "whatsapp", "status": "read",
"message_id": "wamid.…"}` on the same `/messages` endpoint.

The success response carries `messages[0].id` (the `wamid`). Store it: delivery and read statuses
arrive later by webhook with that id. A 200 means "accepted", not "delivered".

## Receiving media

Incoming media arrives in the webhook as an id. Downloading is two steps:
`GET /{MEDIA_ID}` returns a short-lived `url`, then `GET` that URL **with the same Bearer token**.
The URL expires within minutes — download right away, then store the file in your own storage.

## Phone numbers (Brazil)

- `to` is the number in international format, digits only: country code + area code + number
  (`55` + `11` + `987654321`).
- For replies, use the `wa_id` from the webhook rather than the number stored in your database.
  Some Brazilian mobile accounts registered before the ninth digit have a `wa_id` without the
  extra `9`; sending to the "corrected" number can fail or reach nobody.

## The 24-hour customer service window

- When a user messages the business, a 24-hour window opens (and restarts on every new user
  message). Inside it the business may send any message type, free-form.
- Outside it, only an approved **template** may be sent. A free-form send outside the window fails
  with error `131047` (re-engagement required).
- Track `last_inbound_at` per `wa_id` and choose template vs free-form in code, before calling the
  API — do not rely on the error.

## Errors worth handling explicitly

Read `error.code`, `error.error_subcode` and `error.error_data.details`. Common ones (confirm the
current list in Meta's error-code reference):

| Code | Meaning | What to do |
|---|---|---|
| `190` | Access token invalid or expired | Alert and rotate; do not retry |
| `100` | Invalid parameter | Fix the payload; do not retry |
| `131047` | Outside the 24-hour window | Send a template instead |
| `131026` | Message undeliverable (not a WhatsApp user, old app, or blocked) | Do not retry; mark the contact |
| `131051` | Unsupported message type | Fix the type |
| `132000` | Template parameter count mismatch | Fix the parameters |
| `132001` | Template does not exist in that language | Check name and `language.code` |
| `130429` | Throughput rate limit | Back off and retry with jitter |
| `131056` | Too many messages to the same user too fast | Slow down for that user |

Retry only rate-limit and 5xx errors, with exponential backoff and a cap. Everything else is a
bug or a policy outcome; log it with the `wamid` (or payload hash) and stop.

## Limits that shape the design

- **Messaging limits**: a new business portfolio can start conversations with a limited number of
  unique users per rolling 24 hours, raised in tiers as quality and volume grow. Check the current
  tier in WhatsApp Manager; plan campaigns around it.
- **Quality rating**: blocks and reports lower the number's rating and can pause templates or
  lower the tier. Sending only to opted-in users is the main defence.
- **Throughput**: each number has a messages-per-second cap. Queue sends and drain the queue at a
  controlled rate instead of firing a burst.
- **Pricing**: Meta charges per delivered template message by category and country, and changes
  the model from time to time (it moved from per-conversation to per-message pricing in 2025).
  Never state a price from memory — link the user to Meta's current pricing page.

## Checklist for code you write or review

- [ ] Uses the Cloud API endpoints, not an unofficial WhatsApp Web client.
- [ ] Graph version in one config value; token from a secret store; nothing secret logged.
- [ ] Template vs free-form decided from the stored 24-hour window, before sending.
- [ ] Every send stores the returned `wamid`; statuses reconciled from webhooks.
- [ ] Retries only on rate-limit/5xx, with backoff; idempotency key per logical message so a retry
      cannot send twice.
- [ ] Replies go to the webhook `wa_id`.
- [ ] Opt-in recorded before any business-initiated template (see `whatsapp-compliance-br`).
- [ ] Sending a message is an action with an effect on a real person: an agent asks before it
      sends, and never sends from an unattended job without an explicit, per-campaign approval.
