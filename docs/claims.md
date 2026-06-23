# Claims

- Mechanism claim: retrieval-augmented control can fail when language, visual, or state-nearest memories are semantically close but physically mechanism-incompatible with the current action.
- Method claim: an action-conditioned mechanism key with counterfactual rejection, stale-memory downweighting, calibration, and recovery arbitration can retain useful retrieval context while rejecting harmful memories.
- Evidence claim: the v5 local benchmark shows `action_conditioned_mechanism_retrieval_v5` beats retained v4 baseline `proposed_mechanism_retrieval_controller_v4` with hard success `0.72389` vs `0.66339`, hard utility `0.79699` vs `0.68129`, and `10/10` paired hard utility wins.
- Safety and cost claim: v5 improves mechanism precision by `+0.06009`, incompatible retrieval by `-0.03436`, recovery success by `+0.05821`, damage by `-0.01149`, query cost by `-0.01485`, and regret by `-0.01858`.
- Evidence-scale claim: the current package contains 102,400 main cells, 8,000 ablation cells, 48,000 stress cells, 51,200 fixed-risk cells, and 24 failure cases.
- Scope claim: the result is strong local evidence for an expanded submission rebuild, not final ICLR-main readiness.
- Unsupported claim explicitly avoided: no claim of real-robot SOTA, external benchmark superiority, deployed safety, or released retrieval-control artifact readiness.
