# Политика загрузки источников — v2.2 candidate

Кратко: источник должен находиться в активном контексте только тогда, когда его статус и область действия оправдывают постоянную загрузку. Наличие файла в проекте не делает его автоматически действующим каноном.

## 1. Классы источников

### A. Базовые управляющие

Должны быть доступны каждой рабочей Сущности при инициации:

1. действующий универсальный файловый канон;
2. `project-instructions-core.md` или утверждённая замена;
3. `entity-roles-short.md` или утверждённая замена;
4. `source-loading-policy.md` или утверждённая замена;
5. действующий канон сохранения состояния, инициации и восстановления Сущностей.

`task-conveyor-canon` является базовым управляющим источником для KOO и для Entity instances/tasks, которые фактически используют inter-chat/PROMPT conveyor. Для recovery-managed non-chat instance он подключается только если exact initiation/recovery/task использует этот mechanism.

Эти документы задают не предмет задачи, а правила работы с задачами, файлами, ролями, восстановлением и, когда применимо, передачей управления между Entity-чатами.

### B. Текущие управляющие

Подключаются, если их содержимое действительно актуально:

- заполненная текущая доска приоритетов;
- краткая актуальная карта состояния проекта;
- иной короткий status-source, явно утверждённый для текущего цикла.

**Пустой шаблон доски не является текущей доской приоритетов.** Он может храниться как шаблон, но из него нельзя выводить, что у проекта сейчас нет задач или что перечисленные строки являются приоритетами.

### C. Профильные и тематические

Подключаются только по задаче или в чат соответствующей Сущности:

- понятийное ядро проекта;
- канон маршрутизации артефактов;
- инженерный фильтр постановки задач;
- технические регламенты;
- исследования, отчёты, handoff, evidence;
- профильные initiation/snapshot/recovery-manifest;
- файлы, которые требуется проверить, изменить или применить.

### D. Черновики и кандидаты

Файлы со статусами `draft`, `candidate`, `review_required`, `requires_operator_review` не должны использоваться как действующая норма без явного решения ОПЕРАТОРА.

Их можно держать рядом для ревизии, но новая Сущность обязана отличать их от approved-источников.

## 2. Что не держать постоянно

Без конкретной необходимости не загружать:

- старые route-note;
- manifest завершённых пакетов;
- длинные status-report и handoff;
- технические логи;
- acceptance notes;
- промежуточные request;
- большие исследования «для сведения»;
- runtime-файлы;
- secrets и приватные конфиги;
- поглощённые или superseded-черновики.

## 3. Специальные правила для текущего корпуса

`file-work-canon-v2_1-proposed-amendments.md` является черновым дополнением. После утверждения редакции файлового канона, которая поглощает его полезные положения, этот файл следует вывести из активных источников и сохранить только как provenance/evidence.

`artifact-routing-canon-v02.md` имеет статус `draft_for_adoption`; его обязательные формулировки не должны трактоваться как утверждённый канон до решения ОПЕРАТОРА.

`blagopoluchie-concept-core.md` имеет статус `working_for_project_source_review`; он может использоваться как рабочий понятийный материал, но не как утверждённая нормативная основа.

`triz_task_filter_canon.md` в текущей редакции не должен применяться ко всем задачам проекта; до исправления области действия его следует считать профильным черновиком инженерного метода.

## 4. Инициация

При запуске новой Сущности сначала загружаются базовые управляющие источники, затем профильный initiation/snapshot/recovery-manifest. `task-conveyor-canon` дополнительно загружается для KOO и для instances/tasks, использующих inter-chat/PROMPT conveyor. После этого выполняется процедура внешней проверки recovery-пакета, если внешний контур определён.

Профильные исследования не подтягиваются «для полноты картины». Они подключаются после получения конкретной задачи.

## 5. Разделение доставки артефактов и task conveyor

Маршрутизация результатов и других рабочих артефактов выполняется по действующему файловому канону и подключённым профильным правилам маршрутизации. Политика загрузки источников не дублирует этот алгоритм.

Передача управления между отдельными Entity-чатами выполняется по task-conveyor canon через адресный PROMPT. PROMPT может быть direct text либо file-form.

Referenced artifacts физически не переносятся ОПЕРАТОРОМ, если адресная Сущность имеет проверяемый доступ к их exact locator и immutable identity в информационном поле. Physical transfer остаётся fallback только для недоступного locator либо внешнего файла, отсутствующего в общем информационном поле.

Технически проверенный automatic chat-resume механизм может заменить ручной transfer только если для exact scope отдельно утверждено standing/explicit automation-authority; техническая проверка capability такого authority не создаёт. `activation != processing_started`. GitHub `inbox`, publication или dispatch не доказывают активацию чата.

Исторические PROMPT-файлы не являются постоянными управляющими источниками. Их загружают только когда нужно проверить конкретный шаг, provenance или recovery-состояние; старый PROMPT не воспроизводится автоматически.

## 6. Критерий качества контекста

    минимум действующих управляющих источников
    + точная задача
    + только нужные профильные материалы
    + явные статусы документов

Слишком много файлов обычно повышает вероятность конфликта старых и новых норм. Поэтому источник без ясного статуса хуже, чем источник, которого нет.

---

## Служебная карточка

document_type: source-loading-policy
version: v2.2
status: candidate_for_operator_approval
source: source-loading-policy-v2-approved.md
based_on_reviewed_candidate: entities/kancelar/outbox/source-loading-policy-v2_1-candidate.md@59ae5c036151460ca63a0e2ccd37d4aa53c88aaf
open_operator_gate_for_predecessor_candidate: entities/koordinator/outbox/KOO__source-loading-policy-v2_1-approval__OPERATOR.md@b15a9250e72e7bb5da4efabd027fa4e43386022e
predecessor_gate_status: unresolved_open_gate
candidate_lineage_rule: this v2.2 candidate does not silently supersede or approve v2.1 candidate; OPERATOR must explicitly resolve which lineage is approved before any source-set activation
supersedes_if_approved_and_lineage_gate_resolved: source-loading-policy-v2-approved.md plus any explicitly withdrawn/rejected predecessor candidate
change_basis: preserve reviewed v2.1 delivery harmonization by delegation to file-work canon, add task-conveyor source-loading split and automation-authority boundary
changed_sections: A. Базовые управляющие; Инициация; Разделение доставки артефактов и task conveyor; служебная карточка
approval_status: requires_operator_review
effective: false
responsibility_boundary: algorithms of file delivery and task conveyor belong to their own canons; this policy only defines loading/context rules
