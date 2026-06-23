# Paper 114 Expanded Submission Plan - 2026-06-23

Paper: `embodied_retrieval_augmented_control`

Target posture: ICLR-main-targeted, evidence-bound, hostile-review-ready local audit.

Current status before v5: v4.1 `STRONG_REVISE`, not ICLR-main ready.

## Goal

Rebuild Paper 114 into a 25+ page submission-audit artifact that tests whether retrieval-augmented control should retrieve by physical mechanism compatibility rather than language, visual, or state similarity. The paper should be strengthened as far as possible under CPU-only and RAM-light constraints, while preserving an honest decision.

## Frozen Experimental Protocol

- Tasks: 10 contact/control tasks covering drawers, peg insertion, cable routing, cloth motion, force-limited twisting, latch release, granular scooping, deformable packing, mobile base alignment, and bimanual handoff.
- Regimes: 8 mechanism shifts covering source matched, friction, support topology, compliance, occluded contact, actuator lag, tool geometry, and compound shift.
- Splits: 8 corpus/domain splits covering seen corpus, held-out object, held-out mechanism, cross embodiment, sparse corpus, stale memory, visually aliased, and combined stress.
- Methods: 16 non-oracle/proposed/oracle methods with the old v4.1 mechanism retrieval controller retained as a strong non-oracle baseline.
- Seeds: 10 paired seeds.
- Metrics: success, utility, mechanism precision, incompatible retrieval, recovery success, damage, query cost, regret, calibration error, and retrieval coverage.

## Hostile Baselines

The non-oracle comparator set includes no retrieval, language retrieval, visual retrieval, state-nearest memory, retrieved-context behavior cloning, uncertainty-gated retrieval, conformal retrieval filtering, test-time retrieval adaptation, invariant retrieval alignment, contrastive mechanism memory, learned expected utility retrieval, model-predictive retrieval arbitration, failure-aware active retrieval, and the retained v4.1 controller.

## Predefined Gates

The paper may remain `STRONG_REVISE` only if the v5 method beats the strongest non-oracle baseline on hard success and hard utility; improves mechanism precision, incompatible retrieval, recovery, damage, query cost, regret, stress endpoint utility, paired hard utility, fixed-risk coverage, and fixed-risk utility; and survives ablations. Otherwise the decision becomes `KILL_ARCHIVE`.

## Scope Boundary

Even if every local gate passes, the paper is not ICLR-main ready without real robot or accepted high-fidelity retrieval-control evidence, trained checkpoints, calibrated mechanism logs, released retrieval corpus/checkpoint, and rollout videos.

## Artifact Rules

- Produce a numbered PDF only at `C:/Users/wangz/Downloads/114.pdf`.
- Keep no visible Desktop PDF copy.
- Use bright boxed clickable citations.
- Commit and push the public repo only after validator and visual PDF QA pass.
