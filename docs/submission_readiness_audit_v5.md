# Submission Readiness Audit v5

Paper: 114 embodied_retrieval_augmented_control

Version: v5_expanded

Decision: STRONG_REVISE

ICLR main ready: NO

## What Improved

- Expanded the manuscript to 25 pages with method theory, frozen protocol, stress tests, fixed-risk analysis, failure cases, reviewer attack surface, and reproducibility details.
- Increased the experiment to 10 tasks, 8 mechanism-shift regimes, 8 corpus/domain splits, 16 methods, and 10 paired seeds.
- Added fixed-risk evaluation to test whether retrieval remains useful under an explicit risk budget.
- Retained the v4.1 mechanism-retrieval controller as the strongest non-oracle baseline.
- Added bright boxed clickable citations and PDF artifact validation.

## What The Evidence Supports

- The proposed v5 method is better than the retained v4 controller on the predefined local hard slice.
- The method improves hard success and hard utility while improving mechanism precision and reducing incompatible retrieval, damage, query cost, and regret.
- The method survives ablations, stress endpoint checks, and fixed-risk evaluation under the frozen local benchmark.

## What The Evidence Does Not Support

- It does not establish real-robot retrieval-control transfer.
- It does not establish superiority on accepted external retrieval-control benchmarks.
- It does not validate hardware safety under calibrated mechanism logs.
- It does not release trained retrieval/controller checkpoints, corpora, or videos.

## Terminal Recommendation

Keep the paper and revise aggressively. The next quality leap must come from real robot or accepted high-fidelity retrieval-control validation, not more local synthetic expansion.
