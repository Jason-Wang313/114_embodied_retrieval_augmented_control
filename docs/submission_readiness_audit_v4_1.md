# Submission Readiness Audit v4.1

Paper: 114 `embodied_retrieval_augmented_control`

Date: 2026-06-15

Terminal decision: STRONG_REVISE

ICLR main ready: no

## Evidence Rerun

Command:

```powershell
$env:OMP_NUM_THREADS='1'
$env:OPENBLAS_NUM_THREADS='1'
$env:MKL_NUM_THREADS='1'
python -m py_compile src\run_experiment.py
python src\run_experiment.py *> C:\Users\wangz\robotics_massive_pool_paper_factory\logs\114_embodied_retrieval_augmented_control_continuation_rerun_20260615.log
```

## Integrity Gates

- `metrics.csv`: 45 rows.
- `per_task_regime_metrics.csv`: 1,575 rows.
- `seed_task_regime_metrics.csv`: 11,025 rows.
- `seed_split_metrics.csv`: 315 rows.
- `pairwise_stats.csv`: 8 rows.
- `ablation_metrics.csv`: 7 rows.
- `ablation_seed_metrics.csv`: 49 rows.
- `ablation_task_regime_seed_metrics.csv`: 1,715 rows.
- `stress_sweep.csv`: 24 rows.
- `stress_sweep_seed_metrics.csv`: 5,880 task/regime/seed rows.
- `failure_cases.csv`: 8 rows.
- Numeric sanity: no NaN or infinite values found.

## Result Gates

- Strongest non-oracle baseline: `conformal_retrieval_filter`.
- Combined-stress success: `0.665 +/- 0.008` proposed vs `0.562 +/- 0.008` baseline.
- Paired success gain: `0.103 +/- 0.005`, 7/7 seed wins.
- Mechanism precision: `0.609` proposed vs `0.524` baseline.
- Incompatible retrieval: `0.119` proposed vs `0.201` baseline.
- Recovery success: `0.571` proposed vs `0.488` baseline.
- Damage rate: `0.065` proposed vs `0.087` baseline.
- Query cost: `0.240` proposed vs `0.269` baseline.
- Ablation margin over best removed component: `0.043`.
- Max stress success: `0.608 +/- 0.007` proposed vs `0.465 +/- 0.008` conformal retrieval and `0.735 +/- 0.007` oracle.

## Submission Decision

The local evidence clears the strong-revise gate: strongest-baseline margin, mechanism-precision gain, incompatible-retrieval reduction, recovery gain, damage/query-cost non-regression, paired-seed wins, ablation margin, expanded stress detail, and failure-case documentation all pass.

The paper is not ICLR-main ready. It still needs real robot or independent high-fidelity validation, released retrieval/controller artifacts, hardware/video artifacts, and deeper manual related-work synthesis before submission.

## Artifact Gate

- PDF: `C:/Users/wangz/Downloads/114.pdf`.
- SHA256: `A30F44414A79FF28C28E2232B2A4C89262A3277C5B20D931861EC829BF923B4E`.
- Size: `418378` bytes.
- Desktop copy: absent.
- LaTeX scan: no substantive warnings; only the `rerunfilecheck` package line matched the warning scan after the final pass.
- BibTeX scan: `missing$ -- 0` and `warning$ -- 0`.
