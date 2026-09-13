# KOO — operator-facing language rule v0.1

status: ACTIVE_WORKING_DIRECTIVE
canon: no
scope: KOO/Entity materials explicitly addressed for OPERATOR reading
project_time: omitted; trusted project-time source not used

## Rule

If a file is intended primarily for OPERATOR reading/decision:

1. Main prose is Russian.
2. Latin script is retained only where technically necessary:
   - variables and enums;
   - filenames and paths;
   - commands/code;
   - machine identifiers;
   - model/provider/product names;
   - commit/blob hashes;
   - exact API/URI/locator strings.
3. Necessary English technical terms are translated or explained in Russian at first meaningful use.
4. Human-facing summary comes before service metadata.
5. Exact underlying technical artifacts may remain in their native technical notation, but KOO must provide a Russian human-readable brief when OPERATOR is expected to read/decide.
6. A path alone is not sufficient human delivery; provide direct link and/or downloadable readable file where practical.
7. This working rule does not rewrite machine artifacts, code, protocol fields or approved canon.

Basis: explicit OPERATOR instruction in current work session.

---
КТО: KOO / КООРДИНАТОР
ДЛЯ ЧЕГО: устранить ненужный языковой барьер в операторской очереди чтения
СТАТУС: active_working_directive
