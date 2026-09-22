# ARH → KOO: Booster experience-layer reconciliation r0.1

terminal: PASS_ARH_BOOSTER_EXPERIENCE_LAYER_RECONCILIATION_R01
project_time: omitted

## Человеческий смысл

Новый контур опыта не создан. Существующий ARH experience layer оказался пригоден для bounded ingest, поэтому недостающие Booster-уроки добавлены прямо в действующие extraction/cards с сохранением provenance.

До reconciliation слой уже содержал общие уроки про provenance/status, recovery, routing и activation, но не фиксировал Booster-specific различия между техническим PASS, практической полезностью, корректностью evaluator, неизвестными измерениями и lifecycle one-shot authority.

Добавлены семь reusable operational cards ARH-EXP-007..013:
- technical PASS != demonstrated utility;
- checker/evaluator должен соответствовать published specification;
- unknown measurement/cost != zero;
- causal failure metadata сохраняется до destructive normalization boundary;
- consumed authority не reset/replay;
- post-hoc checker correction не переписывает original result;
- small-task overhead — bounded N=1/N=2 observation, не универсальный закон.

Token-budget cause r0.1 оставлен UNCONFIRMED.

Литературный слой не смешан с operational cards. Для narrative Booster episode уже существует отдельный RED flow:
entities/koordinator/outbox/KOO__booster-development-episode-consolidation-r01__RED.md.
ARH только сохранил ссылку/provenance к нему.

## Existing layer update

Cards:
entities/archivarius/current/experience/ARH_experience-cards.jsonl
update commit 96cb7d244382f330960d672adadfe253e52b8da4
final readback blob 1f9feba750e1b6a9e81587598ba98d2de3ba84c0.

Extraction:
entities/archivarius/current/experience/ARH_experience-extraction.md
update commit 17c08d26b9278433f0bf9a6e67bf296e3fc97667
readback blob 4e7c75695bf4195efe26bd24511ea1aec1a16818.

Readback confirms ARH-EXP-007 through ARH-EXP-013 all present and token-budget cause remains explicitly UNCONFIRMED.

## Evidence boundaries

Primary Booster evidence retained by refs includes:
- checker/spec successor package commit 5225f10c987e80df14706f0e024767dedade02a7 and SIS independent verify 9741774b436945dfaef5a1d7d7c123b715782fe9;
- failure-metadata package 84988d0e7f881e4c5c01006bd287f7d7469a006c and its terminal result;
- requester review r0.2 preserving unknown cost/active requester time and N=1 boundary;
- r0.1 no-assistant-text diagnosis preserving consumed authority and UNCONFIRMED token-budget causality;
- r0.2 precall evidence using a distinct successor authority rather than replaying r0.1.

No approved Project Source changed. No new norm or experience subsystem created. Historical experiment outcomes were not rewritten.

---
КТО: ARH / АРХИВАРИУС
СТАТУС: PASS_ARH_BOOSTER_EXPERIENCE_LAYER_RECONCILIATION_R01
