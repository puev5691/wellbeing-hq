# ARH → OPERATOR: подготовка emergency replacement KOO r1.0

exchange_gate: v1
sender: archivarius
recipient: operator
artifact: `entities/archivarius/outbox/ARH__KOO-emergency-replacement-r10-prep__OPERATOR.md`
version:
  commit: `15f411bbebe3f96c7ac9516b4aa7b6dc07f65815`
  blob: `10c0113519627c012999d73e69e5a1422b649989`
related_prompt: `entities/archivarius/outbox/PROMPT__KOO__emergency-replacement-r10-cold-start__OPERATOR.md`
related_prompt_version:
  commit: `2b4e8c4d439ac64fca9494ad694838a80b875967`
  blob: `682a9553214b83f452ea89742730978583d44f7a`
purpose: вернуть ОПЕРАТОРУ проверенную подготовку replacement KOO и один exact cold-start prompt
required_action: открыть новый чат KOO и передать exact prompt без изменений
expected_result: immutable KOO Initiation Gate result либо exact blocker
failure_mode: commit/blob mismatch, появление newer conflicting KOO writer/recovery/replacement evidence

status:
READY_FOR_KOO_REPLACEMENT_COLD_START

Этот dispatch не инициирует KOO и не выполняет Writer Gate.
