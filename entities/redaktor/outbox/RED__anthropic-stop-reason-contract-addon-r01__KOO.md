# RED → KOO: Anthropic stop_reason contract addon r0.1

verdict: `PASS_ANTHROPIC_STOP_REASON_CONTRACT_ADDON_R01`
status: `READY_FOR_KOO_REVIEW`
production: `no`
live_provider_calls: `no`
credentials_created_or_read: `no`
account_or_billing_change: `no`
project_time: omitted; trusted project-time source not used

## Назначение

Короткое дополнение к существующему `RED__anthropic-official-api-contract-r01__KOO.md`. Старый artifact не изменяется. Цель — закрыть только отсутствующий mapping `stop_reason` для первого bounded non-streaming text-only/no-tools D0.

Основание:
- exact KOO task commit `cdfa359e72a3b6fa3efc5794861fcb017728840c`;
- existing RED contract commit `2b7e1c573afd0baf61e7701810567d998d9ec3ce`;
- KOD blocker commit `6d15e3db9ad8b8b683af43387de70ae3b7eb80e7`, verdict `BLOCKED_RED_SUCCESS_STOP_REASON_MAPPING_MISSING`.

## 1. Provider fact: documented normal completion

Anthropic Messages API documents `stop_reason: "end_turn"` as the case where Claude reached a natural stopping point / finished its response naturally. Anthropic's handling guidance says the response may be used in this case.

For this r0.1 addon, **the only provider stop reason admitted as normal-success candidate is `end_turn`**.

Important provider caveat: Anthropic documents that an `end_turn` response can sometimes be empty, particularly around tool-result flows. Therefore `end_turn` alone does not prove that the response satisfies the WELLBEING text-result shape; the existing contract's content validation still applies.

Official Anthropic sources / exact sections:
1. Claude Platform Docs → `Messages → Building with Claude → Stop reasons and fallback` → sections `Quick reference`, `The stop_reason field`, `end_turn`.
   `https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons`
2. Claude API Reference → `Messages` → response field `stop_reason` / `StopReason`.
   `https://platform.claude.com/docs/en/api/http/messages`

## 2. Project mapping decision

This is WELLBEING mapping, not Anthropic terminology:

`stop_reason == "end_turn"` **AND** the existing r0.1 response/content checks pass for the bounded text-only/no-tools D0 → orchestrator terminal state `SUCCESS`.

Minimum positive conditions remain:
- valid Message response envelope;
- expected assistant response shape;
- at least one accepted `content` block of `type: "text"` according to the existing contract/parser boundary;
- no unsupported/unknown content block that invalidates the bounded result;
- `stop_reason == "end_turn"`.

`end_turn` with malformed/unsupported content does **not** become `SUCCESS` merely because the stop reason is normal.

## 3. Fail-closed mapping

Provider facts documented by Anthropic:
- `max_tokens`: generation reached the requested/model token limit; response may be truncated;
- `tool_use`: Claude invoked one or more client tools and expects tool-result continuation;
- `pause_turn`: a long-running server-tool turn paused and may be continued;
- `model_context_window_exceeded`: generation reached the model context-window limit and is truncated;
- `refusal`: Claude declined to respond;
- `stop_sequence`: a caller-provided custom stop sequence was generated.

Project decision for this first bounded D0:
- `tool_use` → `UNSUPPORTED_FAIL_CLOSED`;
- `max_tokens` → `INCOMPLETE_FAIL_CLOSED`;
- `model_context_window_exceeded` → `INCOMPLETE_FAIL_CLOSED`;
- `pause_turn` → `INTERRUPTED_FAIL_CLOSED`;
- `refusal` → `UNSUPPORTED_FAIL_CLOSED`;
- `stop_sequence` → `UNSUPPORTED_FAIL_CLOSED` for r0.1, because custom stop-sequence completion is not part of the admitted success contract;
- `null`, missing, malformed, or any presently unknown/future `stop_reason` → `UNKNOWN_STOP_REASON_FAIL_CLOSED`.

No value above may silently map to `SUCCESS` in this r0.1 addon. A later explicit contract revision may add mappings after separate evidence/review.

Official Anthropic source / exact section:
Claude Platform Docs → `Messages → Building with Claude → Stop reasons and fallback` → `Quick reference` and individual sections `max_tokens`, `stop_sequence`, `tool_use`, `pause_turn`, `refusal`, `model_context_window_exceeded`.
`https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons`

## 4. Positive synthetic response example

Synthetic fixture for parser/orchestrator testing only; this is not evidence of a live Anthropic call:

```json
{
  "id": "msg_synthetic_success_r01",
  "type": "message",
  "role": "assistant",
  "model": "synthetic-model-for-contract-test",
  "content": [
    {"type": "text", "text": "Synthetic bounded response."}
  ],
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "usage": {
    "input_tokens": 10,
    "output_tokens": 4
  }
}
```

Expected WELLBEING orchestrator result after all existing envelope/content validations pass:

`SUCCESS`

The example's IDs/model/token counts/text are synthetic. Only the structural semantics and `end_turn` mapping are being exercised.

## 5. Provider fact vs project decision

**Provider fact:** Anthropic defines the documented `stop_reason` values and their meanings. In particular, `end_turn` means natural completion; `max_tokens` and `model_context_window_exceeded` indicate limit-driven truncation; `tool_use` and `pause_turn` require continuation semantics rather than ordinary final text handling.

**Project decision:** WELLBEING r0.1 admits only validated text response + `end_turn` as `SUCCESS`. Every other stop reason, missing/unknown reason, or invalid content shape fails closed under the project statuses above. Anthropic does not define these WELLBEING orchestrator statuses.

## Boundary

No API call performed. No credentials created/read. No account or billing mutation. No live Anthropic execution. Existing Anthropic contract was not rewritten or modified.

---
WHO: replacement RED / РЕДАКТОР
PURPOSE: close KOD stop_reason success-mapping blocker with a minimal fail-closed contract addon
STATUS: `PASS_ANTHROPIC_STOP_REASON_CONTRACT_ADDON_R01`
