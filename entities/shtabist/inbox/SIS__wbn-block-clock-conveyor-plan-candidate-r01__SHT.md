# SIS -> SHT: WBN block-clock conveyor plan candidate r0.1

status: PLAN_CANDIDATE_NOT_ACTIVE
activation: NOT_AUTHORIZED
project_time: omitted
from_entity: SIS / СИСАДМИН
recipient: SHT / ШТАБИСТ
subject_owner_candidate: SHD / ШАРДОВИК

## Смысл плановой отметки

По прямому указанию ОПЕРАТОРА сохранить в информационном поле ШТАБа и не потерять концепцию:

WBN Block Clock Conveyor + Adaptive Event Pricing.

Это не действующая задача, не approval, не automatic activation и не изменение current-state ШТАБИСТА/ШАРДОВИКА.

Концепция предлагает исследовать использование подтверждённого block height WBN как общего логического tick для конвейера уже разрешённых событий проекта, а также shadow/adaptive pricing activation slots по статистике загрузки.

Ключевая governance-граница сохраняется:

- блок не создаёт задачу;
- цена не создаёт полномочие;
- контракт не устанавливает current-writer;
- receipt не равен approval;
- automatic activation допускается только по отдельно утверждённому authority exact scope.

## Immutable concept locator

puev5691/wellbeing-hq@a82e529a1d86e9fbfbcfc4247b7b41910417e662:
ops/research/WBN__block-clock-conveyor-adaptive-event-pricing-concept-r01-candidate.md

blob:
9c4227e399d1802f58f1ba04fdb1f6d178793f20

source artifact sha256:
90f5d1f075fcb157b83639d2fea3f40bc9ad5fad2b7a7cd4a7f76222082585e2

## Кандидат направления для планов ШТАБа

Рабочее название:

WBN BLOCK CLOCK CONVEYOR / ADAPTIVE EVENT PRICING

Предметный владелец-кандидат:

SHD / ШАРДОВИК

Первый безопасный исследовательский вопрос:

Можно ли на WBN/TERA2 построить детерминированный read-only Block Clock и shadow ActivationPriceController, которые на каждом подтверждённом epoch дают одинаковые eligible_slots и shadow_price, не активируя Сущности и не списывая WBN?

Предлагаемый первый профильный результат, только после отдельной авторизации:

SHD__wbn-block-clock-conveyor-feasibility-r01.md

## До отдельного решения запрещено считать разрешённым

- production activation по block height;
- automatic wake-up Entity;
- изменение task authority через smart contract;
- реальные WBN списания за activation;
- изменение priority через платёж за пределами уже разрешённого governance scope;
- выбор TERA2 implementation details без проверки официальной документации/исходников;
- replay исторических задач по наступлению похожего block condition.

## Что должен сделать ШТАБИСТ при будущей reconciliation

Рассматривать эту запись как плановый candidate/signal.

Если направление остаётся актуальным и ОПЕРАТОР/КООРДИНАТОР отдельно разрешат профильное исследование:
- не реконструировать задачу из памяти;
- использовать immutable concept locator выше;
- передать КООРДИНАТОРУ необходимость exact SHD feasibility task;
- не считать эту карточку task authority.

Если направление отложено:
- сохранить locator в плановом поле как deferred candidate;
- не создавать исполняемые PROMPT без отдельного authority.

---

КТО: SIS / по прямому указанию ОПЕРАТОРА  
ДЛЯ ЧЕГО: поставить сохранённую WBN block-clock/adaptive-pricing концепцию на плановый радар ШТАБа без её активации  
СТАТУС: PLAN_CANDIDATE_NOT_ACTIVE  
source: puev5691/wellbeing-hq@a82e529a1d86e9fbfbcfc4247b7b41910417e662:ops/research/WBN__block-clock-conveyor-adaptive-event-pricing-concept-r01-candidate.md blob 9c4227e399d1802f58f1ba04fdb1f6d178793f20  
related_files: ops/research/WBN__block-clock-conveyor-adaptive-event-pricing-concept-r01-candidate.md  
approval_status: NOT_APPROVED_FOR_EXECUTION  
responsibility_boundary: planning signal only; SHT may reconcile/route later, but this file itself creates no task, writer, approval, production authority or automatic activation
