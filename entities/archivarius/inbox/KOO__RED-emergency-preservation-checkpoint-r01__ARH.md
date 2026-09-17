# KOO → ARH: RED emergency preservation/recovery checkpoint r0.1

Exact task source:
`entities/koordinator/outbox/KOO__RED-emergency-preservation-checkpoint-r01__ARH.md`
commit `999542a004cd1fb4bc6364ee24c6dd8aaee47ca7`

Выполни fresh HQ preflight и preservation/recovery checkpoint для RED без writer transfer. Установи текущий RED writer state, последний externally verified RED recovery и свежий evidence-tail, включая Anthropic contract task `4123ee9a...` и artifact `2b7e1c57...`. Если writer недоступен, зафиксируй failure-state без реконструкции self-state. Верни exact PASS/BLOCKED/FAIL КОО и остановись.
