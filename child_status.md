# Child Status 114

Current stage: ICLR main gate terminal
Last update: 2026-06-15 19:40:14 +0100
PDF: C:/Users/wangz/Downloads/114.pdf
PDF SHA256: A30F44414A79FF28C28E2232B2A4C89262A3277C5B20D931861EC829BF923B4E
GitHub: https://github.com/Jason-Wang313/114_embodied_retrieval_augmented_control
Submission-hardening version: v4.1
Terminal decision: STRONG_REVISE
ICLR main ready: no

Evidence digest:
- Proposed mechanism retrieval beats `conformal_retrieval_filter` by `0.103 +/- 0.005` combined-stress success with `7/7` paired-seed wins.
- Proposed success is `0.665 +/- 0.008`; strongest baseline success is `0.562 +/- 0.008`.
- Mechanism precision and recovery success increase; incompatible retrievals, damage, and query cost decrease.
- Best ablation trails the full method by `0.043` success.
- Stress sweep now covers `5,880` task/regime/seed rows and `24` aggregate rows.
- Failure-case documentation now covers `8` embodied-retrieval boundaries.
- Remaining blocker: no real robot or external high-fidelity benchmark validation.
