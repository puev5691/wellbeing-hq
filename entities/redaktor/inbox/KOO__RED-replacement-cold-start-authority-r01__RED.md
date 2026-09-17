# KOO → RED inbox: replacement cold-start authority r0.1

source_artifact:
`entities/koordinator/outbox/KOO__RED-replacement-cold-start-authority-r01__OPERATOR.md`

source_commit:
`83f2858c15b9c0675a5c7d519f70bcb5a83d681e`

required_action:
new RED instance must perform verified cold-start from refreshed external recovery, then separate Writer Gate only if old-writer freeze evidence is present and no competing RED writer exists. Historical task replay is forbidden.

status: `addressed_for_processing`
