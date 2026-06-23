# Final Audit

Paper: 114 embodied_retrieval_augmented_control

Submission-hardening version: v5_expanded

Terminal decision: STRONG_REVISE

ICLR main ready: NO

## Evidence

The v5 rebuild expands the embodied retrieval-control package into a 25-page submission audit. The frozen CPU-only experiment evaluates 10 tasks, 8 mechanism-shift regimes, 8 corpus/domain splits, 16 methods, and 10 paired seeds. It records 102,400 main cells, 10,240 main group rows, 1,280 seed metrics, 128 aggregate metrics, 8,000 ablation cells, 48,000 stress cells, 51,200 fixed-risk cells, and 24 failure cases.

Key results:
- Proposed method: `action_conditioned_mechanism_retrieval_v5`.
- Strongest non-oracle: `proposed_mechanism_retrieval_controller_v4`.
- Oracle: `oracle_mechanism_retrieval`.
- Hard success: `0.72389` proposed vs `0.66339` strongest non-oracle.
- Hard utility: `0.79699` proposed vs `0.68129` strongest non-oracle.
- Hard margins: success `+0.06049`, utility `+0.11570`.
- Paired hard utility wins: `10/10`.
- Mechanism precision delta: `+0.06009`.
- Incompatible-retrieval delta: `-0.03436`.
- Recovery-success delta: `+0.05821`.
- Damage-rate delta: `-0.01149`.
- Query-cost delta: `-0.01485`.
- Regret delta: `-0.01858`.
- Ablation utility margin: `+0.10562`.
- Stress endpoint utility margin: `+0.13756`.
- Strict fixed-risk budget: `0.10000`.
- Strict fixed-risk coverage: `0.59500`.
- Strict fixed-risk breach: `0.00000`.
- Strict fixed-risk utility margin: `+0.20791`.
- Numeric integrity: no NaN or infinite values found by the validator.

Artifact audit passes: `C:/Users/wangz/Downloads/114.pdf` exists, has 25 pages, is 785,264 bytes, has SHA256 `83CFE32A3356ADD3EF335B5CA4966F972320D65B548118A1BA4C1716A2701412`, and `C:/Users/wangz/Desktop/114.pdf` is absent.

## Remaining Risk

The result remains local evidence. It does not include real robot retrieval-control rollouts, accepted high-fidelity retrieval-control simulation, trained controller/retrieval checkpoints, calibrated mechanism logs, a released retrieval corpus/checkpoint, or rollout videos. The correct terminal action is strong revise, not ICLR-main-ready submission.
