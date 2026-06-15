# Submission Readiness Decision

Decision: STRONG_REVISE

ICLR main-conference readiness: NO.

Reason: The v4.1 rebuild adds a paper-specific mechanism-retrieval control benchmark with strong local evidence. The proposed controller beats `conformal_retrieval_filter` by `0.103 +/- 0.005` combined-stress success, wins `7/7` paired seeds, improves mechanism precision and recovery success, lowers incompatible retrievals, damage, and query cost, survives ablations, expands stress coverage to `5,880` task/regime/seed rows, documents `8` failure cases, and has no numeric-integrity issues.

Honest terminal action: keep and revise aggressively. Do not submit as final ICLR main paper until external validation is added.

Revival-to-ready condition: add real robot or accepted high-fidelity simulator experiments, release retrieval corpus/controller artifacts, compare to external robot-memory baselines, and deepen related work through manual full-paper reading.
