# 114 Embodied Retrieval-Augmented Control

Submission-hardening version: v4

Terminal decision: STRONG_REVISE for an ICLR-main-target robotics submission package.

This rebuild replaces the archive/template scaffold with a paper-specific local benchmark for retrieval-augmented robot control. The evidence supports a strong-revise direction: mechanism-indexed retrieval beats language, visual, state-nearest, uncertainty-gated, and conformal retrieval baselines under embodied mechanism shift. The paper is not yet ICLR-main ready because it lacks real robot or external high-fidelity validation.

## Evidence Snapshot

- Design: 5 tasks x 7 mechanism-shift regimes x 5 corpus/domain splits x 9 methods, 7 paired seeds, 84 rollout episodes per group.
- Strongest non-oracle baseline: `conformal_retrieval_filter`.
- Combined-stress success: proposed `0.665 +/- 0.008` vs baseline `0.562 +/- 0.008`.
- Paired difference: `0.103 +/- 0.005`, wins `7/7` seeds.
- Mechanism-precision delta: `+0.085`.
- Incompatible-retrieval delta: `-0.083`.
- Damage delta: `-0.022`; query-cost delta: `-0.029`.
- Recovery-success delta: `+0.083`.
- Best ablation gap: `0.043`.

## Reproduce

```powershell
pip install -r requirements.txt
python src\run_experiment.py
```

## Rebuild PDF

```powershell
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Canonical local PDF: `C:/Users/wangz/Downloads/114.pdf`
