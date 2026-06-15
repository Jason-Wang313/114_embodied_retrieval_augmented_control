# Novelty Boundary Map

## Inside The Claim

- Mechanism-indexed retrieval for robot control.
- Action-conditioned retrieval keys.
- Counterfactual rejection of physically incompatible episodes.
- Recovery control triggered by mechanism-matched memories.
- Control metrics for retrieval quality.

## Outside The Claim

- General RAG for text.
- Universal robot memory.
- Real hardware SOTA.
- Replacing system identification.
- External benchmark generality.

## Closest Baseline Boundary

The closest local competitor is `conformal_retrieval_filter`. It rejects uncertain retrievals but does not encode physical mechanism compatibility. The proposed method wins by `0.103 +/- 0.005` combined-stress success and reduces incompatible retrievals by `0.083`.
