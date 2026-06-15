# Submission Attack Log

Paper: 114 embodied_retrieval_augmented_control

This v4.1 pass replaces the v3 archive decision with a local empirical rebuild and expanded continuation audit. The result is `STRONG_REVISE`, not final ICLR-main readiness.

## Attack 1: No real robot validation.

Verdict: Still a blocker for readiness.

Action: Preserve `ICLR main ready: no`.

## Attack 2: Generic RAG novelty.

Verdict: Addressed locally.

Action: Reframed around mechanism-compatible retrieval for control, not semantic document retrieval.

## Attack 3: Weak baselines.

Verdict: Addressed locally.

Action: Added language retrieval, visual retrieval, nearest-state memory, retrieved-context behavior cloning, uncertainty-gated retrieval, conformal retrieval, and oracle retrieval.

## Attack 4: Conformal retrieval may be enough.

Verdict: Addressed locally.

Action: Proposed beats conformal retrieval by `0.103 +/- 0.005`, wins `7/7` seeds, and improves retrieval-quality and safety diagnostics.

## Attack 5: Components may be unnecessary.

Verdict: Addressed locally.

Action: Best ablation trails full method by `0.043`, clearing the `0.020` gate.

## Attack 6: Missing corpus/checkpoints.

Verdict: Still a blocker for readiness.

Action: Document as required next evidence.

## Attack 7: Main-conference decision.

Verdict: STRONG_REVISE.

Action: Keep and expand; do not mark as submission-ready.

## Attack 8: Stress/failure coverage is thin.

Verdict: Addressed locally in v4.1.

Action: Expanded stress evidence to `5,880` task/regime/seed rows and failure documentation to `8` concrete embodied-retrieval boundaries.
