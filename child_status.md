# Child Status 114

Current stage: expanded-standard v5 terminal
Last update: 2026-06-23 15:01:17 +08:00
PDF: C:/Users/wangz/Downloads/114.pdf
PDF SHA256: 83CFE32A3356ADD3EF335B5CA4966F972320D65B548118A1BA4C1716A2701412
PDF pages: 25
PDF bytes: 785264
GitHub: https://github.com/Jason-Wang313/114_embodied_retrieval_augmented_control
Submission-hardening version: v5_expanded
Terminal decision: STRONG_REVISE
ICLR main ready: no

Evidence digest:
- Proposed method `action_conditioned_mechanism_retrieval_v5` beats strongest non-oracle `proposed_mechanism_retrieval_controller_v4`.
- Hard success is `0.72389` proposed vs `0.66339` strongest non-oracle.
- Hard utility is `0.79699` proposed vs `0.68129` strongest non-oracle.
- Paired hard utility wins are `10/10`.
- Mechanism precision and recovery success increase; incompatible retrieval, damage, query cost, and regret decrease.
- Evidence scale is 102,400 main cells, 8,000 ablation cells, 48,000 stress cells, 51,200 fixed-risk cells, and 24 failure cases.
- Strict fixed-risk budget is `0.10000`, coverage is `0.59500`, breach is `0.00000`, and utility margin is `+0.20791`.
- All frozen local gates pass.
- Remaining blocker: no real robot retrieval-control rollouts, accepted high-fidelity retrieval-control simulation, trained checkpoints, calibrated mechanism logs, released corpus/checkpoint, or rollout videos.
