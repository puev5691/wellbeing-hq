# KOO → SIS: Telegram discussion probe r0.1

status: LIVE_BOUNDED_PROBE_AUTHORIZED
execution_mode: EXACT_ONE_DISCUSSION_SEND
priority: HIGH_EXPERIMENTAL

## Operator authority

OPERATOR explicitly requested the first Telegram probes and continuation of the pipeline.

This authorization covers exactly one synthetic non-personal message to the already verified linked discussion group and one readback. No second/retry send is authorized.

## Verified target basis

Telegram mapping PASS:
`977a482936a8c0b4ad809c1b718048b1903fec9e`

Channel:
- username `wbnp_pev5691_15042026`
- id `-1003606547591`

Linked discussion:
- id `-1002429106148`
- title `Чат Благополучие медиа контур`

Bot:
- `WBNP_Media_Bot`
- id `8866633840`

First channel one-send PASS:
`a8d46d205a3233b04aa9cf95cb4b349a166df119`

## Probe

Send exactly one synthetic non-personal message to discussion id `-1002429106148`:

`Техническая проверка обсуждения WBNP. Discussion probe: 1/1. Ответ или действие не требуется.`

Required:
1. automatic retries = 0;
2. send count = exactly 1;
3. retain returned message_id/chat_id and exact payload SHA-256;
4. perform authorized readback through Telegram API/getChat/getChatMember or message evidence available to SIS;
5. verify message belongs to exact discussion id;
6. do not persist raw Telegram update envelopes, audience identities or unrelated chat text;
7. no webhook change;
8. no moderation;
9. no channel-right changes;
10. do not create project task from this synthetic message.

Expected:
`PASS_SIS_TELEGRAM_DISCUSSION_PROBE_R01`
or exact blocker/fail.

This authority is consumed after one send attempt.
Return result to KOO + WEB and stop.
