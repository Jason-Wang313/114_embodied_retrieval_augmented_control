# ICLR Main Gate

Paper: 114 embodied_retrieval_augmented_control

Earlier v3 decision: KILL_ARCHIVE

v5 gate verdict: STRONG_REVISE

Evidence digest: embodied-retrieval-control-local-v5-expanded

## Passed Local Gates

- Hard success margin over strongest non-oracle baseline: `+0.06049 > 0`.
- Hard utility margin over strongest non-oracle baseline: `+0.11570 > 0`.
- Mechanism precision delta: `+0.06009 > 0`.
- Incompatible-retrieval delta: `-0.03436 < 0`.
- Recovery-success delta: `+0.05821 > 0`.
- Damage-rate delta: `-0.01149 <= 0`.
- Query-cost delta: `-0.01485 <= 0`.
- Regret delta: `-0.01858 <= 0`.
- Paired hard utility wins: `10/10`.
- Ablation utility margin: `+0.10562`.
- Stress endpoint utility margin: `+0.13756`.
- Fixed-risk coverage at strict budget `0.10000`: `0.59500`.
- Fixed-risk breach: `0.00000`.
- Fixed-risk utility margin: `+0.20791`.
- Evidence scale: 102,400 main cells, 8,000 ablation cells, 48,000 stress cells, 51,200 fixed-risk cells, and 24 failure cases.
- PDF integrity: 25 pages, bright boxed clickable citations, and Downloads-only final artifact.
- Numeric integrity: validator reports no NaN or infinite values.

## Failed Scope Gate

- No real robot retrieval-control validation.
- No accepted high-fidelity retrieval-control simulator benchmark.
- No trained controller or retrieval checkpoint release.
- No calibrated mechanism logs.
- No released retrieval corpus or checkpoint.
- No hardware rollout videos.

The only honest main-conference-safe terminal state is STRONG_REVISE.
