# E2E test: activation state recording

sender: koordinator
recipient: koder
purpose: trigger extended entity-activation-detector and verify automatic creation of an activation state record
required_action: none; this is a detector/state-machine test only
expected_result: GitHub workflow detects this inbox locator and writes routes/activation/KOO__activation-state-e2e-test__KOD.activation.md with explicit activation_requested and either processing_started or activation_failed
safety_boundary: do not claim exact Entity-chat resume unless independently proven
project_time: omitted; trusted project-time source not used
