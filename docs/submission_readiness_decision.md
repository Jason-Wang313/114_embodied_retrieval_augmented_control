# Submission Readiness Decision

Decision: STRONG_REVISE

ICLR main-conference readiness: NO.

Reason: The v5 rebuild creates a 25-page submission audit with a frozen CPU-only benchmark, strong retained baselines, ablations, stress sweeps, fixed-risk tests, failure cases, and bright boxed clickable citations. The proposed method beats the retained v4 controller on hard success, hard utility, mechanism precision, incompatible retrieval, recovery success, damage, query cost, regret, stress endpoint utility, and fixed-risk utility. All frozen local gates pass.

Honest terminal action: keep and revise aggressively. Do not submit as final ICLR main paper until external retrieval-control validation is added.

Revival-to-ready condition: add real robot retrieval-control experiments or an accepted high-fidelity simulator, train/release retrieval and controller checkpoints, provide calibrated mechanism logs and rollout videos, release a retrieval corpus/checkpoint, compare to external baselines, and deepen related work with manual full-paper synthesis.
