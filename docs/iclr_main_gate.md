# ICLR Main Gate

Paper: 114 embodied_retrieval_augmented_control

Existing v3 decision: KILL_ARCHIVE

v4.1 gate verdict: STRONG_REVISE

Evidence digest: embodied-mechanism-retrieval-local-v4.1

## Passed Local Gates

- Success margin over strongest non-oracle baseline: `0.103 >= 0.030`.
- Mechanism-precision delta: `0.085 >= 0.030`.
- Incompatible-retrieval delta: `-0.083 <= -0.020`.
- Damage delta: `-0.022 <= 0`.
- Query-cost delta: `-0.029 <= 0`.
- Recovery-success delta: `0.083 >= 0.020`.
- Paired-seed wins: `7/7 >= 5/7`.
- Ablation margin: `0.043 >= 0.020`.
- Expanded stress coverage: `5,880` task/regime/seed rows.
- Failure-case coverage: `8` rows.
- Numeric integrity: no NaN or infinite values.

## Remaining Main-Conference Blockers

- No real robot validation.
- No external high-fidelity simulator benchmark.
- No released retrieval corpus/checkpoints.
- Related work still needs manual full-paper synthesis.

The only honest main-conference-safe terminal state is STRONG_REVISE.
