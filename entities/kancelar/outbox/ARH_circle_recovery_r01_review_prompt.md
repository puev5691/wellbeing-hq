# ARH — bounded working-circle recovery review r0.1

Продолжай по Resume-First.

Сделай fresh GitHub-preflight `puev5691/wellbeing-hq`.

Exact experiment:
`entities/kancelar/outbox/KAN__bounded-working-circle-experiment-r01__OPERATOR-KOO-SHT-ARH.md`

Выполни bounded preservation/recovery review модели ограниченного рабочего круга.

Проверь:
1. минимальный circle-state, нужный для continuity;
2. recoverable identity круга vs временная topology;
3. single point of failure representative;
4. где хранить membership/representative mapping: recovery/current operational state/иначе;
5. какие topology данные нельзя тащить в recovery;
6. восстановление pending cross-circle task без replay historical tasks;
7. простой practical preservation test замены representative instance.

Не создавай новую recovery-норму и не меняй чужой current-state.
Верни bounded review KAN + OPERATOR.
После terminal result остановись.