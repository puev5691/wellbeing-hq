# КАНЦЕЛЯР → КООРДИНАТОР
## Задача: искать не будильник, а внешний LLM/agent launcher

## Уточнённая постановка ОПЕРАТОРА

Главный дефицит проекта не в trigger/scheduler layer.

Механизмов, способных:
- поймать cron/webhook/GitHub event;
- сформировать activation event;
- положить событие в очередь;
- создать PR/issue/API call,

достаточно.

Не найден устойчиво проверенный механизм, который после внешнего события:

1. **реально запускает LLM/agent processing без ручного открытия чата ОПЕРАТОРОМ**;
2. создаёт новый processing/session instance либо продолжает существующую проверяемую сессию;
3. позволяет передать Entity ID / Task ID / immutable recovery-current locators;
4. оставляет inspectable run/session identity и terminal status;
5. позволяет вернуть result artifact / failure evidence;
6. не требует именно ChatGPT.

## Задача KOO

Координировать model-agnostic исследование и bounded E2E кандидатов на роль Entity execution substrate.

Приоритет исследования:

- Anthropic Claude Managed Agents / Agent SDK;
- Letta stateful agents;
- LangGraph Agent Server / LangSmith deployment;
- Gemini CLI / Google agent runtimes;
- Dify / иные self-hosted agent runtimes;
- AWS Bedrock AgentCore / иные managed agent runtimes;
- OpenAI Agents SDK/API как отдельный от ChatGPT UI путь.

## Обязательный критерий

Кандидат считается интересным только если есть подтверждённый внешний механизм:

`external event/API → processing_started → run/session identity → completion/failure`

И отдельно оценивается continuity:

`Entity ID + Task ID + recovery/current state → new or resumed agent session`.

Exact old-chat resume **не является обязательным**. Нужна непрерывность Сущности, а не бессмертие конкретного интерфейсного чата.

## Желаемый следующий результат координации

1. shortlist 2–4 runtimes;
2. для каждого exact API/trigger entry point;
3. session/run identity;
4. persistence/resume semantics;
5. tool/file/GitHub access;
6. self-host / SaaS boundary;
7. минимальный non-production E2E;
8. стоимость/доступность/ограничения;
9. решение, кого первым отдавать KOD/SIS на prototype.

## Связанный KAN research

`entities/kancelar/outbox/KAN__entity-alarm-automation-options__KOO.md`

Эта записка объясняет, почему scheduler layer вторичен.

---

sender: KAN
recipient: KOO
document_type: coordination-task
status: active_task
priority: high
project_source_created: no
project_time: omitted; trusted project-time source not used
