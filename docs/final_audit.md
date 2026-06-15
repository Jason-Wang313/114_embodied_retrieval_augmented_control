# Final Audit

Paper: 114 embodied_retrieval_augmented_control

Submission-hardening version: v4.1

Terminal decision: STRONG_REVISE

## Evidence

The archive scaffold was replaced with a mechanism-retrieval benchmark. The benchmark evaluates 5 tasks, 7 mechanism regimes, 5 corpus/domain splits, 9 methods, 7 seeds, and 84 rollout episodes per group. The proposed mechanism retrieval controller beats the strongest non-oracle baseline, `conformal_retrieval_filter`, under combined stress.

Key results:
- Success: `0.665 +/- 0.008` proposed vs `0.562 +/- 0.008` strongest baseline.
- Paired difference: `0.103 +/- 0.005`; wins `7/7`.
- Mechanism-precision delta: `+0.085`.
- Incompatible-retrieval delta: `-0.083`.
- Recovery-success delta: `+0.083`.
- Damage delta: `-0.022`.
- Query-cost delta: `-0.029`.
- Best ablation gap: `0.043`.
- Stress sweep coverage: `5,880` task/regime/seed rows and `24` aggregate rows.
- Failure cases: `8` documented embodied-retrieval boundaries.
- Numeric integrity: no NaN or infinite values found across result CSVs.

Artifact audit passes: `C:/Users/wangz/Downloads/114.pdf` exists, is 418,378 bytes, has SHA256 `A30F44414A79FF28C28E2232B2A4C89262A3277C5B20D931861EC829BF923B4E`, and `C:/Users/wangz/Desktop/114.pdf` is absent.

## Remaining Risk

The result is local benchmark evidence. It lacks real robot experiments, external high-fidelity simulator transfer, released retrieval corpus/checkpoints, and hardware videos. The correct terminal action is strong revise, not ICLR-main-ready submission.
