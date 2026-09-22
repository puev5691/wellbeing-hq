# Checker/spec alignment r0.1 — bounded non-live

Exact task: 3e2a1e7145260e1255cacba6d1254373c3c9b3c5:entities/koordinator/outbox/KOO__booster-utility-r02-checker-spec-alignment-r01__KOD.md; blob 9b5d3719f90a44432be732cd6a1db046559bce1e.
Basis: 433c292daa10d15075431f2e7ce1d7c22cf7140e:entities/koder/outbox/KOD__booster-utility-pilot-r02-requester-decision__KOO-SIS.md.

Новый checker.py + source_policy.py. Frozen original checker и все входы находятся в frozen/ exact bytes. Task, expected outputs, 8 cases, rubric loop не менялись. diff-rationale.json содержит exact unified diff original→successor и machine-readable rationale; новый policy module входит в manifest.

len(str), range(int...), min(int...) — детерминированные операции без внешнего доступа, совместимые с опубликованной спецификацией. Разрешены именно эти builtins и append локального списка; это узкий протокол для данного bounded task. Неизвестные конструкции возвращают BLOCKED_UNREVIEWED_SYNTAX_OR_CAPABILITY либо другой конкретный blocker и требуют отдельного review. Это не объявление всех остальных pure Python конструкций нарушением публичной спецификации.

Перед исполнением статически просмотрены оба exact входа: только одна функция runs(s), локальные str/int/list/tuple операции, конечные обходы входной строки, отсутствие import/dynamic execution/external access. Candidate сканирует серии и делит каждую на группы <=3; baseline накапливает такие группы напрямую. Candidate bytes не изменялись. Это review этих двух файлов, не обещание безопасного запуска произвольного чужого Python.

Successor запрещает top-level effects/decorators/default expressions/nested functions, imports, private attributes/names, eval/exec/compile/import/open/process/network/env calls, input/global mutation и неизвестные методы. Исполнение статически проверенной функции происходит с restricted __builtins__={len,range,min}; двухсекундный локальный deadline ограничивает loops. Это не универсальный hostile-code sandbox и не ограничитель произвольного memory allocation: неизвестный candidate всё равно требует статического review. Compile/exec используется самим trusted checker для загрузки проверенного AST, но не доступен candidate.

Проверка: python3 -B run_tests.py. Guard запрещает external capabilities/processes/real environment/out-of-scope file access; forbidden attempts учитываются даже если тест поймал exception. Рабочие project/host/credentials не используются. Все negative fixtures проверяются статически без исполнения.

6 tests PASS, включая 20 negative fixture subcases. candidate-posthoc.json и baseline-posthoc.json содержат каждый из восьми случаев с полями exact, valid (тип/символ/счётчик1..3), roundtrip, greedy, input_unchanged. Все true, 8/8 для обоих. Source-policy admission не равен функциональному PASS: отдельный допустимый, но неверный вариант return[] не проходит rubric.

Candidate verdict: POST_HOC_RECHECK_PASS. Baseline: POST_HOC_BASELINE_RECHECK_PASS. Original pilot остаётся needs_rework / source-policy FAIL / cases NOT_REACHED; original checker reproduction PASS означает воспроизведённый отказ, не исправление исходного результата.

Elapsed baseline40.071600699 и assisted165.731668817 не пересчитывались/не заменялись. Проверка не является новым provider cycle, не исправляет candidate, не доказывает ускорение, не выдаёт project/production acceptance.

SHA256SUMS включает payload и MANIFEST, исключая сам checksum list. Manifest перечисляет payload кроме manifest/checksum; immutable Git identities находятся в итоговом result. Independent SIS non-live verify обязателен до дальнейшей интерпретации КОО.
