# Experiment Rigor Checklist

## v5 Local Empirical Rigor

- [x] Paper-specific embodied retrieval-control benchmark.
- [x] 10 contact/control tasks.
- [x] 8 mechanism-shift regimes.
- [x] 8 corpus/domain splits.
- [x] 16 methods including strong non-oracle baselines and oracle upper bound.
- [x] Retained v4.1 controller as the strongest non-oracle baseline.
- [x] 10 paired seeds.
- [x] Main evidence at 102,400 task/regime/split/method/seed cells.
- [x] Seed-level, aggregate, and group-level metrics.
- [x] Pairwise hard-seed differences and win counts.
- [x] Stress sweep with 48,000 cells.
- [x] Fixed-risk evaluation with 51,200 cells and strict budget 0.10000.
- [x] Ablation evaluation with 8,000 cells.
- [x] Twenty-four failure cases and limitations.
- [x] Paper-specific figures and generated LaTeX tables.
- [x] Bright boxed clickable citations in the PDF.
- [x] Validator checking row counts, gates, PDF hash, page count, and artifact placement.
- [x] Rendered-page visual QA on pages 1, 4, 9, 17, and 25.

## ICLR Main Remaining Gaps

- [ ] Real robot retrieval-control validation.
- [ ] Accepted high-fidelity retrieval-control simulator benchmark.
- [ ] Release of trained retrieval/controller checkpoints.
- [ ] Calibrated mechanism logs.
- [ ] Released retrieval corpus or checkpoint package.
- [ ] Hardware qualitative rollouts or failure videos.
- [ ] External retrieval-control baseline confirmation.

Decision: STRONG_REVISE, not submission-ready.
