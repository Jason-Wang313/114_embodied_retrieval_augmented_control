# 114 Embodied Retrieval-Augmented Control

Submission-hardening version: v5_expanded

Terminal decision: STRONG_REVISE for an ICLR-main-target robotics submission package.

This expanded rebuild replaces the v4.1 continuation package with a 25-page local submission audit for embodied retrieval-augmented control. The proposed v5 method retrieves by action-conditioned mechanism compatibility rather than language, visual, or state-nearest similarity alone. It beats the retained v4.1 mechanism-retrieval controller, which is the strongest non-oracle baseline, under hard mechanism shift, ablations, stress sweeps, and fixed-risk retrieval budgets.

The paper is still not ICLR-main ready because the scope gate fails: no real robot retrieval-control rollouts, accepted high-fidelity retrieval-control simulation, trained controller/retrieval checkpoint, calibrated mechanism logs, released retrieval corpus/checkpoint, or rollout videos are present.

## Evidence Snapshot

- Design: 10 contact/control tasks x 8 mechanism-shift regimes x 8 corpus/domain splits x 16 methods x 10 paired seeds.
- Main evidence: 102,400 main cells, 10,240 main group rows, 1,280 seed metrics, and 128 aggregate metrics.
- Additional evidence: 8,000 ablation cells, 48,000 stress cells, 51,200 fixed-risk cells, and 24 documented failure cases.
- Proposed method: `action_conditioned_mechanism_retrieval_v5`.
- Strongest non-oracle baseline: `proposed_mechanism_retrieval_controller_v4`.
- Oracle upper bound: `oracle_mechanism_retrieval`.
- Hard success: proposed `0.72389` vs strongest non-oracle `0.66339`.
- Hard utility: proposed `0.79699` vs strongest non-oracle `0.68129`.
- Hard margins: success `+0.06049`, utility `+0.11570`, with `10/10` paired hard utility wins.
- Diagnostics: mechanism precision delta `+0.06009`, incompatible-retrieval delta `-0.03436`, recovery-success delta `+0.05821`, damage-rate delta `-0.01149`, query-cost delta `-0.01485`, regret delta `-0.01858`.
- Stress endpoint utility margin: `+0.13756`.
- Fixed-risk result: strict budget `0.10000`, coverage `0.59500`, breach `0.00000`, utility margin `+0.20791`.
- Local gates: all frozen local gates pass.
- Citation behavior: in-text citations are bright boxed clickable links routed to the reference section.

## Reproduce

```powershell
pip install -r requirements.txt
python src\run_experiment.py
python scripts\generate_manuscript.py
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
cd ..
python scripts\validate_submission_artifacts.py
```

Canonical local PDF: `C:/Users/wangz/Downloads/114.pdf`

PDF SHA256: `83CFE32A3356ADD3EF335B5CA4966F972320D65B548118A1BA4C1716A2701412`

PDF pages: `25`

PDF size: `785264` bytes.

Artifact rule: keep the numbered PDF in Downloads only; do not copy it to the visible Desktop.
