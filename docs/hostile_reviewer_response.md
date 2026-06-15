# Hostile Reviewer Response

## Reviewer Attack: This is just RAG for robots.

Response: The evidence focuses on physical mechanism compatibility. Language and visual retrieval fail badly under combined mechanism shift (`0.405` and `0.462` success). The proposed mechanism-indexed controller reaches `0.665 +/- 0.008`.

## Reviewer Attack: A conformal retrieval filter should be enough.

Response: The strongest non-oracle baseline is `conformal_retrieval_filter` at `0.562 +/- 0.008`. The proposed method reaches `0.665 +/- 0.008`, a paired `0.103 +/- 0.005` gain with `7/7` seed wins, while also lowering incompatible retrieval, damage, and query cost.

## Reviewer Attack: The mechanism index may be decorative.

Response: Ablations reject that. The full method reaches `0.669 +/- 0.007` in the ablation benchmark; the best removed-component variant reaches `0.626 +/- 0.008`, leaving a `0.043` success gap.

## Reviewer Attack: The paper is not ready for ICLR main.

Response: Agreed. The honest decision is `STRONG_REVISE`, not ready. It needs real robot or external high-fidelity validation and a released retrieval corpus/checkpoints.
