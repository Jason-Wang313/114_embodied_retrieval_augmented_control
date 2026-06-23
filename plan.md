# Plan

Build Paper 114 `embodied_retrieval_augmented_control` into an expanded-standard v5 submission-audit package.

## Non-Negotiable Constraints

- Work one paper at a time.
- Use CPU-only execution with light RAM/thread settings.
- Do not optimize for pretty results. Optimize for hostile-review survival.
- Freeze the protocol before interpreting results.
- Report all predefined results honestly.
- Keep the final numbered PDF in `C:/Users/wangz/Downloads/114.pdf` only.
- Do not copy any PDF to the visible Desktop.
- Use bright boxed clickable in-text citations that jump to the reference section.
- Do not mark ICLR-main ready without real robot or accepted high-fidelity validation.

## Frozen v5 Scope

- Expand from v4.1 to a 25+ page manuscript only through new method/theory, experiment, ablation, stress, fixed-risk, failure-case, related-work-boundary, and reproducibility content.
- Main benchmark: 10 contact/control tasks x 8 mechanism-shift regimes x 8 corpus/domain splits x 16 methods x 10 paired seeds = 102,400 main cells.
- Ablations: 10 component/removal variants x 10 tasks x 8 regimes x 10 seeds = 8,000 cells.
- Stress sweep: 6 stress levels x 10 tasks x 8 regimes x 10 seeds x 10 methods = 48,000 cells.
- Fixed-risk retrieval budget: 4 budgets x 8 methods x 8 splits x 10 tasks x 2 deployment-risk profiles x 10 seeds = 51,200 cells.
- Failure cases: 24 documented embodied-retrieval boundaries.

## Strong Baselines

The v5 comparator set must include no retrieval, language retrieval, visual retrieval, state-nearest memory, retrieved-context behavior cloning, uncertainty-gated retrieval, conformal retrieval filtering, test-time retrieval adaptation, invariant retrieval alignment, contrastive mechanism memory, learned expected utility retrieval, model-predictive retrieval arbitration, failure-aware active retrieval, the retained v4.1 method as `proposed_mechanism_retrieval_controller_v4`, the new v5 method, and an oracle upper bound.

## Evidence Gates

The paper may remain `STRONG_REVISE` only if all local frozen gates pass:

- v5 hard success exceeds the strongest non-oracle baseline.
- v5 hard utility exceeds the strongest non-oracle baseline.
- mechanism precision improves.
- incompatible retrieval decreases.
- recovery success improves.
- damage does not increase.
- query cost does not increase.
- regret does not increase.
- paired hard utility wins are at least 8/10 seeds.
- ablations trail the full method on success or utility.
- stress endpoint utility remains positive against the strongest non-oracle baseline.
- fixed-risk coverage and utility gates pass.
- all numeric and artifact validators pass.

## Scope Gate

ICLR-main readiness is false unless the package includes real robot rollouts or accepted high-fidelity robotic retrieval-control validation, trained controller/retrieval checkpoints, calibrated mechanism logs, a released retrieval corpus or checkpoint, and rollout videos. If those are absent, the correct terminal state is either `STRONG_REVISE` or `KILL_ARCHIVE`, never ready.

## Execution Order

1. Implement the frozen v5 experiment and run it with CPU-only/RAM-light thread settings.
2. Generate all result CSVs, figures, LaTeX tables, summary JSON, and failure cases.
3. Generate the expanded manuscript with bright boxed citations and no fabricated claims.
4. Compile the PDF, copy only `114.pdf` to Downloads, and compute SHA256.
5. Validate row counts, gates, numeric integrity, PDF page count, citation settings, hash, artifact placement, and log sanity.
6. Render representative PDF pages to PNG and visually inspect layout.
7. Update child docs, final audit, readiness decision, README, and child status.
8. Commit and push the public GitHub repo.
9. Update shared root ledgers.
