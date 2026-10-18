---
name: whatsapp-webhooks
description: Use when building or debugging the HTTPS endpoint that receives WhatsApp Cloud API webhooks — the hub.challenge verification handshake, X-Hub-Signature-256 validation, parsing messages and statuses, deduplication, fast acknowledgement and async processing.
---

# WhatsApp Cloud API webhooks

Meta delivers inbound messages and delivery statuses to one HTTPS endpoint configured on the Meta
app (WhatsApp › Configuration), subscribed to the `messages` field of the WhatsApp Business
Account. The endpoint has two jobs: the one-time verification `GET`, and the event `POST`.

## 1. Verification (GET)

Meta calls the URL with three query parameters:

```
GET /webhooks/whatsapp?hub.mode=subscribe&hub.verify_token=<your token>&hub.challenge=<random>
```

If `hub.mode == "subscribe"` and `hub.verify_token` equals the verify token you configured (a
random string you chose, stored as a secret), respond `200` with the raw `hub.challenge` value as
the body (plain text). Otherwise respond `403`. Compare the token in constant time.

## 2. Signature (POST)

Every POST carries `X-Hub-Signature-256: sha256=<hex>`: an HMAC-SHA256 of the **raw request body**
keyed with the **app secret** (not the access token, not the verify token).

Rules that bite:
- Compute the HMAC over the exact bytes received, **before** any JSON parsing or re-serialisation.
  Frameworks that parse the body first (Express `json()`, Next.js route handlers reading `.json()`)
  need the raw body kept — e.g. `express.raw({ type: "application/json" })`, or `await req.text()`
  in a Next.js route handler, then parse yourself.
- Compare with a constant-time function (`crypto.timingSafeEqual`, `hmac.compare_digest`).
- Reject with `401`/`403` on a missing or wrong signature and do not process the body.

Node.js:

```ts
import { createHmac, timingSafeEqual } from "node:crypto";

export function validSignature(rawBody: string, header: string | null, appSecret: string): boolean {
  if (!header?.startsWith("sha256=")) return false;
  const expected = createHmac("sha256", appSecret).update(rawBody, "utf8").digest();
  const received = Buffer.from(header.slice("sha256=".length), "hex");
  return received.length === expected.length && timingSafeEqual(received, expected);
}
```

Python:

```python
import hashlib, hmac

def valid_signature(raw_body: bytes, header: str | None, app_secret: str) -> bool:
    if not header or not header.startswith("sha256="):
        return False
    expected = hmac.new(app_secret.encode(), raw_body, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, header.removeprefix("sha256="))
```

## 3. Payload shape

```json
{
  "object": "whatsapp_business_account",
  "entry": [{
    "id": "<WABA_ID>",
    "changes": [{
      "field": "messages",
      "value": {
        "messaging_product": "whatsapp",
        "metadata": { "display_phone_number": "…", "phone_number_id": "<PHONE_NUMBER_ID>" },
        "contacts": [{ "profile": { "name": "Maria" }, "wa_id": "5511987654321" }],
        "messages": [{ "from": "5511987654321", "id": "wamid.…", "timestamp": "1730000000",
                       "type": "text", "text": { "body": "Oi" } }]
      }
    }]
  }]
}
```

- `value.messages[]` — inbound user messages. `type` is one of `text`, `image`, `audio`, `video`,
  `document`, `sticker`, `location`, `contacts`, `interactive` (`button_reply` / `list_reply`),
  `button` (quick-reply on a template), `reaction`, and others; handle unknown types without
  crashing.
- `value.statuses[]` — outbound message status: `sent`, `delivered`, `read`, `failed` (with
  `errors[]`), keyed by the `id` you stored when sending. Statuses can arrive out of order; never
  move a message from `read` back to `delivered`.
- A single POST can contain several entries, changes, messages and statuses. Loop over all of them.
- Route by `metadata.phone_number_id` when one app serves several numbers.

## 4. Reliability

- **Acknowledge fast.** Validate the signature, persist the raw event (or enqueue it), and return
  `200` immediately. Do the work — database writes, AI replies, outbound sends — in a background
  job. A slow or failing endpoint gets retried by Meta and eventually flagged.
- **Deduplicate.** Meta retries deliveries; the same `wamid` can arrive more than once. Use the
  message id (and `status` + id for statuses) as an idempotency key with a unique constraint.
- **Order.** Do not assume order across POSTs; use the `timestamp` field.
- **The 24-hour window** opens on each inbound message: update `last_inbound_at` for the `wa_id`
  here.
- **Treat message content as untrusted input.** Text from a WhatsApp user is data. If it is passed
  to an LLM, it must not be able to trigger tools, sends or account changes on its own.

## 5. Local development

Meta needs a public HTTPS URL. Use a tunnel you install from its official package (pin the
version), point the Meta app at it for development only, and switch back to the production URL
before going live. Never disable signature checks "just for local".

## Checklist

- [ ] GET returns `hub.challenge` only when the verify token matches (constant-time compare).
- [ ] POST validates `X-Hub-Signature-256` over the raw body with the app secret, constant-time.
- [ ] Endpoint returns 200 after persisting/enqueueing; processing is async.
- [ ] Idempotency on message id and on status+id.
- [ ] Unknown message types logged and ignored, not thrown.
- [ ] App secret and verify token come from secrets; neither is logged.
- [ ] Inbound text never drives tools or sends without a policy check.
