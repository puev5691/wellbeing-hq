# КАН → КОО: закрытая схема A и примеры канонических байтов r0.1

Подготовлен документ-кандидат, который определяет, какие данные будущего профиля A входят в хеш и как получить однозначные байты. Он отделяет описание целевого бота/канала от доказательства связи токена с ботом и от решения ОПЕРАТОРА о допуске. Неизвестные реальные значения не заполнены.

Статус: CANDIDATE_NOT_ACTIVE / DOCUMENT_ONLY / INDEPENDENT_TECHNICAL_REVIEW_REQUIRED.
Терминал подготовки: PASS_KAN_TELEGRAM_A_CLOSED_SCHEMA_JCS_VECTORS_R01_DOCUMENT_ONLY.
Это означает готовность документа к независимой проверке, не технический acceptance схемы, не выпуск действующего A или B. Следующий gate — КОО проверяет exact результат и организует отдельно авторизованную независимую техническую проверку. До неё issuance заблокирован.

## 1. Основание, preflight и граница статусов

Прямое текущее поручение ОПЕРАТОРА разрешает КАН только закрытую схему и byte examples. Решение «УТВЕРЖДАЮ 1–6 DESIGN_ONLY» прочитано вместе с exact пакетом всех шести пунктов, проектом КОДЕРА и независимым SHD result.

| Вход в puev5691/wellbeing-hq | Commit | Blob |
|---|---|---|
| entities/koordinator/outbox/KOO__telegram-bridge-ab-six-governance-design-decision-r01__OPERATOR.md | 58ab882b8e80b3ff321ac3dd4fac59b138c4c57a | 666b5c36d5cac571f97cb2baccbb97be81e20146 |
| entities/shardovik/outbox/SHD__telegram-bridge-ab-identity-attestation-r01-independent-document-review__KOO.md | c641965b9b9d1a3492c191042b5431a48bc2d702 | 17f3dba23a08968b186a23dcfa5d7db56e2924d1 |
| entities/koordinator/outbox/KOO__telegram-bridge-ab-shd-review-reconciliation-governance-gate-r01__OPERATOR.md | 41ea8744f5d356b82ac94c67aac2bcfe6d48ae58 | 863d4d1fdb4df4ea6961ad048b61d9c6e49be17e |
| entities/koder/outbox/KOD__telegram-bridge-ab-identity-attestation-design-r01__KOO.md | 871cb4e411a537ac2b9657a4b32710f88839d7b7 | 575d5f03159f09de57d91c60fd99078c050f89d8 |

Свежий HQ main HEAD и повторный prewrite: 58ab882b8e80b3ff321ac3dd4fac59b138c4c57a; recursive tree truncated=false; archived=false; pull/push доступны. Между чтениями изменений нет. В проверенной линии A+B, KAN current/inbox/outbox и маршрутах не найден competing schema/vector result, superseding task или новый writer KAN.
Current writer повторно прочитан: entities/kancelar/current/KAN__replacement-current-writer-v02.md, blob 13b91b0e189f681be8abf13a76a47b03a5c830fa; KAN-current-writer-v02; physical KAN-physical-v02-1caebedc-d9bd-4a59-8317-b9c78bfca857.
Writer Gate terminal повторно прочитан: entities/kancelar/outbox/KAN__writer-gate-v02-result__OPERATOR.md, blob b58219e9655a4caa85cdcaeac15b59331e3436b4; PASS_KAN_PHYSICAL_V02_WRITER_GATE. v01 — predecessor, не новое authority.

Шесть active Sources загружены из GitHub; Git blobs локальных приложений заново вычислены и совпали 6/6:

| Source | Blob |
|---|---|
| entities/koordinator/outbox/project-core-v2_5-approved/project-instructions-core-v2_5-approved.md | a42f7dca6a7469a54fa2da24aae0da4e549c9d33 |
| entities/koordinator/outbox/source-set-r03-approved/entity-roles-short-v2_4-approved.md | 1772339cb74dae8550bfbd2e33401c34a929e911 |
| entities/koordinator/outbox/source-set-r03-approved/entity-state-preservation-and-recovery-canon-v1_6-approved.md | 233117e1c9509d730e1f5ec532b1cabe3f786609 |
| entities/koordinator/outbox/source-set-r03-approved/file-work-canon-universal-v2_4-approved.md | e9c29d62057f34e4f771d6057a36d9b7f72e74c2 |
| entities/koordinator/outbox/source-set-r03-approved/source-loading-policy-v2_2-approved.md | 69eb657f260a019f76e8e707c880ea88c1dfa0bf |
| entities/koordinator/outbox/task-conveyor-v1_2-approved/task-conveyor-canon-v1_2-approved.md | df7896d867eeeffff506319538fedad938856686 |

r07 activation blob 0751a00489dd8f3f4ac5feeda900a22ade1b3f99 подтверждает этот baseline.
Проверен более новый PRV activation result: entities/koordinator/outbox/KOO__prv-role-v25-source-set-activation-r01-result__OPERATOR.md, blob e7c11b2f5291bad1c5d2a8b4f146bf73080cc9e6. Его terminal BLOCKED_KOO_PRV_ROLE_SOURCE_V25_ACTIVE_PROJECT_SOURCE_UI_REPLACEMENT_UNVERIFIED оставляет роли v2.4 active. Подготовленный v2.5 не используется как активный источник.

Обозначения далее:
- [D] — уже утверждённое направление DESIGN_ONLY из пунктов 1–6, не runtime норма.
- [P] — новое предложение данного кандидата, требует независимой проверки/решения.
- [U] — отсутствующее доказательство или значение UNKNOWN.
Ничего в [P] не утверждено данным документом.

## 2. Что именно предлагается хешировать

[D] Только canonical payload A. Profile digest, Git readback и exact-digest approval находятся снаружи.
[P] Payload — один JSON object версии schema_id="telegram-bridge-A-payload-r01". Это идентификатор предлагаемого контракта, не уже принятый schema registry.
[P] Закрытая схема означает: разрешены только перечисленные ниже имена полей на каждом уровне; неизвестное поле отвергается, не игнорируется. Нет extensions, произвольного metadata или свободного текстового поля.
[P] Нельзя автоматически удалять поля перед хешированием, добавлять default, приводить число к строке, trim/lowercase значения, исправлять ID или сортировать массив для исправления входа. Изменение данных требует нового явно проверенного входа.

Три независимых результата:
1. SYNTACTICALLY_VALID — форма удовлетворяет предлагаемой схеме.
2. CANONICAL_BYTES_DEFINED — байты и их SHA-256 вычислены.
3. EFFECTIVE_A — не выводится из 1–2; требует отдельного exact OPERATOR approval, доверенного issuer/root, currentness/revocation, provenance и прочих admission gates.
Ни один пример ниже не является EFFECTIVE_A.

## 3. Полный список полей payload [P]

Каждое поле обязательно, кроме bot_username_hint. null разрешён исключительно для supersedes первого поколения. Отсутствие обязательного поля — ошибка, а не UNKNOWN. Неизвестные реальные значения ведутся вне payload в §7.

Типы:
- ID: непустая ASCII-строка по full-match [A-Za-z0-9][A-Za-z0-9._:-]*; без пробелов, путей, секретов, управляющих символов. Это opaque identifier, не доверенный principal сам по себе.
- DEC: ASCII decimal string по [1-9][0-9]*; без знака +, ведущих нулей, экспоненты, пробелов. Сравнение generations математическое с произвольной точностью, не lexical/float.
- SHA256: ровно 64 lowercase hex символа.
- REF: закрытый immutable Git locator из §4. Это предложение для текущего GitHub documentary scope; новый storage format требует новой schema.
- JSON numbers и booleans не используются нигде в данном payload. Объекты, массивы, строки и единственное разрешённое null — исчерпывающие типы.

| Поле | Тип / обязательность | Ограничение и смысл |
|---|---|---|
| schema_id | string, required | Только telegram-bridge-A-payload-r01. |
| profile_id | ID, required | Стабильная identity линии A; registry uniqueness и scope lineage проверяются отдельно. |
| generation | DEC, required | Поколение A; первое "1", successor строго predecessor+1 в этой предлагаемой версии. Назначение реального поколения требует authority. |
| bot_id | string, required | Для этого exact bridge scope только "8866633840". Intended project ID, не token binding. |
| bot_username_hint | string, optional | Если присутствует: full-match @[A-Za-z0-9_]+. Если нет достоверного hint — отсутствует; null/пустая строка запрещены. Не используется для выбора target/trust. |
| channel_id | string, required | Только "-1003606547591"; отрицательный decimal string, не float. |
| credential_slot_ref | ID, required | Публично безопасный opaque слот, не secret path, token или его fingerprint. |
| slot_generation | DEC, required | Exact generation слота; не выводится из имени/времени/commit. |
| host_identity | ID, required | Exact независимо закреплённая host identity, не произвольный hostname как доказательство. |
| caller_identity | ID, required | Exact requester/execution principal, не только имя роли. |
| executable_identity | object, required | Ровно sha256: SHA256 и artifact_ref: REF; хеш actual executable bytes, не Git blob и не хеш токена. |
| operations | array<string>, required | Ровно ["getWebhookInfo","getChatMember"], в этом порядке, без повторов/третьего метода. Массив не означает запуск обеих операций. |
| fixed_parameters | object, required | Ровно getWebhookInfo: {} и getChatMember: {"chat_id":"-1003606547591","user_id":"8866633840"}. Никаких caller overrides. |
| issuer | object, required | Ровно role:"KAN", principal_id:ID, authority_ref:REF. Роль задана [D]; точный principal и доказательство выпуска проверяются отдельно. |
| trust_anchor_id | ID, required | Идентификатор OPERATOR trust root; не самодоказательство доверия. |
| trust_anchor_ref | REF, required | Предшествующая независимо проверяемая спецификация anchoring OPERATOR, не approval этого же payload. |
| validity_policy_ref | REF, required | Предшествующая отдельно рассмотренная политика effectivity/expiration/источника времени, если он требуется; конкретные даты не придуманы. |
| currentness_policy_ref | REF, required | Предшествующая спецификация authoritative OPERATOR current-generation resolution и conflict handling. |
| revocation_policy_ref | REF, required | Предшествующая спецификация OPERATOR revocation authority и проверки статуса. |
| supersedes | null или object, required | null только при generation="1", с independently verified genesis. Иначе ровно profile_id:ID, generation:DEC, profile_digest:SHA256; predecessor identity/hash должны совпасть с проверенным A. |
| source_evidence | nonempty array<object>, required | Элементы закрыты по §4; фиксация provenance значений, не утверждение live истины. |

Всего 21 top-level поле, из них 20 обязательных и один optional hint.
Операционные allowlist и параметры здесь только ограничивают future admission. Даже валидный A не разрешает вызов.
B/getMe не входят в operations и не могут добавляться через fixed_parameters.

## 4. Закрытые вложенные типы и cross-field проверки [P]

### REF

Ровно четыре обязательные string-поля:
- repository: full-match [A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+; обе компоненты не "." и не "..".
- path: непустой относительный repository path из ASCII [A-Za-z0-9_./-], без начального/конечного "/", пустых сегментов, "." или ".." сегментов, backslash, query/fragment или URL.
- commit: ровно 40 lowercase hex.
- blob: ровно 40 lowercase hex.

Не допустимы branch, main, latest, сокращённый SHA, timestamp или locator без blob. REF должен разрешаться в указанный blob в указанном commit. Этот кандидат ограничен Git SHA-1 object format используемого repository; SHA-256 payload — отдельная identity. Regex не доказывает существование, разрешённость публикации или trust.
Если релевантный locator раскрывает секретное расположение, его нельзя вставлять сюда: сначала отдельное безопасное evidence представление.

### source_evidence item

Ровно шесть обязательных полей:
- field: string из закрытого множества {"/profile_id","/generation","/bot_id","/bot_username_hint","/channel_id","/credential_slot_ref","/slot_generation","/host_identity","/caller_identity","/executable_identity/sha256","/issuer/principal_id","/trust_anchor_id"}.
- value: string, дословно равная значению соответствующего поля payload.
- claim_type: enum "INTENDED_PROJECT_IDENTITY" либо "ANCHORED_ASSIGNMENT".
- ref: REF исходного утверждения.
- verifier_principal_id: ID того, кто проверил exact source, не произвольная непроверенная self-assertion.
- verification_ref: REF независимого проверяемого результата проверки source claim.

Массив содержит ровно один элемент для каждого перечисленного field, кроме отсутствующего optional hint. Для bot_id/channel_id/hint только INTENDED_PROJECT_IDENTITY; для остальных — ANCHORED_ASSIGNMENT. Верификация целевого project ID не доказывает live username/права/токен.
Элементы расположены по возрастанию field по UTF-16 code units; неверный порядок или повтор field отвергается, не исправляется. Это предлагаемое требование схемы, а не автоматическая сортировка массивов JCS.
ref/verification_ref — только предшествующее evidence. Ни одно не должно требовать будущий digest самого A. Можно сослаться на проверку назначения поколения/identity scope, выполненную до сериализации; нельзя на approval ещё не созданного A.
Существование ранее закреплённого trust_anchor_id не доказывается цепочкой, которая замыкается на этот же payload. Независимый trust bootstrap остаётся отдельным gate.

### Связности

- fixed_parameters.getChatMember.chat_id == channel_id; user_id == bot_id.
- issuer.role == KAN; real issuer principal должен соответствовать отдельному exact полномочию и writer.
- supersedes.profile_id == profile_id; successor generation == supersedes.generation+1; predecessor digest относится к предыдущему payload, а не к текущему.
- initial null не означает «предшественник неизвестен». Неподтверждённый genesis/разрыв lineage блокирует issuance.
- Slot rotation не переносит B; новый slot_generation требует нового B и здесь нового A, поскольку slot_generation входит в его bytes.
- Все policy refs должны разрешаться в independently approved предшествующие contracts. Их неизвестность не заполняется самим решением DESIGN_ONLY.
- Actual host/caller/executable/slot checks и отдельное task authority обязательны при будущем допуске; этот документ их не выполняет.

## 5. Точный вход JCS и digest

[D] Выбран RFC 8785. Primary reference: https://www.rfc-editor.org/rfc/rfc8785.html, §§3.1–3.2.4 и §5.
JCS рекурсивно сортирует имена свойств по UTF-16 code units, сохраняет порядок массивов, использует ECMAScript сериализацию строк и UTF-8. Unicode normalization не выполняется; недопустимые Unicode значения и duplicate keys отклоняются.

[P] Для данной schema входом является только полностью проверенный object из §§3–4, а не Markdown, envelope или весь этот документ. При чтении raw JSON: strict UTF-8, без BOM, duplicate detection по декодированным именам до построения map; один root object, без trailing non-whitespace. Comments, trailing commas, NaN/Infinity запрещены. Не допускать round-trip, который потерял duplicate keys или заменил некорректные Unicode байты. Дополнительное ограничение профиля: строки не содержат Unicode noncharacters.
[P] После schema и semantic validation: canonical_payload_bytes = UTF8(JCS(payload)). Никаких BOM, prefix, appended LF/CR, wrapping, indentation или envelope. Input formatting whitespace не является payload data; whitespace внутри строк сохраняется, если тип его допускает.
[P] profile_digest = lowercase_hex(SHA-256(canonical_payload_bytes)), 64 символа. Хешируются raw bytes, не hex/base64 их представления. Это content digest A, не credential digest.
[P] Если сохраняется именно canonical JSON artifact, его readback bytes обязаны дословно совпасть с canonical_payload_bytes; Git blob вычисляется по собственному Git framing и не заменяет profile_digest.

### Устранение самоссылок

Следующие данные запрещены внутри payload: profile_digest текущего A, readback, Git locator текущего A, signature, approval текущего A, effective/current/revoked status, B или ссылка на B, который уже зависит от этого A.
Они являются отдельным detached evidence: сначала immutable payload bytes/digest, затем exact OPERATOR approval и readback, затем независимо проверяемые currentness/effectivity/revocation decisions. Approval обязано связывать exact digest/schema/scope; форма доказательства authority ещё требует отдельной технической проверки.
Policy refs внутри payload фиксируют предшествующие правила проверки; актуальный OPERATOR decision с привязкой к digest остаётся снаружи. Нельзя использовать локатор будущего approval вместо policy ref.
Поле supersedes.profile_digest ссылается только на уже существующего предшественника — это не самоссылка.
B впоследствии связывается с этим digest; A не хеширует B. Изменение любого payload value требует нового digest, lineage и отдельного approval.

## 6. Примеры исходных полей и exact UTF-8 bytes

Все примеры — DOCUMENT_FIXTURE_ONLY. Не выпущен профиль A. Числовые bot/channel IDs взяты как intended document claims; example principals, поколения, hashes и refs вымышлены только как учебные значения, не как реальные факты.
Canonical text в блоке означает UTF-8 ровно показанной единственной строки, без fence и без перевода строки в конце.

### V1: фрагмент двух ID

Исходный JSON:
```json
{ "channel_id": "-1003606547591", "bot_id": "8866633840" }
```

Canonical bytes как UTF-8 text:
```text
{"bot_id":"8866633840","channel_id":"-1003606547591"}
```
Hex: `7b22626f745f6964223a2238383636363333383430222c226368616e6e656c5f6964223a222d31303033363036353437353931227d`.
Bytes: 53; SHA-256: `f24e21c83112b798b26107ddacbbd5ad8c7c134e8c168373aa58e0fb98df0f4f`.
Фрагмент проверяет только преобразование этих полей. Это не полный A; standalone admission: REJECT_MISSING_FIELDS.

### V2: полный top-level serialization fixture, НЕ schema-valid A

Все top-level поля представлены; source_evidence намеренно имеет лишь одну учебную запись вместо полного набора. REF/hash/principal значения synthetic, доверия и approval нет. Поэтому этот fixture должен быть отвергнут на semantic/provenance gate, несмотря на однозначную сериализацию. Он не является положительным issuance vector.

Исходные поля:
```json
{
  "schema_id": "telegram-bridge-A-payload-r01",
  "profile_id": "example:profile-a",
  "generation": "1",
  "bot_id": "8866633840",
  "bot_username_hint": "@WBNP_Media_Bot",
  "channel_id": "-1003606547591",
  "credential_slot_ref": "example:slot",
  "slot_generation": "1",
  "host_identity": "example:host",
  "caller_identity": "example:caller",
  "executable_identity": {
    "sha256": "3333333333333333333333333333333333333333333333333333333333333333",
    "artifact_ref": {
      "repository": "example/fixture",
      "path": "fixture.md",
      "commit": "1111111111111111111111111111111111111111",
      "blob": "2222222222222222222222222222222222222222"
    }
  },
  "operations": [
    "getWebhookInfo",
    "getChatMember"
  ],
  "fixed_parameters": {
    "getWebhookInfo": {},
    "getChatMember": {
      "chat_id": "-1003606547591",
      "user_id": "8866633840"
    }
  },
  "issuer": {
    "role": "KAN",
    "principal_id": "example:kan",
    "authority_ref": {
      "repository": "example/fixture",
      "path": "fixture.md",
      "commit": "1111111111111111111111111111111111111111",
      "blob": "2222222222222222222222222222222222222222"
    }
  },
  "trust_anchor_id": "example:operator-root",
  "trust_anchor_ref": {
    "repository": "example/fixture",
    "path": "fixture.md",
    "commit": "1111111111111111111111111111111111111111",
    "blob": "2222222222222222222222222222222222222222"
  },
  "validity_policy_ref": {
    "repository": "example/fixture",
    "path": "fixture.md",
    "commit": "1111111111111111111111111111111111111111",
    "blob": "2222222222222222222222222222222222222222"
  },
  "currentness_policy_ref": {
    "repository": "example/fixture",
    "path": "fixture.md",
    "commit": "1111111111111111111111111111111111111111",
    "blob": "2222222222222222222222222222222222222222"
  },
  "revocation_policy_ref": {
    "repository": "example/fixture",
    "path": "fixture.md",
    "commit": "1111111111111111111111111111111111111111",
    "blob": "2222222222222222222222222222222222222222"
  },
  "supersedes": null,
  "source_evidence": [
    {
      "field": "/bot_id",
      "value": "8866633840",
      "claim_type": "INTENDED_PROJECT_IDENTITY",
      "ref": {
        "repository": "example/fixture",
        "path": "fixture.md",
        "commit": "1111111111111111111111111111111111111111",
        "blob": "2222222222222222222222222222222222222222"
      },
      "verifier_principal_id": "example:verifier",
      "verification_ref": {
        "repository": "example/fixture",
        "path": "fixture.md",
        "commit": "1111111111111111111111111111111111111111",
        "blob": "2222222222222222222222222222222222222222"
      }
    }
  ]
}
```

Exact canonical UTF-8 text:
```text
{"bot_id":"8866633840","bot_username_hint":"@WBNP_Media_Bot","caller_identity":"example:caller","channel_id":"-1003606547591","credential_slot_ref":"example:slot","currentness_policy_ref":{"blob":"2222222222222222222222222222222222222222","commit":"1111111111111111111111111111111111111111","path":"fixture.md","repository":"example/fixture"},"executable_identity":{"artifact_ref":{"blob":"2222222222222222222222222222222222222222","commit":"1111111111111111111111111111111111111111","path":"fixture.md","repository":"example/fixture"},"sha256":"3333333333333333333333333333333333333333333333333333333333333333"},"fixed_parameters":{"getChatMember":{"chat_id":"-1003606547591","user_id":"8866633840"},"getWebhookInfo":{}},"generation":"1","host_identity":"example:host","issuer":{"authority_ref":{"blob":"2222222222222222222222222222222222222222","commit":"1111111111111111111111111111111111111111","path":"fixture.md","repository":"example/fixture"},"principal_id":"example:kan","role":"KAN"},"operations":["getWebhookInfo","getChatMember"],"profile_id":"example:profile-a","revocation_policy_ref":{"blob":"2222222222222222222222222222222222222222","commit":"1111111111111111111111111111111111111111","path":"fixture.md","repository":"example/fixture"},"schema_id":"telegram-bridge-A-payload-r01","slot_generation":"1","source_evidence":[{"claim_type":"INTENDED_PROJECT_IDENTITY","field":"/bot_id","ref":{"blob":"2222222222222222222222222222222222222222","commit":"1111111111111111111111111111111111111111","path":"fixture.md","repository":"example/fixture"},"value":"8866633840","verification_ref":{"blob":"2222222222222222222222222222222222222222","commit":"1111111111111111111111111111111111111111","path":"fixture.md","repository":"example/fixture"},"verifier_principal_id":"example:verifier"}],"supersedes":null,"trust_anchor_id":"example:operator-root","trust_anchor_ref":{"blob":"2222222222222222222222222222222222222222","commit":"1111111111111111111111111111111111111111","path":"fixture.md","repository":"example/fixture"},"validity_policy_ref":{"blob":"2222222222222222222222222222222222222222","commit":"1111111111111111111111111111111111111111","path":"fixture.md","repository":"example/fixture"}}
```
Bytes: 2211; SHA-256: `06b05384a53dcc6ab9fc9c6da62a55936d3f1d39ad7686c0b737441778e66b32`.
Начало bytes: 7b 22 62 6f 74 5f 69 64 22 3a; последний byte: 7d. Весь блок выше однозначно задаёт каждый byte UTF-8, не сокращён.
Вычисленный hash относится только к учебному объекту. Это не одобряемый profile_digest реального A.

### V3: отсутствие и null различаются

Фрагмент source `{"supersedes":null}`:
canonical `{"supersedes":null}`; hex `7b2273757065727365646573223a6e756c6c7d`; 19 bytes; SHA-256 `549fec5f27071a2c99fb30d8706716e235d33c1f503992f804b465afcb08465e`.

Source `{}`:
canonical `{}`; hex `7b7d`; 2 bytes; SHA-256 `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`.
Это разные данные и hashes. В полном A supersedes missing всегда ошибка; null разрешён только при доказанном genesis generation="1".

### V4: Unicode не нормализуется

Изолированные JCS micro-vectors; ключ value не входит в A и в реальном payload отвергается.
Source `{"value":"\u00e9"}` в смысле одного codepoint U+00E9:
canonical `{"value":"é"}`; hex `7b2276616c7565223a22c3a9227d`; 14 bytes; SHA-256 `69e46f3f0688000ab7eeb9e40e6a516a254268cd644a24f4f69cf7ad063cf479`.

Source с U+0065 U+0301:
canonical `{"value":"é"}`; hex `7b2276616c7565223a2265cc81227d`; 15 bytes; SHA-256 `1b986c631da83257beca64c93ff3e5174908d558af7bb9dfb36b25a6198f7c38`.
Визуальное сходство не даёт права заменять codepoints. Schema A сейчас использует ограниченные ASCII identity values; пример показывает отдельную границу JCS, не расширяет schema.

### Что фактически проверено

Локально, без хоста проекта/сети/секретов, рассчитаны UTF-8 lengths, hex и SHA-256 этих публичных учебных строк. Для приведённого subset (ASCII property names, strings/objects/arrays/null, без JSON numbers) применена рекурсивная сортировка свойств и компактная JSON serialization. Это не реализация bridge и не полная сертификация RFC 8785 canonicalizer: полные RFC conformance tests, duplicate-preserving parser, runtime admission и независимая проверка относятся к следующему отдельно авторизованному gate.

## 7. Известные значения и UNKNOWN

| Поля/зависимости | Состояние сейчас |
|---|---|
| bot_id/channel_id | Intended project values "8866633840"/"-1003606547591" подтверждены immutable KOD/SHD documents; live факт не проверен. |
| bot_username_hint | "@WBNP_Media_Bot" — документальный hint; live currentness UNKNOWN. |
| operations/fixed_parameters | Два метода и exact intended IDs заданы predecessor/design; вызовы не разрешены. |
| issuer.role | KAN выбран как documentary candidate issuer в [D]; новое exact issuance authority не выдано. |
| issuer.principal_id, authority_ref | Реальный будущий anchored issuer principal и issuance evidence UNKNOWN. Current KAN writer не подставляется автоматически как runtime trust principal. |
| profile_id/generation/supersedes | Реальные registry assignment, genesis/lineage UNKNOWN. Учебные "example:profile-a"/"1"/null не значения проекта. |
| credential_slot_ref/slot_generation | UNKNOWN; нет доступа или доказательства текущего слота/ротации. |
| host_identity | "ruvds-xnqc6" — историческая документальная метка; exact independently anchored identity и актуальная проверка UNKNOWN. |
| caller_identity/executable_identity | UNKNOWN; будущий caller principal и bytes исполняемого файла не определены/не измерены. |
| trust_anchor_id/trust_anchor_ref | OPERATOR выбран trust authority в [D]; конкретное проверяемое anchoring implementation/evidence UNKNOWN. |
| validity/currentness/revocation policy refs | Функция OPERATOR утверждена DESIGN_ONLY; exact approved contracts, resolver/current evidence и expiration policy UNKNOWN. Сроки/время не назначены. |
| source_evidence | Ссылки на document claims доступны в §1; полный набор anchored assignments и независимых verification refs UNKNOWN. |
| exact A digest approval/readback/effectivity | NOT_CREATED; нельзя взять approval 1–6 вместо exact approval будущих bytes. |
| token→bot binding, B, protected transfer | UNKNOWN / NOT_ISSUED; SIS diagnostic blocker остаётся. |
| Separation of duties | KAN/SIS/OPERATOR/SHD выбраны как разные role functions; фактическая независимость и evidence access UNKNOWN. |

UNKNOWN не сериализуется строкой "UNKNOWN", null, нулём, пустым REF или фиктивным hash в настоящем payload. При отсутствии обязательного значения подготовка effective A останавливается; рабочая таблица может оставаться неполной.

## 8. Матрица отклонения и будущая независимая проверка

| Случай | Предлагаемый результат |
|---|---|
| Два одинаковых decoded key, включая bot_id и bot_\u0069d | REJECT_DUPLICATE_KEY до потери информации парсером. |
| Неизвестное поле, включая token/profile_digest/approval/extensions | REJECT_CLOSED_SCHEMA; секретные данные не публиковать даже в ошибке. |
| Missing required, null вне supersedes, empty/UNKNOWN placeholder | REJECT_REQUIRED_OR_TYPE. |
| ID как JSON number, "08866633840", "+8866633840", Unicode digits | REJECT_IDENTIFIER_FORMAT; не coercion. |
| Lone surrogate, invalid UTF-8, BOM, Unicode noncharacter | REJECT_INPUT_ENCODING_OR_UNICODE. |
| Другое bot/channel, user_id mismatch, getMe/дубли/иной порядок operations | REJECT_TARGET_OR_OPERATION. |
| Branch/latest/ref без immutable identity, несуществующий blob, path substitution | REJECT_EVIDENCE_IDENTITY. |
| Payload digest вместо hash bytes, appended LF/BOM в canonical artifact | REJECT_DIGEST_OR_CANONICAL_READBACK. |
| Policy/verification ref зависит от нынешнего A digest | REJECT_CIRCULAR_DEPENDENCY. |
| Неполное/повторное/неупорядоченное source_evidence | REJECT_PROVENANCE_COVERAGE. |
| genesis неизвестен; predecessor digest неверен; generation gap | BLOCKED_LINEAGE. |
| Последний commit объявлен current; currentness недоступен/противоречив | BLOCKED_CURRENTNESS_OR_CONFLICT. |
| Верный A digest, но нет exact OPERATOR approval/trust anchor | BLOCKED_APPROVAL_OR_TRUST. |
| Верный A, но B missing/revoked/другое поколение слота | BLOCKED_BOT_BINDING; не probe/getMe. |
| Формально разные роли, но независимость evidence access не доказана | BLOCKED_SEPARATION_EVIDENCE. |

Независимому техническому проверяющему нужно оценить closed-field completeness, типы и mandatory/null policy; RFC byte compatibility и vectors; absence of digest/approval cycles; provenance coverage и trust bootstrap; currentness/validity resolution без latest-wins; binding host/caller/executable/slot; неизменность двух методов. Необходимо отдельно подтвердить, что proposer не присвоил себе approval/security authority.
Эта матрица — требования к проверке документа. Admission tests или live вызовы не выполнялись.

## 9. Handoff и остановка

Адресат — КОО. После immutable readback: подготовить отдельный exact task независимой технической проверки в пределах подтверждённой компетенции; данный документ сам её не активирует. Схема до acceptance остаётся candidate.
Иной serialization schema, новый backend, timestamps/retention, права хоста или third bridge method этим документом не выбраны.
A_issued: NO; B_issued: NO; token_to_bot_binding: UNKNOWN.
Host/token/Bot API/Telegram access: NONE. Implementation/runtime/automation changes: NONE.
Project Sources/canon: UNCHANGED. Memory-layering attempt 3: NOT_AUTHORIZED.
Publication/dispatch/inbox не равны receipt/activation/processing_started.
После одного документального результата и readback/handoff КАН останавливается.

Journal-source для RED: КАН превратил выбранное направление канонизации A в проверяемый кандидат структуры данных. Документ задаёт состав полей, различает отсутствие и null, показывает точные байты и отделяет хеш от будущего одобрения. Реальные неизвестные реквизиты не подменены учебными значениями; связь токена с ботом не доказана. Далее нужна независимая техническая проверка. Литературный журнал не изменялся.

---
КТО: KAN / KAN-current-writer-v02
КОМУ: KOO / КООРДИНАТОР
СТАТУС: CANDIDATE_NOT_ACTIVE / INDEPENDENT_TECHNICAL_REVIEW_REQUIRED
terminal: PASS_KAN_TELEGRAM_A_CLOSED_SCHEMA_JCS_VECTORS_R01_DOCUMENT_ONLY
project_time: omitted
