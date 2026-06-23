# Novelty Boundary Map

## Inside The Claim

- Mechanism-indexed retrieval for robot control.
- Action-conditioned retrieval keys.
- Counterfactual rejection of physically incompatible episodes.
- Stale-memory downweighting.
- Recovery control triggered by mechanism-matched memories.
- Fixed-risk retrieval budgets.
- Control metrics for retrieval quality.

## Outside The Claim

- General RAG for text.
- Universal robot memory.
- Real hardware SOTA.
- Replacing system identification.
- External benchmark generality.
- Deployed safety under calibrated robot logs.

## Closest Baseline Boundary

The closest current local competitor is the retained prior mechanism controller, `proposed_mechanism_retrieval_controller_v4`. It is strong because it already encodes mechanism retrieval. The v5 method still wins by `+0.06049` hard success and `+0.11570` hard utility, with `10/10` paired hard utility wins and better mechanism precision, incompatible retrieval, recovery, damage, query cost, regret, stress-endpoint, and fixed-risk diagnostics.
