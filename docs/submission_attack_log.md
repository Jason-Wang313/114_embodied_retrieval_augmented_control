# Submission Attack Log

Paper: 114 embodied_retrieval_augmented_control

The v5_expanded pass replaces the earlier v4.1 continuation package with a 25-page local submission audit. The result is `STRONG_REVISE`, not final ICLR-main readiness.

## Attack 1: No real robot validation.

Verdict: Still a blocker for readiness.

Action: Preserve `ICLR main ready: no`; require real robot or accepted high-fidelity retrieval-control validation before final submission.

## Attack 2: Generic RAG novelty.

Verdict: Addressed locally.

Action: Reframed around action-conditioned mechanism-compatible retrieval for control, not semantic document retrieval.

## Attack 3: Weak baselines.

Verdict: Addressed locally.

Action: Included language, visual, state-nearest, behavior-clone, uncertainty, conformal, test-time adaptation, invariant alignment, contrastive memory, learned expected utility, model-predictive arbitration, failure-aware active retrieval, retained v4 controller, proposed v5, and oracle comparisons.

## Attack 4: The retained v4 controller may be enough.

Verdict: Addressed locally.

Action: v5 beats retained v4 by `+0.06049` hard success and `+0.11570` hard utility, wins `10/10` paired hard utility seeds, and improves mechanism precision, incompatible retrieval, recovery, damage, query cost, and regret.

## Attack 5: Components may be unnecessary.

Verdict: Addressed locally.

Action: Best ablation trails the full method by `0.03768` success and `0.10562` utility.

## Attack 6: Missing corpus/checkpoints.

Verdict: Still a blocker for readiness.

Action: Document as a remaining requirement. The v5 benchmark is evidence for a rebuild direction, not a final trained model or retrieval-corpus release.

## Attack 7: Main-conference decision.

Verdict: STRONG_REVISE.

Action: Keep and expand with external validation; do not mark as submission-ready.

## Attack 8: Stress/failure/fixed-risk coverage is thin.

Verdict: Addressed locally.

Action: Expanded stress evidence to 48,000 stress cells, fixed-risk evidence to 51,200 cells, and failure documentation to 24 embodied-retrieval boundaries.
