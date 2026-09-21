# Происхождение редакции v1.7

Кандидат собран из exact v1.6 и одобренной для интеграции вставки KAN r01. Полные locator, blob и SHA-256 указаны в его новой служебной карточке. Содержательная часть исходного канона, кроме одной вставки, сохранена побайтно. Изменены только первая строка и служебная карточка, необходимые для честного статуса новой версии.

Исторические упоминания v1.6 candidate, predecessor gates и lineage внутри тела не правились: их массовая редактура не входит в поручение. Удалённая карточка v1.6 приведена ниже как provenance, не как метаданные нового кандидата. Отдельный KOO instance-admission guard не объединён с этим текстом.

## Карточка исходного v1.6, без изменений


Документ: канон сохранения состояния, инициации и восстановления Сущностей  
Версия: v1.6  
Статус: candidate_for_operator_approval  
Область: все Сущности проекта «БЛАГОПОЛУЧИЕ»  
Основа active: `entity-state-preservation-and-recovery-canon-v1_4-approved.md`  
Reviewed predecessor candidate: `entities/koordinator/outbox/entity-recovery-canon-v1_5-wake-initiation-resume-amendment-candidate-r04.md@aea341e30d5d5297a491e7320674f2587d66d1e5`  
Reviewed predecessor blob: `99b1ef3428330fa2e43d76a373b79cb8d3d663c5`  
Open OPERATOR gate for predecessor: `entities/koordinator/outbox/KOO__entity-recovery-canon-v1_5-operator-gate__OPERATOR.md@17190f729eef6537f0404af387253c9c11eb3a21`  
Predecessor gate status: resolved_by_operator_successor_selection  
Lineage resolution: OPERATOR selected v1.6 r0.3 as successor; predecessor v1.5 r0.4 gate resolved by d07a843f57f962a02c5ee34ba8713ad08e4ef416.  
Supersedes after activation barrier pass: active v1.4 and any predecessor candidate explicitly withdrawn/rejected by OPERATOR  
Изменены разделы: файл инициации; recovery-пакет; обязательная процедура инициации; integrated Wake/Writer layer; Recovery task conveyor; связь с политикой источников  
Основание изменения: preserve reviewed r0.4 authority/recovery work, add task-conveyor recovery state and prohibit historical PROMPT replay  
Current-writer / Writer Gate / exact task authority / immutable identity / verified initiation: preserved and not weakened  
Automation authority: capability does not create authority; `activation != processing_started`  
Approval status: requires_operator_review  
Effective: false  
Responsibility boundary: полный алгоритм task conveyor не дублируется; recovery canon owns continuity, initiation, writer and recoverability boundaries

Approval decision: entities/koordinator/current/KOO__source-rebuild-r03-operator-decision.md@c1e44243eb57ef0e667d0b9c4e93c1991cbf1899
