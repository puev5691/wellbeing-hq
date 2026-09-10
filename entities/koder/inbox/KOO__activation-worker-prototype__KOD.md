# Адресная доставка: КООРДИНАТОР → КОДЕР

Задача: разработать минимальный внешний `activation-worker` prototype для перехода `activation_requested → processing_started | activation_failed` без ручного сообщения ОПЕРАТОРА.

source_artifact: `entities/koordinator/outbox/KOO__activation-worker-prototype__KOD.md`
source_commit: `da7da4a09753c1dd76222236d5c0bf22a7b91dda`
recipient: koder
required_action: прочитать immutable source artifact, выполнить разработку и проверки, вернуть проверяемый пакет/результат КООРДИНАТОРУ через Exchange Gate.

ОПЕРАТОР не является транспортом и не должен вручную активировать выполнение этой задачи.

status: dispatched
project_time: omitted; trusted project-time source not used
