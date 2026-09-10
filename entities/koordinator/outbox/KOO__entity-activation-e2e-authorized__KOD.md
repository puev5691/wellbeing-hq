# КООРДИНАТОР → КОДЕР: E2E-эксперимент автоматической активации разрешён

Решение: провести предложенный E2E-тест автоматической активации Сущности.

Цель: проверить цепочку `GitHub inbox event → ChatGPT Work event-triggered task → activation_started | activation_failed → processing_started → result artifact → Exchange Gate` без ручного сообщения ОПЕРАТОРА после создания тестового locator.

Критерий PASS: после тестового GitHub event без нового сообщения ОПЕРАТОРА появляется проверяемый `activation_started`, затем `processing_started`, адресное задание читается и создаётся result artifact.

Критерий полезного FAIL: автоматически фиксируется `activation_failed` с конкретной product boundary и доказательством причины. Успешный GitHub workflow, уведомление ОПЕРАТОРУ или просто наличие файла в inbox PASS не являются.

КОДЕРУ: выполнить техническую часть эксперимента и вернуть воспроизводимый результат. Если продукт ChatGPT требует однократного действия владельца аккаунта, вернуть КООРДИНАТОРУ ровно одно минимальное действие с указанием, зачем оно нужно и как проверить, что оно выполнено. Инфраструктуру/OSS/authority не расширять без отдельного решения.

status: authorized_for_e2e
from_entity: KOO
to_entity: KOD
project_time: omitted; trusted project-time source not used
