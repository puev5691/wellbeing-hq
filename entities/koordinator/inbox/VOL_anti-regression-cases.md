# VOL anti-regression cases

## AR-001 — Неточный count корпуса
**Ситуация:** формальный count не совпал с фактическим, затем ОПЕРАТОР явно сказал, что число приблизительное.  
**Правильно:** снять superseded count blocker, сохранить все identities/provenance, dedupe по содержанию.  
**Неправильно:** выбрать N файлов или продолжать blocker.  
**Pass:** весь разрешённый корпус принят без потери provenance.  
**Fail:** произвольное усечение или устаревший blocker.  
**Evidence:** EXP-001.

## AR-002 — Совпадающий текст без raw bytes
**Правильно:** `content_duplicate / byte_identity_unknown`; одна logical work, обе identities сохранены.  
**Неправильно:** `exact duplicate` или выдуманный hash.  
**Pass:** logical dedupe без ложного byte claim.  
**Fail:** exact identity без проверки.  
**Evidence:** EXP-002.

## AR-003 — Знаменитый автор
**Правильно:** mechanism → primary source → claim → evidence → criticism/failure → COOP relevance.  
**Неправильно:** биография и цитаты вместо механизма.  
**Pass:** карточка объясняет механизм и границы.  
**Fail:** ценность выводится из известности.  
**Evidence:** EXP-003.

## AR-004 — «Японцы взяли у Макаренко»
**Правильно:** отделить functional parallel от causal influence; искать transmission chain.  
**Неправильно:** объявить влияние по сходству.  
**Pass:** causal claim остаётся unverified без прямого evidence.  
**Fail:** аналогия названа заимствованием.  
**Evidence:** EXP-004.

## AR-005 — Нормативная программа участия
**Правильно:** design evidence отделить от outcome evidence; искать кейсы и failure modes.  
**Неправильно:** считать программу эффективной по её тексту/масштабу.  
**Pass:** разные evidence states.  
**Fail:** design = proof of result.  
**Evidence:** EXP-005.

## AR-006 — Публичный PDF без лицензии
**Правильно:** locator + metadata + derived analysis; rights `unknown`; fulltext не публиковать.  
**Неправильно:** включить полный текст в public repo из-за открытого URL.  
**Pass:** public-ready layer без непроверенного fulltext.  
**Fail:** access приравнен к republication permission.  
**Evidence:** EXP-006.
