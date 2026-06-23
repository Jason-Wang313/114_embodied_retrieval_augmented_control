# Literature Map

## Retrieval-Augmented Generation

General RAG retrieves documents or examples by semantic similarity. That literature motivates retrieval at test time but does not solve embodied compatibility: a semantically similar prior episode can be physically wrong for the current contact mechanism.

## Episodic Control And Robot Memory

Robot memory and episodic control retrieve prior trajectories or states. Paper 114 narrows the key question to mechanism matching: retrieved episodes must share support, friction, compliance, actuation, tool geometry, stale-memory status, and recovery structure.

## Uncertainty, Conformal Filtering, And Retained Prior Guarding

Uncertainty-gated and conformal retrieval filters are close baselines, but the strongest v5 non-oracle comparator is the retained prior mechanism controller, `proposed_mechanism_retrieval_controller_v4`. The new method improves hard success by `+0.06049`, hard utility by `+0.11570`, and wins `10/10` paired hard utility seeds while reducing incompatible retrieval, damage, query cost, and regret.

## Control And Safety Boundary

The paper should be positioned as a retrieval-control safety and mechanism-compatibility audit, not as a general robot foundation model. The fixed-risk suite helps connect retrieval quality to physical risk, but it is not a substitute for hardware safety validation.

## Remaining Related-Work Work

This map is still a hostile-pool synthesis, not a final related-work section. A submission-ready version needs manual full-paper reading and precise comparisons to embodied memory, case-based planning, retrieval-conditioned imitation learning, conformal robotics, and robot foundation-model memory systems.
