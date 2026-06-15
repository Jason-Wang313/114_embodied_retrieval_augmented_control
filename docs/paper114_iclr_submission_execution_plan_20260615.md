# Paper 114 ICLR Submission Execution Plan - 2026-06-15

Paper: `embodied_retrieval_augmented_control`

Target venue posture: ICLR main target, evidence-bound.

Current terminal posture before continuation: `STRONG_REVISE`, not ICLR-main ready.

## Goal

Re-audit Paper 114 as if preparing a real ICLR-main submission, while preserving an honest terminal decision. The paper may remain `STRONG_REVISE` only if the rerun reproduces a decisive local advantage for mechanism-indexed embodied retrieval over the strongest non-oracle retrieval baseline, without increasing incompatible retrievals, damage, or query cost. It must not be marked ICLR-main ready without real robot or independent high-fidelity validation.

## Execution Steps

1. Compile and rerun the experiment with low-RAM thread caps:

```powershell
$env:OMP_NUM_THREADS='1'
$env:OPENBLAS_NUM_THREADS='1'
$env:MKL_NUM_THREADS='1'
python -m py_compile src\run_experiment.py
python src\run_experiment.py *> C:\Users\wangz\robotics_massive_pool_paper_factory\logs\114_embodied_retrieval_augmented_control_continuation_rerun_20260615.log
```

2. Verify CSV integrity:
- `metrics.csv`: 45 rows.
- `per_task_regime_metrics.csv`: 1,575 rows.
- `seed_task_regime_metrics.csv`: 11,025 rows.
- `seed_split_metrics.csv`: 315 rows.
- `pairwise_stats.csv`: 8 rows.
- `ablation_metrics.csv`: 7 rows.
- `ablation_seed_metrics.csv`: 49 rows.
- `ablation_task_regime_seed_metrics.csv`: 1,715 rows.
- `stress_sweep.csv`: 24 aggregate rows.
- `stress_sweep_seed_metrics.csv`: target 5,880 task/regime/seed rows after recoverable coverage patch.
- `failure_cases.csv`: target 8 documented failure boundaries after recoverable coverage patch.

3. Verify result gates:
- Strongest non-oracle baseline remains `conformal_retrieval_filter`.
- Proposed method clears at least `+0.030` combined-stress success over the strongest non-oracle baseline.
- Mechanism precision improves by at least `+0.030`.
- Incompatible retrievals decrease by at least `0.020`.
- Damage and query cost do not regress.
- Recovery success improves by at least `+0.020`.
- Paired seed wins over the strongest non-oracle baseline are at least 5/7.
- Best removed-component ablation remains at least `0.020` success below the full method.

4. Harden documentation and paper:
- Update README, child status, decision docs, final audit, version log, checklists, hostile reviewer response, and manuscript text to v4.1.
- Make clear the evidence is local and generated.
- Preserve the narrow claim: embodied retrieval must be indexed by physical mechanism and action context, not merely language, visual similarity, state-nearest memory, uncertainty, or conformal filtering.

5. Build and verify artifact:
- Build `paper/main.pdf` with `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.
- Copy only to `C:/Users/wangz/Downloads/114.pdf`.
- Verify SHA256, file size, LaTeX/BibTeX warnings, public GitHub repo, and no `C:/Users/wangz/Desktop/114.pdf`.

6. Update root ledgers:
- `GLOBAL_POOL_STATUS.md`
- `BATCH_STATUS.md`
- `SUBMISSION_STATUS.md`
- `MASTER_REPORT.md`
- `MASTER_SUBMISSION_REPORT.md`

## Terminal Decision Rule

`STRONG_REVISE`: local mechanism-indexed retrieval evidence remains strong, stress/failure coverage is expanded, reproducibility and artifact gates pass, but real robot or independent high-fidelity evidence is missing.

`KILL_ARCHIVE`: rerun fails to reproduce the strongest-baseline, mechanism-precision, incompatible-retrieval, safety/cost, recovery, paired-seed, or ablation gates.

No `ICLR main ready` label is allowed without real robot or independent high-fidelity validation, trained retrieval/controller artifacts, and deeper manual related-work synthesis.
