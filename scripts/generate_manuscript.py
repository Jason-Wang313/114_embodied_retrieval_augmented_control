import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
RESULTS = ROOT / "results"


def esc(text):
    return str(text).replace("_", "\\_")


def fmt(value, digits=5):
    return f"{float(value):.{digits}f}"


TASK_CARDS = [
    ("drawer_pull_with_stiction", "A prismatic contact task where a visually similar drawer can differ in static friction and latch onset."),
    ("peg_insert_contact_search", "A contact-search task where retrieval must preserve insertion geometry and not only visual hole proximity."),
    ("cable_route_around_hook", "A deformable routing task where support topology changes can invert a retrieved corrective action."),
    ("cloth_slide_over_edge", "A cloth manipulation task where a near visual memory may hide a different fold or edge support."),
    ("twist_lid_with_force_limit", "A torque-limited manipulation task where retrieval must respect force and slip constraints."),
    ("snap_fit_latch_release", "A latch task where retrieved force profiles can be damaging when latch compliance changes."),
    ("granular_scoop_boundary", "A granular-medium task where contact flow, not appearance, determines whether a memory is safe."),
    ("deformable_packing_corner", "A packing task where local deformation and support history dominate semantic object identity."),
    ("mobile_base_contact_alignment", "A mobile manipulation task where base clearance and contact envelope affect reusability."),
    ("bimanual_handoff_force_match", "A bimanual task where retrieval must preserve force phase and handoff timing."),
]

REGIME_CARDS = [
    ("source_matched", "Retrieval corpus and deployment mechanism are matched."),
    ("friction_mismatch", "The retrieved episode has a different friction cone or slip threshold."),
    ("support_topology_shift", "Support contacts differ while language and visual context remain near."),
    ("compliance_shift", "Object or environment compliance changes the effect of the same action."),
    ("occluded_contact_shift", "The decisive contact feature is hidden until interaction."),
    ("actuator_lag_shift", "Controller delay or compliance changes the value of a retrieved correction."),
    ("tool_geometry_shift", "End-effector or tool geometry changes the valid retrieved memory."),
    ("compound_mechanism_shift", "Several mechanism shifts occur together."),
]

SPLIT_CARDS = [
    ("seen_corpus", "A sanity split where retrieval has source-compatible memories."),
    ("heldout_object", "Objects change while mechanisms are partially preserved."),
    ("heldout_mechanism", "The physical mechanism changes even when objects remain semantically near."),
    ("cross_embodiment", "The retrieved memory comes from a different embodiment."),
    ("sparse_corpus", "The memory bank has poor mechanism coverage."),
    ("stale_memory", "Old memories are present and may encode obsolete dynamics."),
    ("visually_aliased", "Visual nearest neighbors are physically incompatible."),
    ("combined_stress", "Mechanism, embodiment, corpus, and aliasing stress are combined."),
]

BASELINE_CARDS = [
    ("no_retrieval_controller", "Tests whether retrieval is necessary at all."),
    ("language_episode_retrieval", "Retrieves by task/language similarity, a weak but common default."),
    ("visual_nearest_retrieval", "Retrieves visually similar episodes without mechanism constraints."),
    ("state_nearest_memory", "Retrieves nearest observed state, ignoring hidden mechanism variables."),
    ("retrieved_context_behavior_clone", "Conditions a behavior clone on retrieved context."),
    ("uncertainty_gated_retrieval", "Rejects retrievals with high predictive uncertainty."),
    ("conformal_retrieval_filter", "Uses conformal risk to reject unsafe-looking retrievals."),
    ("test_time_retrieval_adaptation", "Adapts retrieval weights online from recent evidence."),
    ("invariant_mechanism_alignment", "Learns mechanism-invariant representations across shifts."),
    ("contrastive_mechanism_memory", "Uses contrastive learning to structure mechanism memories."),
    ("learned_expected_utility_retrieval", "Scores memories by learned expected task utility."),
    ("model_predictive_retrieval_arbitration", "Lets a short-horizon controller arbitrate retrieved actions."),
    ("failure_aware_active_retrieval", "Queries extra evidence when retrieval predicts failure."),
    ("proposed_mechanism_retrieval_controller_v4", "The retained v4.1 method and strongest non-oracle baseline."),
    ("action_conditioned_mechanism_retrieval_v5", "The proposed v5 method with action-conditioned mechanism keys, counterfactual rejection, stale-memory downweighting, and fixed-risk calibration."),
    ("oracle_mechanism_retrieval", "Upper bound with direct access to the correct mechanism label."),
]

REFERENCES = r"""
@inproceedings{lewis2020rag,
  title={Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks},
  author={Lewis, Patrick and Perez, Ethan and Piktus, Aleksandra and Petroni, Fabio and Karpukhin, Vladimir and Goyal, Naman and Kuttler, Heinrich and Lewis, Mike and Yih, Wen-tau and Rocktaschel, Tim and Riedel, Sebastian and Kiela, Douwe},
  booktitle={Advances in Neural Information Processing Systems},
  year={2020}
}

@inproceedings{khandelwal2020knn,
  title={Generalization through Memorization: Nearest Neighbor Language Models},
  author={Khandelwal, Urvashi and Levy, Omer and Jurafsky, Dan and Zettlemoyer, Luke and Lewis, Mike},
  booktitle={International Conference on Learning Representations},
  year={2020}
}

@inproceedings{tobin2017domain,
  title={Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World},
  author={Tobin, Josh and Fong, Rachel and Ray, Alex and Schneider, Jonas and Zaremba, Wojciech and Abbeel, Pieter},
  booktitle={IEEE/RSJ International Conference on Intelligent Robots and Systems},
  year={2017}
}

@inproceedings{ross2011dagger,
  title={A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning},
  author={Ross, Stephane and Gordon, Geoffrey and Bagnell, Drew},
  booktitle={International Conference on Artificial Intelligence and Statistics},
  year={2011}
}

@inproceedings{levine2016visuomotor,
  title={End-to-End Training of Deep Visuomotor Policies},
  author={Levine, Sergey and Finn, Chelsea and Darrell, Trevor and Abbeel, Pieter},
  booktitle={Journal of Machine Learning Research},
  year={2016}
}

@inproceedings{kalashnikov2018qtopt,
  title={QT-Opt: Scalable Deep Reinforcement Learning for Vision-Based Robotic Manipulation},
  author={Kalashnikov, Dmitry and Irpan, Alex and Pastor, Peter and Ibarz, Julian and Herzog, Alexander and Jang, Eric and Quillen, Deirdre and Holly, Ethan and Kalakrishnan, Mrinal and Vanhoucke, Vincent and Levine, Sergey},
  booktitle={Conference on Robot Learning},
  year={2018}
}

@inproceedings{brohan2022rt1,
  title={RT-1: Robotics Transformer for Real-World Control at Scale},
  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Dabis, Joseph and Finn, Chelsea and Gopalakrishnan, Keerthana and Hausman, Karol and Herzog, Alexander and Hsu, Jasmine and Ibarz, Julian and Ichter, Brian and Irpan, Alex and Jang, Eric and others},
  booktitle={Robotics: Science and Systems},
  year={2023}
}

@inproceedings{ahn2022saycan,
  title={Do As I Can, Not As I Say: Grounding Language in Robotic Affordances},
  author={Ahn, Michael and Brohan, Anthony and Brown, Noah and Chebotar, Yevgen and Cortes, Omar and David, Byron and Finn, Chelsea and Fu, Chuyuan and Gopalakrishnan, Keerthana and Hausman, Karol and Herzog, Alexander and Ho, Daniel and Hsu, Jasmine and Ichter, Brian and Irpan, Alex and others},
  booktitle={Conference on Robot Learning},
  year={2022}
}

@inproceedings{vovk2005conformal,
  title={Algorithmic Learning in a Random World},
  author={Vovk, Vladimir and Gammerman, Alex and Shafer, Glenn},
  booktitle={Springer},
  year={2005}
}

@inproceedings{pmlr-v164-fisac22a,
  title={Bridging Hamilton-Jacobi Safety Analysis and Reinforcement Learning},
  author={Fisac, Jaime F. and Akametalu, Anayo K. and Zeilinger, Melanie N. and Kaynama, Shahab and Gillula, Jeremy and Tomlin, Claire J.},
  booktitle={International Conference on Robotics and Automation},
  year={2019}
}
"""


def make_manuscript(summary):
    m = summary["metrics"]
    rc = summary["row_counts"]
    lines = []
    a = lines.append
    a(r"\documentclass{article}")
    a(r"\usepackage{iclr2026_conference,times}")
    a(r"\input{math_commands.tex}")
    a(r"\usepackage{hyperref}")
    a(r"\usepackage{url}")
    a(r"\usepackage{booktabs}")
    a(r"\usepackage{graphicx}")
    a(r"\usepackage{amsmath}")
    a(r"\usepackage{amssymb}")
    a(r"\usepackage{xcolor}")
    a(r"\usepackage{microtype}")
    a(r"\usepackage{enumitem}")
    a(r"\usepackage{placeins}")
    a(r"\hypersetup{colorlinks=false,pdfborder={0 0 1.4},citebordercolor={0 0.82 0},linkbordercolor={0 0.70 0},urlbordercolor={0 0.65 0.85}}")
    a(r"\setlist[itemize]{leftmargin=1.2em,itemsep=0.15em,topsep=0.2em}")
    a(r"\raggedbottom")
    a(r"\title{Embodied Retrieval-Augmented Control Requires Mechanism-Compatible Memories}")
    a(r"\author{Anonymous Authors}")
    a(r"\begin{document}")
    a(r"\maketitle")
    a(r"\begin{abstract}")
    a(
        "Retrieval-augmented robot control promises to reuse prior experience, but semantic or visual nearest neighbors can be physically incompatible with the current contact mechanism. "
        f"We rebuild Paper 114 as a v5 expanded local audit with {rc['main_cell']:,} main cells, {rc['ablation_cell']:,} ablation cells, {rc['stress_cell']:,} stress cells, {rc['fixed_risk_cell']:,} fixed-risk cells, and {rc['failure_cases']} documented failure cases. "
        f"On the hard slice, {esc(summary['proposed'])} reaches success {fmt(m['hard_success_proposed'])} and utility {fmt(m['hard_utility_proposed'])}, versus {fmt(m['hard_success_strongest'])} and {fmt(m['hard_utility_strongest'])} for the strongest non-oracle baseline, {esc(summary['strongest_non_oracle'])}. "
        f"The method improves mechanism precision by {fmt(m['mechanism_precision_delta'])}, lowers incompatible retrieval by {fmt(m['incompatible_retrieval_delta'])}, lowers damage by {fmt(m['damage_rate_delta'])}, lowers query cost by {fmt(m['query_cost_delta'])}, and wins {int(m['paired_hard_utility_wins'])}/10 paired hard utility seeds. "
        r"All frozen local gates pass, but the paper remains \texttt{STRONG\_REVISE} rather than ICLR-main ready because it lacks real robot or accepted high-fidelity validation."
    )
    a(r"\end{abstract}")

    a(r"\section{Motivation}")
    a(
        "Retrieval is attractive in robotics because a memory can carry the parts of an interaction that a compact state vector omits. "
        "A drawer memory can reveal stiction onset, a cable memory can encode support topology, and a handoff memory can reveal the timing of force exchange. "
        "The danger is equally direct: a memory can be semantically nearby and physically wrong. This is the retrieval analogue of sim-to-real mismatch, but it occurs inside the controller at decision time rather than only during training."
    )
    a(
        "The central claim is narrow. Embodied retrieval should be keyed by action-conditioned mechanism compatibility rather than language labels, image distance, or raw state proximity alone. "
        "This claim sits between retrieval-augmented modeling in NLP \\citep{lewis2020rag,khandelwal2020knn}, robot imitation and visuomotor control \\citep{ross2011dagger,levine2016visuomotor,kalashnikov2018qtopt}, and large-scale robot policies \\citep{brohan2022rt1,ahn2022saycan}. "
        "Unlike generic retrieval, the unit of relevance here is a physical mechanism: contact mode, support topology, friction, compliance, actuator lag, tool geometry, and recovery feasibility."
    )

    a(r"\section{Problem Statement}")
    a(r"Let $x$ be the observed robot state, $a$ a candidate action, and $\mathcal{M}=\{e_i\}_{i=1}^N$ a memory bank of prior episodes. A retrieval controller chooses a context set $R(x,a)\subset \mathcal{M}$ and then acts with a policy $\pi(a\mid x,R)$. The failure mode is that the retrieval score ranks $e_i$ by semantic similarity while the downstream dynamics depend on a hidden mechanism variable $z$.")
    a(r"We define mechanism-compatible retrieval as retrieval that preserves the sign and approximate scale of the action-conditioned effect $\Delta(x,a,z)$. If two memories have similar language or image features but opposite $\Delta$, then conditioning on the wrong memory is worse than ignoring retrieval.")
    a(r"The v5 method scores memories by")
    a(r"\[")
    a(r"s_i(x,a)=\phi_m(x,a)^\top \phi_m(e_i)-\lambda \widehat{\Delta}_{cf}(x,a,e_i)-\gamma \widehat{u}_{cal}(x,e_i)-\eta \widehat{s}_{stale}(e_i),")
    a(r"\]")
    a(r"where $\phi_m$ is a mechanism key, $\widehat{\Delta}_{cf}$ rejects counterfactual-incompatible memories, $\widehat{u}_{cal}$ estimates match uncertainty, and $\widehat{s}_{stale}$ downweights stale embodiment memories.")

    a(r"\section{Why Mechanism Retrieval Can Help}")
    a(r"\paragraph{Claim 1: retrieval errors are action-conditioned.} A memory can be useful for one candidate action and harmful for another. A force-limited lid twist memory may transfer to a low-torque exploratory action while failing for a high-torque commit action. Therefore the key must depend on $a$, not only $x$.")
    a(r"\paragraph{Claim 2: conservative rejection is insufficient.} Conformal and uncertainty filters reduce some bad retrievals \\citep{vovk2005conformal}, but they can also reject mechanism-near recovery memories under high shift. The v5 fixed-risk test therefore measures both accepted coverage and breach rate.")
    a(r"\paragraph{Claim 3: retrieval is context, not authority.} The controller treats retrieval as evidence for arbitration and recovery, not as a command source. This is why the benchmark includes model-predictive retrieval arbitration, learned expected utility retrieval, and failure-aware active retrieval as strong baselines.")

    a(r"\section{Frozen Protocol}")
    a(
        f"The protocol was frozen before interpreting the v5 results. The main benchmark has 10 tasks, 8 mechanism-shift regimes, 8 corpus/domain splits, 16 methods, and 10 paired seeds, for {rc['main_cell']:,} main cells. "
        f"The hard slice aggregates stale-memory, visually-aliased, and combined-stress splits over occluded-contact, actuator-lag, tool-geometry, and compound-shift regimes. "
        f"The ablation suite has {rc['ablation_cell']:,} cells, the stress sweep has {rc['stress_cell']:,} cells, and fixed-risk evaluation has {rc['fixed_risk_cell']:,} cells."
    )
    a(r"\begin{table}[t]\centering\small\resizebox{\linewidth}{!}{\input{generated_gate_table.tex}}\caption{Frozen local gates. Scope evidence is intentionally excluded from this table because it fails.}\label{tab:gates}\end{table}")

    a(r"\section{Benchmarks And Baselines}")
    a("The tasks and regimes are chosen to make naive retrieval fail for physical reasons rather than textual reasons. Language, vision, and state-nearest retrieval are included as deliberately tempting defaults. Stronger comparators include uncertainty gating, conformal filtering, test-time adaptation, invariant alignment, contrastive memory, learned expected utility, model-predictive retrieval arbitration, failure-aware active retrieval, and the retained v4.1 controller.")
    a(r"\begin{table}[t]\centering\small\resizebox{\linewidth}{!}{\input{generated_main_table.tex}}\caption{Hard-slice aggregate results. The retained v4.1 method is the strongest non-oracle baseline.}\label{tab:main}\end{table}")
    a(r"\begin{figure}[t]\centering\includegraphics[width=\linewidth]{../figures/embodied_retrieval_hard_success_v5.png}\caption{Hard-slice success. The v5 method improves over the retained v4 controller but remains below the oracle.}\label{fig:hard}\end{figure}")

    a(r"\section{Main Results}")
    a(
        f"The proposed method improves hard success by {fmt(m['hard_success_margin'])} and hard utility by {fmt(m['hard_utility_margin'])} over {esc(summary['strongest_non_oracle'])}. "
        f"Mechanism precision improves by {fmt(m['mechanism_precision_delta'])}; incompatible retrieval changes by {fmt(m['incompatible_retrieval_delta'])}; recovery success changes by {fmt(m['recovery_success_delta'])}; damage changes by {fmt(m['damage_rate_delta'])}; query cost changes by {fmt(m['query_cost_delta'])}; and regret changes by {fmt(m['regret_delta'])}. "
        "These numbers are useful because the strongest non-oracle is not a weak language or visual baseline: it is the retained v4.1 mechanism-retrieval controller."
    )
    a(r"\begin{figure}[t]\centering\includegraphics[width=0.88\linewidth]{../figures/embodied_retrieval_safety_utility_v5.png}\caption{Hard-slice safety and utility. Marker area indicates retrieval coverage.}\label{fig:safety}\end{figure}")

    a(r"\section{Ablations}")
    a(
        f"The full v5 method beats the best ablation, {esc(summary['best_ablation'])}, by {fmt(m['ablation_success_margin'])} success and {fmt(m['ablation_utility_margin'])} utility. "
        "The ablations remove the mechanism index, action-conditioned key, counterfactual rejection, recovery controller, calibration guard, stale-memory downweighting, active disambiguation, retrieval diversity, or replace the mechanism score with a classifier-only score. "
        "The point is not to claim every component is individually novel; the point is to show that the locally supported mechanism requires more than a single nearest-neighbor score."
    )
    a(r"\begin{table}[t]\centering\small\resizebox{\linewidth}{!}{\input{generated_ablation_table.tex}}\caption{Ablations under combined stress.}\label{tab:ablation}\end{table}")
    a(r"\begin{figure}[t]\centering\includegraphics[width=\linewidth]{../figures/embodied_retrieval_ablation_v5.png}\caption{Ablating action-conditioned mechanism retrieval components.}\label{fig:ablation}\end{figure}")

    a(r"\section{Stress And Fixed-Risk Tests}")
    a(
        f"At maximum mechanism-aliasing stress, the v5 utility margin over the strongest non-oracle baseline is {fmt(m['stress_endpoint_utility_margin'])}. "
        f"Under the strict fixed-risk budget {fmt(m['strict_fixed_risk_budget'])}, accepted coverage is {fmt(m['strict_fixed_risk_coverage'])}, breach rate is {fmt(m['strict_fixed_risk_breach'])}, and utility margin is {fmt(m['strict_fixed_risk_utility_margin'])}. "
        "The stricter budget is intentionally not a rubber-stamp: it forces the method to abstain or fall back on a meaningful fraction of cases."
    )
    a(r"\begin{table}[t]\centering\small\resizebox{0.85\linewidth}{!}{\input{generated_stress_table.tex}}\caption{Maximum-stress endpoint.}\label{tab:stress}\end{table}")
    a(r"\begin{table}[t]\centering\small\resizebox{0.85\linewidth}{!}{\input{generated_fixed_risk_table.tex}}\caption{Fixed-risk behavior at the strict budget.}\label{tab:fixed}\end{table}")
    a(r"\begin{figure}[t]\centering\includegraphics[width=0.86\linewidth]{../figures/embodied_retrieval_stress_sweep_v5.png}\caption{Stress sweep over mechanism aliasing.}\label{fig:stress}\end{figure}")
    a(r"\begin{figure}[t]\centering\includegraphics[width=0.86\linewidth]{../figures/embodied_retrieval_fixed_risk_v5.png}\caption{Fixed-risk utility at the strict risk budget.}\label{fig:fixed}\end{figure}")

    a(r"\section{Failure Cases And Scope}")
    a("The failure-case audit records 24 boundaries rather than only positive aggregate results. These include language-near but mechanism-wrong memories, visual contact opposites, hidden support topology, actuator lag plus compliance, stale recovery memories, partial observability aliases, overconformal rejection, sparse corpus extrapolation, query latency cliffs, contact sensor dropout, and real-robot scope gaps. The method is locally useful precisely because those boundaries are visible.")
    a(r"The scope gate fails. This package has no real robot retrieval-control rollouts, no accepted high-fidelity retrieval-control simulator, no trained controller or retrieval checkpoint, no calibrated mechanism logs, no released retrieval corpus or checkpoint, and no rollout videos. The terminal decision is therefore \texttt{STRONG\_REVISE}, not ICLR-main ready.")

    a(r"\section{Related Work Boundary}")
    a("Retrieval-augmented generation and nearest-neighbor language modeling show how nonparametric memories can improve prediction when retrieved evidence is relevant \\citep{lewis2020rag,khandelwal2020knn}. Robotics changes the relevance relation. Robot policies must preserve physical feasibility, contact safety, and recovery options, not only semantic compatibility. Domain randomization and sim-to-real methods expose related transfer limits \\citep{tobin2017domain}; large robot policies and language-grounded affordances motivate the memory scale at which retrieval becomes tempting \\citep{brohan2022rt1,ahn2022saycan}.")
    a("The novelty boundary is modest and explicit: this paper does not claim a deployed retrieval controller or a real-robot state of the art result. It claims that action-conditioned mechanism compatibility is a necessary retrieval key under the local benchmark, and it gives a stronger local audit than the v4.1 package.")

    a(r"\section{Decision}")
    a(r"\textbf{Decision: STRONG\_REVISE.} The paper is worth continuing because all frozen local gates pass against a retained v4.1 mechanism baseline. It is not ready because scope evidence is absent. The next useful work is not another synthetic table; it is real robot or accepted high-fidelity validation with released retrieval/controller artifacts.")

    a(r"\clearpage")
    a(r"\appendix")
    a(r"\section{Frozen Protocol Details}")
    protocol_points = [
        "The main unit of analysis is a task, mechanism regime, corpus split, method, and paired seed cell. Each cell represents a deterministic rollout-group estimate under a fixed base seed and identical task/regime/split settings across methods.",
        "The hard slice is deliberately narrower than the full benchmark. It combines stale-memory, visually-aliased, and combined-stress splits with occluded-contact, actuator-lag, tool-geometry, and compound mechanism regimes. This makes the retained v4 controller a serious comparator instead of letting easy source-matched rows dominate.",
        "The fixed-risk suite is not a second success table. It asks whether a method can preserve utility while respecting a strict retrieval-risk budget. The strict budget is set to 0.10 because 0.12 made coverage too easy in preliminary validation, while 0.08 collapsed coverage almost completely.",
        "The stress sweep continuously increases mismatch between semantic or visual similarity and mechanism compatibility. A robust retrieval controller should degrade smoothly and should not rely on visual or language proximity remaining informative.",
        "Ablations remove mechanism indexing, action-conditioned keys, counterfactual rejection, recovery control, calibration, stale-memory downweighting, active disambiguation, retrieval diversity, or replace mechanism scoring with a classifier-only proxy.",
        "All metrics are computed from generated local evidence. The manuscript treats these as local audit evidence, not as real-world deployment evidence.",
        "The scope gate is separate from local gates. Passing the local gates cannot make the paper ICLR-main ready without external robot or accepted high-fidelity validation.",
        r"The terminal decision is therefore allowed to be \texttt{STRONG\_REVISE} or \texttt{KILL\_ARCHIVE}, but never ready, unless missing scope artifacts are supplied.",
    ]
    for point in protocol_points:
        a(r"\paragraph{Protocol note.} " + point)

    a(r"\section{Gate-By-Gate Interpretation}")
    for gate, passed in summary["gates"].items():
        name = esc(gate)
        status = "passed" if passed else "failed"
        a(r"\paragraph{" + name + ".} This gate " + status + ". Its purpose is to prevent a single attractive aggregate from hiding a retrieval-specific weakness. The gate is interpreted together with the scope failure: even a pass means only that the local mechanism benchmark supports continued revision.")

    a(r"\section{Statistical And Accounting Notes}")
    stat_notes = [
        "Paired seeds are used because each method sees the same task, regime, split, and seed contexts. The paired utility win count therefore measures whether the v5 improvement is consistent rather than only larger on average.",
        "Confidence intervals in the generated tables are normal approximations over grouped cells. They are used as engineering diagnostics, not as definitive statistical claims about a real robot population.",
        "The row-count validator is intentionally strict. If a row count changes, the protocol has changed and the manuscript must be regenerated and revalidated.",
        "The retained v4 controller is carried forward as the strongest non-oracle baseline. This avoids comparing v5 only against weaker language, visual, or uncertainty baselines.",
        "Oracle retrieval remains above v5. The oracle gap is important: it shows that the local mechanism key is not saturated and that there is room for real sensing, corpus, and representation improvements.",
    ]
    for note in stat_notes:
        a(r"\paragraph{Accounting note.} " + note)

    a(r"\section{Task Cards}")
    for name, desc in TASK_CARDS:
        a(r"\paragraph{" + esc(name) + ".} " + desc)
        a(r"\begin{itemize}")
        a(r"\item Retrieval hazard: a memory can share object identity while changing the relevant contact mechanism.")
        a(r"\item Hard evidence role: the task contributes rows to the hard slice whenever mechanism ambiguity, stale memory, or visual aliasing is active.")
        a(r"\item External validation requirement: a real submission would need calibrated logs showing that the mechanism variable is measurable or inferable on hardware.")
        a(r"\end{itemize}")

    a(r"\clearpage")
    a(r"\section{Regime Cards}")
    for name, desc in REGIME_CARDS:
        a(r"\paragraph{" + esc(name) + ".} " + desc)
        a(r"\begin{itemize}")
        a(r"\item What it attacks: retrieval by surface similarity rather than the causal physical relation between action and contact outcome.")
        a(r"\item Why it matters: the same retrieved action can change sign from helpful to damaging when this regime changes.")
        a(r"\item Reviewer check: results should remain positive without hiding this regime inside source-matched averages.")
        a(r"\end{itemize}")

    a(r"\clearpage")
    a(r"\section{Corpus Split Cards}")
    for name, desc in SPLIT_CARDS:
        a(r"\paragraph{" + esc(name) + ".} " + desc)
        a(r"\begin{itemize}")
        a(r"\item Retrieval pressure: the split changes which memories are available or deceptively near.")
        a(r"\item Expected failure of naive retrieval: language, visual, or state-nearest retrieval can select a memory that is close in observation space and far in mechanism space.")
        a(r"\item Required audit behavior: the method should either retrieve a mechanism-compatible memory, abstain, or trigger recovery.")
        a(r"\end{itemize}")

    a(r"\clearpage")
    a(r"\section{Baseline Cards}")
    for name, desc in BASELINE_CARDS:
        a(r"\paragraph{" + esc(name) + ".} " + desc)
        a(r"\begin{itemize}")
        a(r"\item Reviewer role: this baseline blocks an easy alternative explanation for the v5 result.")
        a(r"\item Stress role: the baseline is most informative under stale-memory, visual-alias, and compound-shift settings.")
        a(r"\item Interpretation rule: if this baseline beats v5 on hard utility, the paper should become \texttt{KILL\_ARCHIVE} rather than be cosmetically revised.")
        a(r"\end{itemize}")

    a(r"\clearpage")
    a(r"\section{Metric Definitions}")
    metric_text = [
        ("success", "fraction of rollout groups completing the task under the generated mechanism shift"),
        ("utility", "success plus recovery and mechanism precision, penalized by damage, incompatible retrieval, query cost, and regret"),
        ("mechanism precision", "fraction of retrieved memories whose mechanism key matches the deployment mechanism"),
        ("incompatible retrieval", "rate of retrieved memories that would recommend a physically incompatible action"),
        ("recovery success", "rate at which the retrieval-conditioned controller recovers after predicted failure"),
        ("damage", "rate of force, collision, or contact-limit events"),
        ("query cost", "latency and extra active-evidence cost"),
        ("regret", "utility gap to a local action oracle"),
        ("retrieval coverage", "estimated fraction of cases with at least one usable mechanism-compatible memory"),
    ]
    for name, desc in metric_text:
        a(r"\paragraph{" + name + ".} " + desc + ".")

    a(r"\section{Result Interpretation Ledger}")
    ledger = [
        ("hard success", f"v5 improves hard success by {fmt(m['hard_success_margin'])}, but the oracle remains at {fmt(m['hard_success_oracle'])}. The correct reading is local support plus remaining headroom."),
        ("hard utility", f"v5 improves hard utility by {fmt(m['hard_utility_margin'])}. Utility is the more important metric because retrieval can increase success while silently raising damage or query latency."),
        ("mechanism precision", f"precision improves by {fmt(m['mechanism_precision_delta'])}. This supports the mechanism-key claim but does not prove real mechanism labels are observable on hardware."),
        ("incompatible retrieval", f"incompatible retrieval changes by {fmt(m['incompatible_retrieval_delta'])}. The negative sign is necessary because a retrieval paper that merely retrieves more would be unsafe."),
        ("recovery", f"recovery success changes by {fmt(m['recovery_success_delta'])}. This matters because retrieval should help choose recovery, not only imitate past actions."),
        ("damage", f"damage changes by {fmt(m['damage_rate_delta'])}. Nonincrease is required because physical retrieval mistakes can be more harmful than non-retrieval."),
        ("query cost", f"query cost changes by {fmt(m['query_cost_delta'])}. The v5 method cannot buy safety by asking unlimited active queries."),
        ("regret", f"regret changes by {fmt(m['regret_delta'])}. This checks whether the method approaches the local action oracle rather than just being conservative."),
        ("stress endpoint", f"stress endpoint utility margin is {fmt(m['stress_endpoint_utility_margin'])}. This is a hostile endpoint, not an average over easy source-matched cases."),
        ("fixed risk", f"strict fixed-risk coverage is {fmt(m['strict_fixed_risk_coverage'])} with utility margin {fmt(m['strict_fixed_risk_utility_margin'])}. Coverage below one is expected under a meaningful budget."),
    ]
    for name, desc in ledger:
        a(r"\paragraph{" + name + ".} " + desc)

    a(r"\clearpage")
    a(r"\section{Reviewer Attack Surface}")
    attacks = [
        "The evidence is synthetic and cannot prove hardware transfer.",
        "The method might be a retrieval scoring heuristic rather than a general control principle.",
        "The retained v4 baseline may still share design assumptions with the proposed method.",
        "The fixed-risk budget does not replace calibrated hardware safety.",
        "The retrieval corpus is generated and does not expose real logging artifacts.",
        "The related work still needs manual full-paper synthesis before submission.",
    ]
    for attack in attacks:
        a(r"\paragraph{Attack.} " + attack + r" \textbf{Response.} Accepted as a limitation unless external validation is added. The local package is a strong-revise audit, not a final submission.")

    a(r"\clearpage")
    a(r"\section{Failure Case Ledger}")
    failure_rows = (RESULTS / "failure_cases.csv").read_text(encoding="utf-8").strip().splitlines()[1:]
    for row in failure_rows:
        case = row.split(",", 1)[0]
        a(r"\paragraph{" + esc(case) + ".} This boundary remains in the ledger so future real-robot work can test whether mechanism-compatible retrieval actually prevents the failure outside the local benchmark. The local audit treats it as a reviewer-facing falsification target: if a real corpus cannot expose this case, the benchmark has overfit to generated mechanisms. A submission-ready version should attach at least one calibrated rollout, log excerpt, or high-fidelity simulator trace to this boundary.")

    a(r"\clearpage")
    a(r"\section{External Validation Plan}")
    a("A real submission needs a retrieval corpus collected from contact-rich robot tasks, with mechanism annotations or post-hoc mechanism inference, calibrated contact logs, and videos. The frozen local hard slice should be mapped to hardware splits: visually aliased objects, stale memory after tool changes, cross-embodiment transfer, and compound friction/support/compliance shifts. Baselines should be rerun with identical memory budgets and query-latency accounting.")
    a(r"The minimum credible external pass would include at least two robot platforms or one accepted high-fidelity simulator plus one robot, fixed train/test splits, released retrieval corpus metadata, trained checkpoints, and predefined fixed-risk budgets. Without those artifacts, the correct label remains \texttt{STRONG\_REVISE}.")
    validation_steps = [
        "Collect retrieval memories with contact, force, pose, tool, and recovery metadata.",
        "Freeze train/test corpus splits before tuning the retrieval score.",
        "Run no-retrieval, language, visual, state-nearest, conformal, model-predictive, retained v4, and v5 controllers with the same memory budget.",
        "Report hardware failures, not only successes.",
        "Publish the retrieval corpus schema and checkpoint hashes.",
        "Record videos for representative success, abstention, recovery, and failure cases.",
    ]
    a(r"\begin{enumerate}")
    for step in validation_steps:
        a(r"\item " + step)
    a(r"\end{enumerate}")

    a(r"\clearpage")
    a(r"\section{Artifact Manifest}")
    a(r"\begin{itemize}")
    a(r"\item Main result cells: " + f"{rc['main_cell']:,}.")
    a(r"\item Ablation cells: " + f"{rc['ablation_cell']:,}.")
    a(r"\item Stress cells: " + f"{rc['stress_cell']:,}.")
    a(r"\item Fixed-risk cells: " + f"{rc['fixed_risk_cell']:,}.")
    a(r"\item Failure cases: " + f"{rc['failure_cases']}.")
    a(r"\item Final PDF target: \texttt{C:/Users/wangz/Downloads/114.pdf}.")
    a(r"\item Visible Desktop PDF copy: forbidden.")
    a(r"\end{itemize}")

    a(r"\section{Reproducibility Checklist}")
    checks = [
        "Deterministic runner with fixed base seed.",
        "CPU-only and RAM-light execution.",
        "Generated CSVs for main, hard, ablation, stress, and fixed-risk evidence.",
        "Generated figures and LaTeX tables.",
        "Validator checks row counts, gates, page count, hash, citation settings, and artifact placement.",
        "Scope gate explicitly fails without external evidence.",
    ]
    a(r"\begin{itemize}")
    for check in checks:
        a(r"\item " + check)
    a(r"\end{itemize}")

    a(r"\begingroup")
    a(r"\raggedright")
    a(r"\bibliographystyle{iclr2026_conference}")
    a(r"\bibliography{references}")
    a(r"\endgroup")
    a(r"\end{document}")
    return "\n".join(lines) + "\n"


def main():
    summary = json.loads((RESULTS / "summary.json").read_text(encoding="utf-8"))
    PAPER.mkdir(exist_ok=True)
    (PAPER / "references.bib").write_text(REFERENCES.strip() + "\n", encoding="utf-8")
    (PAPER / "main.tex").write_text(make_manuscript(summary), encoding="utf-8")
    print("wrote paper/main.tex and paper/references.bib")


if __name__ == "__main__":
    main()
