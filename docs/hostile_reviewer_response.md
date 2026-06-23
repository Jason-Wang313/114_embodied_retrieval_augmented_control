# Hostile Reviewer Response

## Reviewer Attack: This is just RAG for robots.

Response: The v5 evidence focuses on physical mechanism compatibility, not generic semantic retrieval. The comparator set includes language, visual, state-nearest, behavior-clone, uncertainty, conformal, invariant, contrastive, learned-utility, model-predictive, active-retrieval, retained v4, proposed v5, and oracle methods. The strongest non-oracle baseline is the retained v4 controller, not a weak RAG baseline.

## Reviewer Attack: The previous mechanism retrieval controller should be enough.

Response: The retained v4 controller reaches hard success `0.66339` and utility `0.68129`. The v5 method reaches hard success `0.72389` and utility `0.79699`, wins `10/10` paired hard utility seeds, improves mechanism precision and recovery, and lowers incompatible retrieval, damage, query cost, and regret.

## Reviewer Attack: The mechanism index may be decorative.

Response: Ablations reject that locally. The best ablation trails the full method by `0.03768` success and `0.10562` utility. Removing mechanism indexing, action-conditioned keys, counterfactual rejection, recovery, calibration, stale-memory downweighting, active disambiguation, or retrieval diversity weakens the package.

## Reviewer Attack: The fixed-risk result is too easy.

Response: The strict fixed-risk budget was set to `0.10000`, not the easier `0.12000`. At this stricter budget, v5 coverage is `0.59500`, breach is `0.00000`, and utility margin is `+0.20791`, so the test forces abstention/fallback rather than rubber-stamping every retrieval.

## Reviewer Attack: The paper is not ready for ICLR main.

Response: Agreed. The honest decision is `STRONG_REVISE`, not ready. The v5 evidence is locally stronger, with 102,400 main cells, 8,000 ablation cells, 48,000 stress cells, 51,200 fixed-risk cells, 24 failure cases, a 25-page PDF, and a validator. It still needs real robot or accepted high-fidelity retrieval-control validation, trained checkpoints, calibrated mechanism logs, released corpus/checkpoint, rollout videos, and external-baseline confirmation.
