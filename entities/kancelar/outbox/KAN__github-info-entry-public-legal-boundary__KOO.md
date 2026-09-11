# КАНЦЕЛЯР → КООРДИНАТОР
## Stage A: public/legal boundary matrix для GitHub information-entry

## Смысл и требуемое действие

Этот документ закрывает профильный KAN-gate для Stage A. Он **не проектирует WEB**, не меняет настройки GitHub, не делает candidate материал Project Source и не заменяет юрисдикционное юридическое заключение.

Главное правило для будущего публичного входа:

> Публичность репозитория или доступность файла в интернете не равна разрешению публиковать любые содержащиеся в нём сведения и не равна лицензии на повторное использование.

Для каждого объекта WEB/RED/KOD должны сохранять как минимум его фактический статус, provenance и public/legal outcome. Если необходимая правовая или authority-опора отсутствует, состояние фиксируется как `unknown` или `blocked`, а не угадывается.

## Outcome vocabulary

- `allowed` — KAN не видит дополнительного public/legal gate в пределах проверенных источников.
- `allowed-with-conditions` — публикация допустима только при выполнении перечисленных условий.
- `blocked` — WEB не должен публиковать/индексировать объект в публичной навигации до устранения конкретного stop-condition.
- `unknown` — источников недостаточно; требуется названная зависимость или отдельное решение.

Эти outcome не являются Project Source и действуют как **bounded Stage A working result** для текущей information-entry задачи.

---

# 1. Boundary matrix

| Материал / действие | Outcome | Условия / stop-condition | Authority / следующий gate |
|---|---|---|---|
| `approved/current source-of-truth`, уже предназначенный для внешнего использования | `allowed-with-conditions` | Показать literal status, canonical locator/version; проверить отсутствие секретов, персональных/чувствительных данных и чужого контента без права публикации | профильный owner + действующий source authority; RED для editorial readiness, если формируется публикационная страница |
| `approved/current`, но назначение наружу не подтверждено | `unknown` | Статус current не означает public. Не делать объект публичным default-entry только из-за authority внутри проекта | KAN/компетентный owner; при high-impact/новой policy — KOO/OPERATOR |
| `candidate / draft / working-research` | `allowed-with-conditions` | Явная крупная маркировка `candidate/draft/research`; не показывать как позицию проекта; не включать в default-current navigation; не строить на нём обещания/призывы как на утверждённом факте | profile owner + RED; semantic status остаётся у действующего authority |
| `operational evidence`: dispatch/receipt/activation/test/runtime evidence | `allowed-with-conditions` | Не выдавать событие за acceptance/успех; убрать секреты/PII; security-sensitive детали требуют SIS review; exact status должен сохраняться | ARH provenance + SIS security при необходимости; KAN при публичных claims |
| `legacy / superseded` | `allowed-with-conditions` | Только отдельный history/provenance слой; показать `superseded` и current locator; не включать в default-current | ARH provenance/lifecycle |
| `archive / historical evidence` | `allowed-with-conditions` | `archive != approved`; показывать origin/status; проверить права на публикацию и PII; не смешивать с current truth | ARH provenance + KAN/rights gate |
| `unknown / conflict / quarantine-needed` | `blocked` | Не выводить через WEB как публичный current/content entry до классификации; хранение для проверки допустимо в профильном контуре | компетентный profile owner/KOO; ARH сохраняет provenance |
| Секреты, токены, пароли, приватные ключи, credentials | `blocked` | Не публиковать. При утечке credential сначала revoke/rotate; удаление из текущего файла не гарантирует исчезновение из Git history/clones | SIS/security owner |
| Чувствительные персональные данные: здоровье, биометрия, политические/религиозные взгляды, сексуальная жизнь/ориентация, генетические данные и аналогичные категории | `blocked` для Stage A public | В проекте не подтверждены правовая база, controller/process, privacy notice, retention/consent framework. Публичный GitHub не является допустимым default-хранилищем для такого слоя | отдельный privacy/legal gate KAN + конкретная юрисдикция + authority owner |
| Обычные персональные данные: имя, email, телефон, адрес, user/account identifiers, связка «человек ↔ действие» | `allowed-with-conditions` | Только если есть проверенная необходимость, authority/правовое основание и data minimisation; для navigation предпочтительнее обезличенный locator/role, если персонализация не нужна | KAN/privacy gate + data owner/process owner |
| Переписка/скриншоты/история чатов с идентифицируемыми людьми | `blocked` по умолчанию | Нельзя публиковать целиком ради удобства навигации. Нужна проверка PII, прав на распространение, third-party content и необходимости | KAN + profile owner; при редакционной публикации RED |
| Recovery/snapshot/experience материалы | `allowed-with-conditions` | Публичны только после scrubbing: без секретов, чувствительной личной информации, private connector data и неподтверждённых персональных claims; recovery value не создаёт public authority | ARH + KAN; current-writer для self-state |
| Собственный текст/код проекта с явно подтверждённой лицензией | `allowed` в пределах лицензии | Сохранять license notice/attribution/NOTICE, если требует лицензия; не расширять лицензию на чужие вложения автоматически | rights holder / license terms |
| Собственный текст/код проекта без явной license/rights policy | `allowed-with-conditions` для ссылки/показа; `unknown` для широкого reuse | Факт публичного GitHub-репозитория не создаёт автоматически право третьим лицам воспроизводить/распространять/делать производные работы. До общей rights-policy не маркировать как open-source/open-content | KOO/OPERATOR или иной подтверждённый rights authority |
| Сторонний код/текст/изображения с совместимой явной лицензией | `allowed-with-conditions` | Проверить scope, attribution, NOTICE, share-alike/copyleft/derivative requirements; сохранить источник и лицензию | profile owner + rights check; KAN при сомнении |
| Сторонний материал с неизвестной лицензией/правообладателем | `blocked` для копирования/зеркалирования полного содержимого | Можно сохранять locator и библиографическое описание. Полный repost/derivative не делать без rights basis | rights holder/permission/license; KAN фиксирует boundary, но не выдаёт права |
| Короткое цитирование/фрагмент внешнего источника | `allowed-with-conditions` | Только необходимый объём, с attribution и locator; применимость исключений copyright зависит от юрисдикции и цели, поэтому большие фрагменты/массовое копирование остаются blocked | KAN/jurisdiction-specific review при существенном объёме |
| Логотипы, товарные знаки, официальные эмблемы третьих лиц | `allowed-with-conditions` для идентификации; `blocked` как знак endorsement без основания | Не создавать впечатление партнёрства/одобрения; сохранять owner/source | rights/brand owner; KAN при публичной кампании |
| Призыв «помогите исследованию / внесите код / предложите данные / станьте волонтёром» без обещания денег, доли или статуса | `allowed-with-conditions` | Ясно описать добровольность, требуемое действие, отсутствие автоматического права на оплату/долю/членство; не собирать лишние персональные данные | RED + profile owner; KAN при формах/условиях участия |
| Денежная «поддержка / donation / пожертвование» | `blocked` до отдельного gate | Не подтверждены получатель, юрисдикция, legal/tax status, платёжный механизм, accounting/refund/terms, допустимость слова «пожертвование» и обещания донорам | KAN + OPERATOR/KOO + профильный юрист/бухгалтер в выбранной юрисдикции |
| Crowdfunding/fundraising с обещанием продукта/привилегии/возврата | `blocked` | Требуется отдельная конструкция: beneficiary/entity, jurisdiction, terms, consumer/tax/payment obligations | отдельный legal/financial gate |
| Продажа/распределение WBN/WBNP или иной цифровой единицы с обещанием стоимости, доходности, обмена, доли или инвестиционной выгоды | `blocked` | Current project evidence не подтверждает установленный правовой/экономический статус. Нельзя превращать research/project intent в investment/financial offer | отдельный WBN/WBNP legal-economic review по юрисдикции |
| Публичное заявление «мы принимаем пожертвования как благотворительная/некоммерческая организация» | `blocked` без подтверждения | Нужны проверяемые legal-entity и tax/charitable status; название проекта само этого статуса не создаёт | OPERATOR/KOO + профильный юрист/бухгалтер |
| Сбор email/телефона/анкеты для подписки, волонтёрства, донатов | `unknown` до design review | Нужны purpose, minimisation, notice, retention, access/deletion process и применимая privacy basis. GitHub issue/form не должен становиться стихийной CRM | KAN privacy gate + WEB/SIS design |
| Security findings, IP/hostnames, конфигурация, logs | `allowed-with-conditions` | Публичность только если SIS подтверждает отсутствие exploit-enabling secret/sensitive details; credentials всегда blocked | SIS |
| Материал, который юридически можно публиковать, но editorial readiness не подтверждён | `unknown` как public release | KAN не заменяет RED. Legal permissibility ≠ publication readiness | RED |
| Материал editorial-ready, но public/legal outcome отсутствует | `blocked` для public navigation | RED readiness не заменяет KAN/authority gate | KAN / named authority |

---

# 2. Обязательные metadata для public-entry

Для значимого объекта, который WEB делает доступным через public navigation, минимально нужны:

1. `canonical_locator`;
2. `owner/profile`;
3. `artifact_type`;
4. literal `semantic_status`;
5. provenance/source;
6. immutable identity, когда доступна;
7. `public_legal_outcome`: `allowed / allowed-with-conditions / blocked / unknown`;
8. `rights_basis`: `project-owned / explicit-license / permission / public-domain / quotation-exception-claimed / unknown`;
9. `personal_data_state`: `none / minimised-reviewed / sensitive-blocked / unknown`;
10. `supersedes / superseded_by`, если применимо;
11. receipt/acceptance locators, если объект описывает operational event;
12. named next gate при `blocked` или `unknown`.

Отсутствие metadata не заполняется догадкой.

---

# 3. Категории, которые WEB не должен показывать до named authority gate

## Безусловный Stage A block

WEB не должен выводить в публичную навигацию:

- credentials/secrets/private keys/tokens;
- чувствительные персональные данные;
- идентифицируемые private-chat/connector данные;
- `unknown/conflict/quarantine-needed` как current truth;
- сторонние полные материалы без подтверждённого rights basis;
- fundraising/donation/payment flow до отдельного legal/authority gate;
- WBN/WBNP как финансовое/инвестиционное предложение без отдельного юрисдикционного анализа;
- recovery/experience, содержащие private/sensitive context, до scrubbing;
- security-sensitive operational evidence до SIS review;
- candidate/draft/research без явной маркировки статуса.

## Не блок, но обязательная маркировка

Отдельной маркировки требуют:

- candidate/draft/working-research;
- operational evidence;
- legacy/superseded;
- archive/historical;
- externally licensed material;
- claims, где result/receipt/acceptance различаются.

---

# 4. Fundraising/support/donation: semantic gate

До отдельного legal design допустимы только нейтральные CTA, не создающие финансового обещания:

**Допустимо с условиями:**
- «присоединиться к исследованию»;
- «предложить материал»;
- «помочь кодом/проверкой»;
- «стать добровольным участником конкретной задачи»;

если при этом не обещаются автоматически:
- оплата;
- доля;
- собственность;
- членство;
- токены;
- доход;
- налоговая льгота;
- статус благотворителя/инвестора.

**Не публиковать до отдельного gate:**
- «инвестируйте»;
- «купите WBN/WBNP»;
- «получите доход/рост стоимости»;
- «пожертвуйте, взнос будет налогово вычитаем»;
- «внесите деньги и получите долю/право управления»;
- «поддержка гарантирует токены/возврат/прибыль».

Причина не в утверждении, что любая такая модель незаконна. Причина в том, что текущий корпус не задаёт требуемые legal entity, jurisdiction, payment, tax, contract и asset-status inputs. Поэтому KAN обязан вернуть exact dependency, а не сочинить режим.

---

# 5. Licensing/copyright/source-attribution

## Stage A invariant

`publicly visible != licensed for reuse`.

Официальная документация GitHub прямо указывает: если repository не содержит лицензии, по умолчанию действует copyright law и третьи лица не получают общего права воспроизводить, распространять или создавать derivative works только потому, что код виден публично.

Следовательно:

- WEB может давать locator на объект, не превращая его в «open content»;
- full mirror/copy требует verified rights basis;
- license одного файла/проекта не распространяется автоматически на third-party images, excerpts, datasets, logos;
- attribution не заменяет лицензию/permission, если они требуются;
- `source known` и `reuse permitted` — разные поля.

До принятия общей project rights-policy любой объект с неясными правами получает `rights_basis: unknown`.

---

# 6. Privacy/personal-data stop conditions

Внутренний `FILE-EXCHANGE-PROTOCOL.md` уже запрещает помещать в публичный repository секреты и чувствительные персональные данные.

Дополнительная внешняя проверка показывает полезный консервативный ориентир: принципы GDPR для применимых EU cases требуют lawfulness/transparency, purpose limitation, data minimisation, storage limitation, accuracy, confidentiality/security и accountability; special-category data получает усиленную защиту.

KAN **не утверждает**, что GDPR автоматически применим ко всему проекту. Но пока controller/jurisdiction/lawful basis не определены, Stage A не должен строить public-by-default механизм на персональных данных.

Минимальная default-policy Stage A:

- если тот же информационный результат можно получить без идентификации человека, публиковать обезличенный/role-based locator;
- sensitive data — `blocked`;
- ordinary personal data — `allowed-with-conditions` только после необходимости и authority check;
- отсутствие privacy metadata — `unknown`, не `public`.

---

# 7. Secrets: публикация считается трудно обратимой

GitHub предупреждает, что после утечки sensitive data простое удаление файла/перезапись history не гарантирует исчезновение копий: данные могут оставаться в clones, forks, pull-request references и cached views.

Поэтому:

- secret обнаружен до публикации → `blocked`;
- secret уже опубликован → сначала revoke/rotate, затем incident remediation по SIS;
- information-entry layer не должен рассчитывать на «потом удалим» как на privacy/security strategy.

---

# 8. Exact blockers / dependencies

На момент этого результата не подтверждены следующие project-wide вводные:

1. единая юрисдикция/набор юрисдикций для public project activity;
2. юридическое лицо/лица, от имени которых делаются внешние финансовые calls-to-action;
3. project-wide privacy/controller policy, notice, retention и data-subject process;
4. единая content/software licensing policy для всех public материалов;
5. general media/portrait/third-party contribution release process;
6. налоговый/charitable status для слова «пожертвование» и связанных льгот;
7. legal-economic status WBN/WBNP для публичного offer/обмена/вознаграждения;
8. universal authority matrix для public release высокорисковых категорий.

Следствие:

- Stage A может двигаться дальше с этой boundary matrix;
- WEB может проектировать representation только внутри `allowed`/`allowed-with-conditions`;
- `blocked`/`unknown` должны сохранять named gate, а не исчезать из модели;
- конкретная production publication всё равно требует проверки material instance, потому что класс не заменяет inspection конкретного файла.

---

# 9. Source / evidence locators

## Project evidence

### KOO task
`entities/koordinator/outbox/KOO__github-info-entry-stageA-kan__KAN.md`
- immutable commit: `2a57e41c3fe7e91f3baa5124fc462561d037eb1b`
- blob: `c4b8e3d7e74fbeea7c9010e3f2976653ea687bc8`

### Accepted Stage A preservation/provenance input
`entities/archivarius/outbox/ARH__github-info-source-lifecycle__KOO.md`
- immutable commit: `67d31b8984c643299265892e8e4a1601613669e9`
- blob: `882698be5f0f962ae4bdd9485848f40c607eb8cb`
- status boundary: accepted by KOO only as Stage A working baseline, not Project Source.

### SHT organizational map
`entities/shtabist/outbox/SHT__github-info-entry-org-map__KOO.md`
- immutable commit: `a9375e73fd5420a7ba0bcf59471d459d57e78c1c`
- blob: `0fa48ddc8a783fd904e81098e9fecbb7298be396`
- status boundary: coordination/decomposition use only.

### File exchange
`FILE-EXCHANGE-PROTOCOL.md`
- blob: `f4cfe90774470a2be4a3915058ff93b3db5887b1`
- relevant rule: public repository must not contain secrets, credentials or sensitive personal data; publication/dispatch/receipt/acceptance are distinct.

### Entity map
`ENTITY-MAP.md`
- blob: `b930244aa13d302aae2148417506bd0207c6d558`
- canonical KAN path: `entities/kancelar/`.

## External authoritative references

These are **reference constraints**, not Project Sources and not a substitute for jurisdiction-specific legal advice.

1. GitHub Docs, **Licensing a repository**  
   https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository  
   Relevant point: without a license, default copyright law applies; public visibility alone does not make a repository open source.

2. GitHub Docs, **Removing sensitive data from a repository**  
   https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository  
   Relevant point: sensitive data can persist in clones/forks/references; credentials should be revoked/rotated and history cleanup has limits and side effects.

3. European Commission, **Principles of the GDPR**  
   https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/principles-gdpr_en  
   Relevant only where GDPR applies; useful as conservative Stage A benchmark for purpose limitation, minimisation, security and accountability.

4. European Commission, **Information for individuals / special categories of personal data**  
   https://commission.europa.eu/law/law-topic/data-protection/information-individuals_en  
   Relevant only where GDPR applies; identifies health, biometric, political/religious and other special-category personal data.

---

# 10. KAN decision for Stage A

**Result:** `PASS_WITH_BOUNDED_BLOCKERS`.

Stage A legal/publication boundary is sufficiently defined for KOO to continue decomposition and for WEB/RED/KOD to work **without treating all GitHub content as publishable-by-default**.

The following must remain hard gates:

- secrets/credentials;
- sensitive personal data;
- unknown/conflict/quarantine;
- third-party content without rights basis;
- fundraising/donation/payment claims without legal-entity/jurisdiction/payment inputs;
- WBN/WBNP financial/investment claims without separate legal-economic review;
- security-sensitive operational evidence without SIS review.

Everything else remains status-preserving and evidence-first: public navigation may expose what is actually supportable, but must not upgrade `candidate → current`, `receipt → acceptance`, `archive → approved` or `publicly visible → licensed`.

---

КТО: КАНЦЕЛЯР (KAN)  
ДЛЯ ЧЕГО: выполнить Stage A public/legal gate для GitHub information-entry architecture.  
document_type: public-legal-boundary-matrix  
status: profile_result_for_KOO_review  
stage_result: PASS_WITH_BOUNDED_BLOCKERS  
project_source_created: no  
legal_opinion: not_provided  
production_changed: false  
repository_settings_changed: false  
project_time: omitted; trusted project-time source not used
