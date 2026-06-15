# Paper 114 Rebuild Plan

Started: 2026-06-15 02:48:00 +0100

## Goal

Rebuild `embodied_retrieval_augmented_control` from an archive memo into a real local empirical submission package. The paper must test whether retrieving prior robot episodes by physical mechanism similarity improves control under embodied shift compared with language, visual, uncertainty, and generic episodic retrieval baselines.

## Claim To Test

Retrieval-augmented robot control fails when retrieval keys are semantic or visual but the decisive failure mode is physical. A mechanism-indexed retrieval controller should retrieve episodes with matching contact, support, friction, compliance, and actuation structure, improving downstream control while reducing incompatible retrievals.

## Evidence Design

- Benchmark dimensions: 5 contact-rich tasks, 7 mechanism-shift regimes, 5 corpus/domain splits, 9 methods, 7 paired seeds, 84 rollout episodes per group.
- Methods: no retrieval, language retrieval, visual retrieval, nearest-state episodic memory, behavior cloning with retrieved context, uncertainty-gated retrieval, conformal retrieval filter, proposed mechanism retrieval controller, and oracle mechanism retrieval.
- Metrics: task success, mechanism-match precision, incompatible retrieval rate, collision/damage, recovery success, latency/query cost, calibration error, and paired-seed wins.
- Stress sweep: increasing mismatch between text/visual similarity and physical mechanism similarity.
- Ablations: remove mechanism index, remove action-conditioned retrieval key, remove counterfactual retrieval rejection, remove recovery controller, remove calibration guard, and top-1-only retrieval.

## Terminal Gates

The paper may become `STRONG_REVISE` only if all gates clear against the strongest non-oracle baseline:

- Combined-stress success margin is at least 0.030.
- Mechanism-match precision increases by at least 0.030.
- Incompatible retrieval rate decreases by at least 0.020.
- Damage and latency/query cost do not increase.
- Recovery success increases by at least 0.020.
- Paired-seed success wins are at least 5/7.
- Best ablation trails the full method by at least 0.020.

If any gate fails, the terminal decision remains `KILL_ARCHIVE` and the negative result is documented.

## Execution Steps

1. Replace the generic branch scaffold with a mechanism-retrieval control benchmark.
2. Generate per-seed/task/regime/split evidence, aggregate metrics, pairwise decisions, ablations, stress sweep, tables, and figures.
3. Remove stale branch-template artifacts if superseded.
4. Rewrite status docs, novelty docs, attack logs, and reproducibility docs around the v4 evidence.
5. Rewrite the manuscript as an ICLR-style evidence report with honest limitations.
6. Compile the PDF and copy `114.pdf` to Downloads only.
7. Audit Python, LaTeX, CSV finiteness, stale outputs, Git status, Downloads-only PDF placement, and GitHub visibility.
8. Update root reports only after Paper 114 reaches a terminal decision.
