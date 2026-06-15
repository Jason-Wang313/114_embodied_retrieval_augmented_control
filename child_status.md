# Child Status 114

Current stage: ICLR main gate terminal
Last update: 2026-06-15 02:56:13 +0100
PDF: C:/Users/wangz/Downloads/114.pdf
GitHub: https://github.com/Jason-Wang313/114_embodied_retrieval_augmented_control
Submission-hardening version: v4
Terminal decision: STRONG_REVISE
ICLR main ready: no

Evidence digest:
- Proposed mechanism retrieval beats `conformal_retrieval_filter` by `0.103 +/- 0.005` combined-stress success with `7/7` paired-seed wins.
- Proposed success is `0.665 +/- 0.008`; strongest baseline success is `0.562 +/- 0.008`.
- Mechanism precision and recovery success increase; incompatible retrievals, damage, and query cost decrease.
- Best ablation trails the full method by `0.043` success.
- Remaining blocker: no real robot or external high-fidelity benchmark validation.
