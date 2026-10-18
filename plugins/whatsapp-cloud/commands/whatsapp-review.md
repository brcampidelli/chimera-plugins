---
description: Review a WhatsApp Cloud API integration in this repository against the plugin's checklists (sending, webhooks, templates, opt-in/LGPD) and report findings with file references.
argument-hint: "[path or area to focus on]"
---

Review the WhatsApp integration in this repository. Focus: $ARGUMENTS

1. Find the code that talks to WhatsApp: search for `graph.facebook.com`, `/messages`,
   `messaging_product`, `hub.challenge`, `X-Hub-Signature-256`, `message_templates`, and for
   unofficial clients (`whatsapp-web.js`, `@whiskeysockets/baileys`, `venom-bot`). If an unofficial
   client is in use, report it first: it breaks WhatsApp's terms and risks the number being banned.
2. Read the sending path, the webhook handler and any template definitions in full.
3. Check them against the checklists in the `whatsapp-cloud-api`, `whatsapp-webhooks`,
   `whatsapp-templates` and `whatsapp-compliance-br` skills.
4. Report findings ordered by severity: security (signature, secrets), message loss or duplication,
   policy (24-hour window, opt-in, opt-out), then quality. For each: file and line, what is wrong,
   why it matters, and the smallest fix.

Read only. Do not send messages, call the Graph API, submit templates or change configuration
while reviewing; propose changes and let the user decide.
