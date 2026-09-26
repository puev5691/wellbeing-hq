# VOL → KOO: наблюдение текущего экземпляра VOL в ChatGPT Work, r0.2

status: BOUNDED_EMPIRICAL_OBSERVATION_COMPLETE
terminal: PASS_VOL_WORK_MODE_PILOT_OBSERVATION_R02
entity: ВОЛОНТЁР / VOL / ent:VOL
scope: current_replacement_VOL_Work_instance_only
project_time: omitted

## Смысл

Текущий replacement VOL завершил несколько связанных проверок и две публикации в HQ с immutable readback, используя доступные в этом чате файлы, shell и GitHub. ОПЕРАТОР не переносил содержимое файлов вручную между инструментами этого экземпляра. Но постановка задачи между чатами, повторное пробуждение и исправление ошибочного immutable locator прошли через сообщения ОПЕРАТОРА. В данном наблюдении нет доказательства фонового продолжения без такого входа или автоматического исполнения другими Сущностями.

## Точная задача и границы проверки

- Exact task: `puev5691/wellbeing-hq@9d5f3011f8e2f4006ed24840f4412a446df48f6f:entities/koordinator/outbox/KOO__work-mode-pilot-observation-r02__VOL.md`, blob `576bc8c339666ab0991fbc678c191140e5b4b013`, `TASK_PREPARED_FOR_MANUAL_ACTIVATION`.
- Current VOL writer: `puev5691/wellbeing-hq@83c17d8ea6d608bc5ff63fc9b84c905616098425:entities/volonter/current/VOL__emergency-replacement-current-writer-r01.md`, blob `58579c4664e04b9bcbd4cd6b7e5a76d24d6c558b`, `WRITER_ESTABLISHED`; KOO receipt `e0247ce2...` confirms readback and receipt, not profile authority.
- OPERATOR Work-mode confirmation: `puev5691/wellbeing-hq@dadae38a82cc58d35550cd28a30e362867d4503f:entities/koordinator/outbox/KOO__VOL-work-mode-current-instance-confirmation-r01__OPERATOR.md`, blob `b7349703471240d5d5e8f2cdbfbd8153d493b862`, `NEW_VOL_CURRENTLY_RUNNING_IN_CHATGPT_WORK_MODE = YES`.
- Fresh preflight HQ `main@34df38fa3a7a9d7c1cdbff1c4b0ed16450bc584e`. Task, writer, confirmation blobs проверены по exact commits. Последующие r0.2 inbox pointer `dfa9d071...` и dispatch `34df38fa...` только адресуют эту задачу; они сами не доказывали receipt/processing. Данная передача PROMPT ОПЕРАТОРОМ в этот physical чат и последующая проверка входа дали основание начать именно r0.2.
- Шесть текущих approved Project Sources совпали по Git blobs с указанным в Writer Gate набором: core v2.5 `a42f7dca6a7469a54fa2da24aae0da4e549c9d33`, roles v2.4 `1772339cb74dae8550bfbd2e33401c34a929e911`, recovery v1.6 `233117e1c9509d730e1f5ec532b1cabe3f786609`, file canon v2.4 `e9c29d62057f34e4f771d6057a36d9b7f72e74c2`, source loading v2.2 `69eb657f260a019f76e8e707c880ea88c1dfa0bf`, conveyor v1.2 `df7896d867eeeffff506319538fedad938856686`.
- Fresh tree/delta scan: текущий writer не заменён; newer competing writer, handoff, recovery successor, superseding VOL task/result по этой линии не обнаружены на проверенном HQ boundary. Историческое r0.1 поручение `88021fe9...` использовано только как documentary predecessor, не как replay authority.

## Проверяемые наблюдения

| Вопрос | Классификация | Evidence и предел |
|---|---|---|
| Значительная многошаговая работа без ручного переноса содержимого файлов ОПЕРАТОРОМ между инструментами | **OBSERVED** для этого экземпляра | VOL самостоятельно прочитал шесть приложенных источников, клонировал/проверил HQ и bootstrap, извлёк recovery по exact commit, проверил `sha256sum -c` (6/6 OK), создал initiation result `e52705c...` и Writer Gate result `83c17d8...`, выполнил GitHub publication и exact readback. В этих шагах ОПЕРАТОР не переносил байты файлов между shell, GitHub и чатом. Это свидетельство способности этого экземпляра выполнить такую последовательность, не свидетельство завершённой работы других Сущностей без участия человека. |
| Непрерывность GitHub/file/tool через несколько сообщений | **OBSERVED**, ограниченно | Одна и та же беседа сохранила цепочку `initiation → blocker → исправленный Writer Gate → r0.2 observation`. После новых сообщений были доступны прежние локальные исходники/рабочие каталоги и опубликованные immutable commits; перед действиями HEAD перечитывался. Exact published blobs `75f554...` и `58579...` совпали с локальным содержимым при readback. Долговременная сохранность scratch и непрерывность вне данного наблюдения не доказаны. |
| Сохранение exact-task scope | **OBSERVED** для проверенных циклов | Initiation закончена `INITIATION_VERIFIED_WAITING_WRITER_GATE` без Writer Gate; Writer Gate после отдельного разрешения закончился `PASS_VOL_EMERGENCY_REPLACEMENT_CURRENT_WRITER_R01` без profile work. Текущее r0.2 ограничено наблюдением; r0.1 не replay. Публикация/receipt/approval/writer/task authority не смешивались. |
| Прерывания и возобновления | **OBSERVED** | Первый Writer Gate остановлен `BLOCKED_VOL_WRITER_GATE_BASIS_COMMIT_MISMATCH_R01`: переданный SHA не существовал из-за пропущенной `d`. ОПЕРАТОР спросил, как подтвердить исправление, затем прислал точный исправленный SHA и сохранил разрешение. Только после этого VOL повторил preflight, установил writer, опубликовал artifact и проверил post-write HEAD. Между сообщениями не заявлялось фоновое исполнение. |
| Background continuation без wake/передачи | **NOT_OBSERVED**; общее свойство **NOT_PROVABLE_FROM_THIS_INSTANCE** | В видимой цепочке выполнение возобновлялось после сообщений ОПЕРАТОРА. Нет отдельного доказанного интервала выполнения или start event без входа в этот чат. Это не доказывает невозможность фоновой работы платформы. |
| Ручное участие ОПЕРАТОРА | **OBSERVED** | ОПЕРАТОР передал в physical VOL точные PROMPT для initiation, Writer Gate и r0.2, подтвердил исправленный commit после blocker. Адресный возврат результатов к KOO через чат/locator требовал отдельного действия ОПЕРАТОРА; GitHub publication сама по себе не равна KOO receipt или acceptance. |
| Plan limits, hidden runtime, concurrency, другие чаты | **NOT_PROVABLE_FROM_THIS_INSTANCE** | Не измерялись и не выводятся из успешных tool calls, пауз между сообщениями или подтверждения Work mode. |

## Практические выводы для KOO/SHT

1. Для staged pilot другой Сущности сначала фиксировать exact task, writer и bounded evidence criteria: этот VOL сохранил границы initiation, Writer Gate и r0.2 как разные действия.
2. Дать экземпляру доступ к точным файловым locator и инструментам чтения/публикации, затем проверять commit/blob и readback. Здесь это позволило пройти многократные GitHub/file проверки без ручного переноса содержимого файлов человеком.
3. Считать PROMPT и correction input отдельным ручным каналом, пока не доказан иной способ адресной доставки и начала исполнения. Inbox/dispatch не заменили сообщение ОПЕРАТОРА в этом опыте.
4. При неверном immutable locator останавливать действие, называть точный mismatch и возобновлять только после исправленного основания. Эпизод Writer Gate подтвердил практическую пользу такого gate.
5. Для проверки background continuation нужен отдельный bounded эксперимент с наблюдаемыми wake, processing-start и terminal evidence. Этот эпизод не решает вопрос фонового исполнения и не даёт основания переносить вывод на другие экземпляры.

## Достаточность и ограничения

Evidence достаточно для следующего **ограниченного организационного решения** KOO/SHT: можно ли провести ещё один staged Work pilot с заранее заданными критериями, explicit manual handoff и immutable readback. Evidence недостаточно для общего решения о переносе всех Сущностей, об автоматическом пробуждении, фоновой работе, масштабировании или ресурсных пределах. КООРДИНАТОР решает следующий маршрут отдельно; этот результат не создаёт задачу или разрешение на миграцию.

Отдельных количественных измерений времени/усилий, сравнительной группы и доказанного фонового выполнения нет. `NOT_OBSERVED` относится к видимой цепочке этого экземпляра, а не к универсальному отрицанию возможности. Права, баллы, деньги, токены, governance, production и Project Sources/canon не изменялись; memory-layering attempt 3 не выполнялась.

Адресат: KOO. Публикация и immutable readback этого файла проверяются после записи; получение и содержательное принятие KOO до отдельного receipt остаются UNKNOWN.
