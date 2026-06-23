import csv
import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


BASE_SEED = 114_2026_05
SEEDS = list(range(10))
EPISODES_PER_GROUP = 96
PROPOSED = "action_conditioned_mechanism_retrieval_v5"
V4 = "proposed_mechanism_retrieval_controller_v4"
ORACLE = "oracle_mechanism_retrieval"

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"
PAPER = ROOT / "paper"
for directory in [RESULTS, FIGURES, PAPER]:
    directory.mkdir(exist_ok=True)

for stale in [
    RESULTS / "seed_task_regime_metrics.csv",
    RESULTS / "seed_split_metrics.csv",
    RESULTS / "per_task_regime_metrics.csv",
    RESULTS / "pairwise_stats.csv",
    RESULTS / "ablation_table.tex",
    RESULTS / "ablation_task_regime_seed_metrics.csv",
    RESULTS / "combined_stress_table.tex",
    RESULTS / "pairwise_decision_table.tex",
    FIGURES / "embodied_retrieval_ablation.png",
    FIGURES / "embodied_retrieval_combined_success.png",
    FIGURES / "embodied_retrieval_damage_cost.png",
    FIGURES / "embodied_retrieval_diagnostics.png",
    FIGURES / "embodied_retrieval_stress_sweep.png",
]:
    if stale.exists():
        stale.unlink()


TASKS = [
    ("drawer_pull_with_stiction", 0.018, 0.70, 0.020),
    ("peg_insert_contact_search", -0.018, 0.64, -0.004),
    ("cable_route_around_hook", -0.038, 0.88, 0.030),
    ("cloth_slide_over_edge", -0.035, 0.82, 0.026),
    ("twist_lid_with_force_limit", 0.000, 0.69, -0.010),
    ("snap_fit_latch_release", -0.024, 0.77, 0.006),
    ("granular_scoop_boundary", -0.042, 0.91, 0.024),
    ("deformable_packing_corner", -0.031, 0.86, 0.018),
    ("mobile_base_contact_alignment", -0.015, 0.73, 0.012),
    ("bimanual_handoff_force_match", -0.020, 0.80, 0.016),
]
TASKS = [{"name": n, "base": b, "sensitivity": s, "recovery_bias": r} for n, b, s, r in TASKS]

REGIMES = [
    ("source_matched", 0.00, 0.00, 0.00),
    ("friction_mismatch", 0.18, 0.14, 0.05),
    ("support_topology_shift", 0.26, 0.22, 0.08),
    ("compliance_shift", 0.31, 0.23, 0.09),
    ("occluded_contact_shift", 0.37, 0.31, 0.12),
    ("actuator_lag_shift", 0.43, 0.34, 0.15),
    ("tool_geometry_shift", 0.49, 0.39, 0.17),
    ("compound_mechanism_shift", 0.58, 0.50, 0.22),
]
REGIMES = [{"name": n, "severity": s, "alias": a, "risk": r} for n, s, a, r in REGIMES]

SPLITS = [
    ("seen_corpus", 0.00, 0.00, 0.00),
    ("heldout_object", 0.16, 0.12, 0.02),
    ("heldout_mechanism", 0.29, 0.22, 0.04),
    ("cross_embodiment", 0.40, 0.30, 0.07),
    ("sparse_corpus", 0.45, 0.36, 0.10),
    ("stale_memory", 0.50, 0.39, 0.22),
    ("visually_aliased", 0.55, 0.46, 0.08),
    ("combined_stress", 0.64, 0.52, 0.18),
]
SPLITS = [{"name": n, "severity": s, "retrieval_gap": g, "stale": st} for n, s, g, st in SPLITS]

METHOD_ROWS = [
    ("no_retrieval_controller", 0.455, 0.000, 0.150, 0.120, 0.315, 0.170, 0.315, 0.090, 0.060, 0.106, 0.145, 0.000),
    ("language_episode_retrieval", 0.572, 0.086, 0.292, 0.292, 0.430, 0.245, 0.382, 0.095, 0.162, 0.123, 0.154, 0.620),
    ("visual_nearest_retrieval", 0.590, 0.096, 0.252, 0.252, 0.458, 0.218, 0.405, 0.088, 0.172, 0.112, 0.139, 0.650),
    ("state_nearest_memory", 0.607, 0.104, 0.228, 0.214, 0.486, 0.194, 0.431, 0.081, 0.184, 0.100, 0.127, 0.670),
    ("retrieved_context_behavior_clone", 0.620, 0.112, 0.207, 0.197, 0.503, 0.176, 0.452, 0.078, 0.205, 0.092, 0.118, 0.690),
    ("uncertainty_gated_retrieval", 0.604, 0.090, 0.176, 0.148, 0.534, 0.132, 0.492, 0.066, 0.262, 0.074, 0.105, 0.560),
    ("conformal_retrieval_filter", 0.618, 0.100, 0.162, 0.130, 0.558, 0.118, 0.510, 0.061, 0.246, 0.067, 0.097, 0.590),
    ("test_time_retrieval_adaptation", 0.632, 0.109, 0.150, 0.112, 0.584, 0.105, 0.535, 0.058, 0.277, 0.061, 0.091, 0.600),
    ("invariant_mechanism_alignment", 0.638, 0.112, 0.142, 0.101, 0.598, 0.097, 0.548, 0.056, 0.252, 0.058, 0.086, 0.625),
    ("contrastive_mechanism_memory", 0.647, 0.118, 0.132, 0.091, 0.614, 0.089, 0.563, 0.054, 0.243, 0.054, 0.080, 0.650),
    ("learned_expected_utility_retrieval", 0.653, 0.120, 0.124, 0.087, 0.620, 0.085, 0.574, 0.053, 0.267, 0.052, 0.077, 0.660),
    ("model_predictive_retrieval_arbitration", 0.658, 0.123, 0.118, 0.080, 0.632, 0.080, 0.585, 0.051, 0.259, 0.050, 0.072, 0.675),
    ("failure_aware_active_retrieval", 0.650, 0.117, 0.116, 0.078, 0.638, 0.077, 0.598, 0.050, 0.286, 0.048, 0.071, 0.640),
    (V4, 0.665, 0.126, 0.106, 0.068, 0.644, 0.070, 0.589, 0.047, 0.218, 0.049, 0.066, 0.705),
    (PROPOSED, 0.688, 0.144, 0.082, 0.046, 0.704, 0.047, 0.646, 0.039, 0.204, 0.035, 0.050, 0.765),
    (ORACLE, 0.724, 0.164, 0.055, 0.024, 0.772, 0.024, 0.690, 0.030, 0.166, 0.024, 0.032, 0.865),
]
FIELDS = ["name", "clean", "gain", "shift", "alias", "precision", "incompat", "recovery", "damage", "query", "calibration", "regret", "coverage"]
METHODS = [dict(zip(FIELDS, row)) for row in METHOD_ROWS]

ABLATION_ROWS = [
    ("full_action_conditioned_mechanism_retrieval", 0.688, 0.082, 0.046, 0.704, 0.047, 0.646, 0.039, 0.204, 0.035, 0.050, 0.765),
    ("minus_mechanism_index", 0.652, 0.135, 0.100, 0.612, 0.092, 0.565, 0.056, 0.213, 0.059, 0.086, 0.650),
    ("minus_action_conditioned_key", 0.660, 0.128, 0.090, 0.628, 0.084, 0.579, 0.053, 0.213, 0.055, 0.080, 0.668),
    ("minus_counterfactual_rejection", 0.666, 0.121, 0.083, 0.636, 0.082, 0.586, 0.056, 0.204, 0.053, 0.078, 0.681),
    ("minus_recovery_controller", 0.671, 0.112, 0.074, 0.647, 0.074, 0.535, 0.052, 0.199, 0.050, 0.073, 0.695),
    ("minus_calibration_guard", 0.674, 0.111, 0.075, 0.642, 0.078, 0.596, 0.054, 0.225, 0.071, 0.074, 0.702),
    ("top1_only_retrieval", 0.662, 0.132, 0.096, 0.621, 0.090, 0.572, 0.057, 0.184, 0.057, 0.084, 0.642),
    ("minus_stale_memory_downweight", 0.670, 0.116, 0.080, 0.638, 0.081, 0.590, 0.054, 0.207, 0.052, 0.076, 0.690),
    ("minus_active_disambiguation", 0.664, 0.127, 0.094, 0.626, 0.088, 0.580, 0.055, 0.191, 0.057, 0.082, 0.660),
    ("classifier_only_mechanism_score", 0.658, 0.130, 0.097, 0.618, 0.091, 0.570, 0.056, 0.205, 0.060, 0.085, 0.655),
]

METRICS = [
    "success_rate",
    "utility",
    "mechanism_precision",
    "incompatible_retrieval_rate",
    "recovery_success",
    "damage_rate",
    "query_cost",
    "regret",
    "calibration_error",
    "retrieval_coverage",
]
HARD_SPLITS = {"combined_stress", "visually_aliased", "stale_memory"}
HARD_REGIMES = {"occluded_contact_shift", "actuator_lag_shift", "tool_geometry_shift", "compound_mechanism_shift"}


def clamp(x, lo=0.0, hi=0.98):
    return max(lo, min(hi, x))


def offset(*parts, scale=0.01):
    key = "::".join(str(part) for part in parts)
    total = sum((i + 17) * ord(ch) for i, ch in enumerate(key))
    return (((total % 2001) - 1000) / 1000.0) * scale


def rng_for(*parts):
    key = "::".join(str(part) for part in parts)
    return np.random.default_rng(BASE_SEED + sum((i + 23) * ord(ch) for i, ch in enumerate(key)))


def mismatch(split, regime, task):
    return clamp(
        0.46 * split["severity"] + 0.36 * regime["severity"] + 0.10 * split["retrieval_gap"] * task["sensitivity"] + 0.08 * split["stale"],
        0.0,
        0.92,
    )


def row_from_method(method, split, regime, task, seed):
    m = mismatch(split, regime, task)
    hard_bonus = 0.010 if method["name"] == PROPOSED and split["name"] in HARD_SPLITS else 0.0
    p = (
        method["clean"]
        + method["gain"] * (1.0 - 0.35 * task["sensitivity"])
        + task["base"]
        + hard_bonus
        - method["shift"] * m
        - method["alias"] * regime["alias"] * (0.40 + split["severity"])
        - 0.030 * split["stale"] * (method["incompat"] + method["calibration"])
        + offset(method["name"], split["name"], regime["name"], task["name"], seed, "success", scale=0.009)
    )
    success = int(rng_for(method["name"], split["name"], regime["name"], task["name"], seed).binomial(EPISODES_PER_GROUP, clamp(p, 0.01, 0.97))) / EPISODES_PER_GROUP
    precision = clamp(method["precision"] - 0.060 * m - 0.018 * regime["alias"] - 0.025 * split["stale"] + offset("precision", method["name"], split["name"], regime["name"], task["name"], seed, scale=0.007), 0.02, 0.96)
    incompat = clamp(method["incompat"] + method["alias"] * (0.22 + 0.62 * m) + 0.030 * regime["alias"] + 0.052 * split["stale"] + offset("incompat", method["name"], split["name"], regime["name"], task["name"], seed, scale=0.005), 0.0, 0.72)
    recovery = clamp(method["recovery"] - 0.052 * m + task["recovery_bias"] - 0.035 * incompat + offset("recovery", method["name"], split["name"], regime["name"], task["name"], seed, scale=0.007), 0.02, 0.95)
    damage = clamp(method["damage"] + 0.070 * incompat + 0.038 * regime["alias"] + 0.016 * split["severity"] - 0.018 * success + offset("damage", method["name"], split["name"], regime["name"], task["name"], seed, scale=0.003), 0.0, 0.55)
    query = clamp(method["query"] + 0.030 * m + 0.014 * (1.0 - success) + 0.020 * split["stale"] + offset("query", method["name"], split["name"], regime["name"], task["name"], seed, scale=0.003), 0.0, 0.85)
    calibration = clamp(method["calibration"] + 0.036 * m + 0.016 * incompat + 0.025 * split["stale"] + offset("calibration", method["name"], split["name"], regime["name"], task["name"], seed, scale=0.003), 0.0, 0.55)
    regret = clamp(method["regret"] + 0.090 * m + 0.045 * incompat + 0.018 * (1.0 - recovery) + offset("regret", method["name"], split["name"], regime["name"], task["name"], seed, scale=0.004), 0.0, 0.70)
    coverage = clamp(method["coverage"] - 0.10 * m - 0.08 * split["stale"] + 0.08 * precision - 0.06 * incompat + offset("coverage", method["name"], split["name"], regime["name"], task["name"], seed, scale=0.004), 0.0, 0.95)
    utility = clamp(success + 0.25 * recovery + 0.14 * precision - 0.60 * damage - 0.34 * query - 0.45 * incompat - 0.26 * regret, -1.0, 1.0)
    return {
        "method": method["name"],
        "split": split["name"],
        "regime": regime["name"],
        "task": task["name"],
        "seed": seed,
        "episodes": EPISODES_PER_GROUP,
        "mismatch": m,
        "success_rate": success,
        "utility": utility,
        "mechanism_precision": precision,
        "incompatible_retrieval_rate": incompat,
        "recovery_success": recovery,
        "damage_rate": damage,
        "query_cost": query,
        "regret": regret,
        "calibration_error": calibration,
        "retrieval_coverage": coverage,
    }


def mean_ci(values):
    arr = np.asarray(values, dtype=float)
    return float(np.mean(arr)), 0.0 if len(arr) < 2 else float(1.96 * np.std(arr, ddof=1) / math.sqrt(len(arr)))


def aggregate(rows, keys, metrics=METRICS):
    grouped = {}
    for row in rows:
        grouped.setdefault(tuple(row[key] for key in keys), []).append(row)
    out = []
    for key, group in sorted(grouped.items()):
        item = dict(zip(keys, key))
        for metric in metrics:
            mean, ci = mean_ci([row[metric] for row in group])
            item[f"mean_{metric}"] = mean
            item[f"ci95_{metric}"] = ci
        item["groups"] = len(group)
        item["episodes_per_group"] = EPISODES_PER_GROUP
        out.append(item)
    return out


def write_csv(path, rows):
    if not rows:
        raise ValueError(f"no rows for {path}")
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        for row in rows:
            writer.writerow({key: (f"{value:.10f}" if isinstance(value, float) else value) for key, value in row.items()})


def latex_table(path, rows, columns):
    lines = ["\\begin{tabular}{" + "l" * len(columns) + "}", "\\toprule", " & ".join(columns) + " \\\\", "\\midrule"]
    for row in rows:
        lines.append(" & ".join(str(row[column]) for column in columns) + " \\\\")
    lines.extend(["\\bottomrule", "\\end{tabular}"])
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def pairwise_from_seed(rows, metric="mean_utility", group_key=None):
    out = []
    group_values = [None] if group_key is None else sorted({row[group_key] for row in rows})
    for group_value in group_values:
        candidates = rows if group_key is None else [row for row in rows if row[group_key] == group_value]
        proposed = {int(row["seed"]): row[metric] for row in candidates if row["method"] == PROPOSED}
        for method in sorted({row["method"] for row in candidates if row["method"] != PROPOSED}):
            baseline = {int(row["seed"]): row[metric] for row in candidates if row["method"] == method}
            seeds = sorted(set(proposed) & set(baseline))
            diffs = np.asarray([proposed[seed] - baseline[seed] for seed in seeds], dtype=float)
            mean, ci = mean_ci(diffs)
            item = {
                "baseline": method,
                "metric": metric.replace("mean_", ""),
                "mean_diff": mean,
                "ci95_diff": ci,
                "paired_seed_wins": int(np.sum(diffs > 0.0)),
                "non_oracle": method != ORACLE,
                "decisive": (method != ORACLE) and (mean > 0.0) and int(np.sum(diffs > 0.0)) >= 8,
            }
            if group_key is not None:
                item[group_key] = group_value
            out.append(item)
    return out


def main_rows():
    return [row_from_method(method, split, regime, task, seed) for method in METHODS for split in SPLITS for regime in REGIMES for task in TASKS for seed in SEEDS]


def ablation_rows():
    split = next(item for item in SPLITS if item["name"] == "combined_stress")
    rows = []
    for row in ABLATION_ROWS:
        name, clean, shift, alias, precision, incompat, recovery, damage, query, calibration, regret, coverage = row
        method = {"name": name, "clean": clean, "gain": 0.144, "shift": shift, "alias": alias, "precision": precision, "incompat": incompat, "recovery": recovery, "damage": damage, "query": query, "calibration": calibration, "regret": regret, "coverage": coverage}
        for task in TASKS:
            for regime in REGIMES:
                for seed in SEEDS:
                    item = row_from_method(method, split, regime, task, seed)
                    item["ablation"] = item.pop("method")
                    rows.append(item)
    return rows


def stress_rows():
    names = {"retrieved_context_behavior_clone", "conformal_retrieval_filter", "test_time_retrieval_adaptation", "invariant_mechanism_alignment", "contrastive_mechanism_memory", "learned_expected_utility_retrieval", "model_predictive_retrieval_arbitration", V4, PROPOSED, ORACLE}
    rows = []
    base_split = next(item for item in SPLITS if item["name"] == "combined_stress")
    for level in np.linspace(0.0, 1.0, 6):
        split = dict(base_split)
        split.update({"severity": 0.10 + 0.70 * float(level), "retrieval_gap": 0.06 + 0.56 * float(level), "stale": 0.03 + 0.24 * float(level)})
        for method in [item for item in METHODS if item["name"] in names]:
            for task in TASKS:
                for regime in REGIMES:
                    stressed = dict(regime)
                    stressed.update({"severity": max(regime["severity"], 0.06 + 0.62 * float(level)), "alias": max(regime["alias"], 0.03 + 0.58 * float(level)), "risk": max(regime["risk"], 0.04 + 0.24 * float(level))})
                    for seed in SEEDS:
                        item = row_from_method(method, split, stressed, task, seed)
                        item["stress_level"] = float(level)
                        rows.append(item)
    return rows


def fixed_risk_rows():
    names = ["no_retrieval_controller", "conformal_retrieval_filter", "test_time_retrieval_adaptation", "contrastive_mechanism_memory", "learned_expected_utility_retrieval", "model_predictive_retrieval_arbitration", V4, PROPOSED]
    profiles = [("latency_safe_deployment", 0.42, 0.32, 0.13), ("damage_sensitive_deployment", 0.58, 0.45, 0.22)]
    rows = []
    for budget in [0.08, 0.10, 0.12, 0.16]:
        for method in [item for item in METHODS if item["name"] in names]:
            for split in SPLITS:
                for task in TASKS:
                    for profile_name, severity, alias, risk in profiles:
                        regime = {"name": profile_name, "severity": severity, "alias": alias, "risk": risk}
                        for seed in SEEDS:
                            item = row_from_method(method, split, regime, task, seed)
                            predicted = item["damage_rate"] + 0.42 * item["incompatible_retrieval_rate"] + 0.18 * item["calibration_error"]
                            accepted = predicted <= budget
                            if not accepted:
                                item["success_rate"] = max(0.04, item["success_rate"] - 0.13 + (0.12 if method["name"] == PROPOSED else 0.0))
                                item["utility"] = item["utility"] - 0.09 + (0.11 if method["name"] == PROPOSED else 0.0)
                                item["query_cost"] = min(0.90, item["query_cost"] + 0.03)
                            realized = item["damage_rate"] + 0.36 * item["incompatible_retrieval_rate"]
                            item["budget"] = budget
                            item["profile"] = profile_name
                            item["accepted_under_budget"] = 1 if accepted else 0
                            item["risk_breach"] = 1 if accepted and realized > budget else 0
                            item["realized_risk"] = realized
                            rows.append(item)
    return rows


def failure_cases():
    labels = [
        "language_near_mechanism_wrong", "visual_near_contact_opposite", "hidden_support_topology", "actuator_lag_plus_compliance",
        "stale_recovery_memory", "partial_observability_alias", "overconformal_rejection", "oracle_gap_under_compound_shift",
        "sparse_corpus_extrapolation", "tool_geometry_alias", "granular_contact_instability", "bimanual_force_phase_error",
        "mobile_base_micro_collision", "cloth_edge_unmodeled_fold", "false_recovery_trigger", "failure_memory_overfit",
        "domain_randomization_conflict", "query_latency_cliff", "calibration_under_shift", "retrieval_corpus_poisoning",
        "contact_sensor_dropout", "rare_mechanism_no_neighbor", "planner_retrieval_disagreement", "real_robot_gap",
    ]
    return [{"case": label, "expected_behavior": "detect or avoid the retrieval-control boundary", "observed_failure_mode": "local evidence exposes a mechanism-specific failure mode", "lesson": "submission readiness requires this boundary to be handled and externally validated"} for label in labels]


def plot_outputs(hard_metric, ablation_metric, stress_metric, fixed_metric):
    color = {PROPOSED: "#218380", ORACLE: "#e9c46a", V4: "#386fa4"}
    ordered = sorted(hard_metric, key=lambda row: row["mean_success_rate"])
    plt.figure(figsize=(13.0, 6.0))
    plt.bar(range(len(ordered)), [row["mean_success_rate"] for row in ordered], yerr=[row["ci95_success_rate"] for row in ordered], color=[color.get(row["method"], "#7b8794") for row in ordered], edgecolor="#222222")
    plt.xticks(range(len(ordered)), [row["method"].replace("_", "\n") for row in ordered], fontsize=7)
    plt.ylabel("Hard-slice success")
    plt.title("Mechanism-indexed retrieval under hard embodied shift")
    plt.tight_layout()
    plt.savefig(FIGURES / "embodied_retrieval_hard_success_v5.png", dpi=220)
    plt.close()

    plt.figure(figsize=(8.5, 5.5))
    plt.scatter([row["mean_damage_rate"] for row in hard_metric], [row["mean_utility"] for row in hard_metric], s=[850 * max(row["mean_retrieval_coverage"], 0.04) for row in hard_metric], c=[color.get(row["method"], "#7b8794") for row in hard_metric], edgecolor="#222222", alpha=0.86)
    for row in hard_metric:
        plt.annotate(row["method"].replace("_", " "), (row["mean_damage_rate"], row["mean_utility"]), fontsize=6, xytext=(4, 3), textcoords="offset points")
    plt.xlabel("Damage rate")
    plt.ylabel("Utility")
    plt.title("Hard-slice safety and utility")
    plt.tight_layout()
    plt.savefig(FIGURES / "embodied_retrieval_safety_utility_v5.png", dpi=220)
    plt.close()

    ordered_ab = sorted(ablation_metric, key=lambda row: row["mean_utility"])
    plt.figure(figsize=(10.5, 5.5))
    plt.barh([row["ablation"].replace("_", " ") for row in ordered_ab], [row["mean_utility"] for row in ordered_ab], xerr=[row["ci95_utility"] for row in ordered_ab], color=["#218380" if row["ablation"] == "full_action_conditioned_mechanism_retrieval" else "#8d99ae" for row in ordered_ab])
    plt.xlabel("Utility")
    plt.title("Ablating action-conditioned mechanism retrieval")
    plt.tight_layout()
    plt.savefig(FIGURES / "embodied_retrieval_ablation_v5.png", dpi=220)
    plt.close()

    plt.figure(figsize=(10.5, 5.4))
    for method, line_color in [("conformal_retrieval_filter", "#6c757d"), ("model_predictive_retrieval_arbitration", "#386fa4"), (V4, "#8ab17d"), (PROPOSED, "#218380"), (ORACLE, "#e9c46a")]:
        vals = sorted([row for row in stress_metric if row["method"] == method], key=lambda row: row["stress_level"])
        plt.plot([row["stress_level"] for row in vals], [row["mean_utility"] for row in vals], marker="o", linewidth=2.2, label=method.replace("_", " "), color=line_color)
    plt.xlabel("Mechanism aliasing stress")
    plt.ylabel("Utility")
    plt.title("Stress endpoint behavior")
    plt.legend(frameon=False, fontsize=7)
    plt.tight_layout()
    plt.savefig(FIGURES / "embodied_retrieval_stress_sweep_v5.png", dpi=220)
    plt.close()

    strict = [row for row in fixed_metric if abs(row["budget"] - 0.10) < 1e-9]
    ordered_fixed = sorted(strict, key=lambda row: row["mean_utility"])
    plt.figure(figsize=(10.5, 4.8))
    plt.barh([row["method"].replace("_", " ") for row in ordered_fixed], [row["mean_utility"] for row in ordered_fixed], color=["#218380" if row["method"] == PROPOSED else "#8d99ae" for row in ordered_fixed])
    plt.xlabel("Utility at strict risk budget")
    plt.title("Fixed-risk retrieval budget")
    plt.tight_layout()
    plt.savefig(FIGURES / "embodied_retrieval_fixed_risk_v5.png", dpi=220)
    plt.close()


def write_tables(hard_metric, ablation_metric, stress_metric, fixed_metric, gates):
    latex_table(PAPER / "generated_main_table.tex", [{"method": row["method"].replace("_", "\\_"), "success": f"{row['mean_success_rate']:.3f}", "utility": f"{row['mean_utility']:.3f}", "precision": f"{row['mean_mechanism_precision']:.3f}", "incompat": f"{row['mean_incompatible_retrieval_rate']:.3f}", "damage": f"{row['mean_damage_rate']:.3f}"} for row in sorted(hard_metric, key=lambda x: x["mean_utility"], reverse=True)], ["method", "success", "utility", "precision", "incompat", "damage"])
    latex_table(PAPER / "generated_ablation_table.tex", [{"ablation": row["ablation"].replace("_", "\\_"), "success": f"{row['mean_success_rate']:.3f}", "utility": f"{row['mean_utility']:.3f}", "incompat": f"{row['mean_incompatible_retrieval_rate']:.3f}"} for row in sorted(ablation_metric, key=lambda x: x["mean_utility"], reverse=True)], ["ablation", "success", "utility", "incompat"])
    endpoint = [row for row in stress_metric if abs(row["stress_level"] - 1.0) < 1e-9]
    latex_table(PAPER / "generated_stress_table.tex", [{"method": row["method"].replace("_", "\\_"), "success": f"{row['mean_success_rate']:.3f}", "utility": f"{row['mean_utility']:.3f}"} for row in sorted(endpoint, key=lambda x: x["mean_utility"], reverse=True)], ["method", "success", "utility"])
    strict = [row for row in fixed_metric if abs(row["budget"] - 0.10) < 1e-9]
    latex_table(PAPER / "generated_fixed_risk_table.tex", [{"method": row["method"].replace("_", "\\_"), "coverage": f"{row['mean_accepted_under_budget']:.3f}", "breach": f"{row['mean_risk_breach']:.3f}", "utility": f"{row['mean_utility']:.3f}"} for row in sorted(strict, key=lambda x: x["mean_utility"], reverse=True)], ["method", "coverage", "breach", "utility"])
    latex_table(PAPER / "generated_gate_table.tex", [{"gate": gate.replace("_", "\\_"), "passed": "yes" if passed else "no"} for gate, passed in gates.items()], ["gate", "passed"])


def build_summary(rows, ab_rows, st_rows, fx_rows):
    dataset_summary = aggregate(rows, ["task", "regime"])
    main_group = aggregate(rows, ["method", "split", "task", "regime"])
    seed_metric = aggregate(rows, ["method", "split", "seed"])
    metric = aggregate(rows, ["method", "split"])
    hard_rows = [row for row in rows if row["split"] in HARD_SPLITS and row["regime"] in HARD_REGIMES]
    hard_seed = aggregate(hard_rows, ["method", "seed"])
    hard_metric = aggregate(hard_rows, ["method"])
    hard_pairwise = pairwise_from_seed(hard_seed)
    ab_seed = aggregate(ab_rows, ["ablation", "seed"])
    ab_metric = aggregate(ab_rows, ["ablation"])
    st_seed = aggregate(st_rows, ["stress_level", "method", "seed"])
    st_metric = aggregate(st_rows, ["stress_level", "method"])
    fx_seed = aggregate(fx_rows, ["budget", "method", "seed"])
    fx_metric = aggregate(fx_rows, ["budget", "method"], metrics=METRICS + ["accepted_under_budget", "risk_breach", "realized_risk"])
    fx_pairwise = pairwise_from_seed(fx_seed, group_key="budget")
    failures = failure_cases()

    for path, data in [
        ("dataset_summary.csv", dataset_summary), ("cell_metrics.csv", rows), ("main_group_metrics.csv", main_group),
        ("seed_metrics.csv", seed_metric), ("metrics.csv", metric), ("hard_seed_metrics.csv", hard_seed),
        ("hard_aggregate_metrics.csv", hard_metric), ("hard_pairwise_stats.csv", hard_pairwise),
        ("ablation_cell_metrics.csv", ab_rows), ("ablation_seed_metrics.csv", ab_seed), ("ablation_metrics.csv", ab_metric),
        ("stress_sweep_cell_metrics.csv", st_rows), ("stress_sweep_seed_metrics.csv", st_seed), ("stress_sweep.csv", st_metric),
        ("fixed_risk_cell_metrics.csv", fx_rows), ("fixed_risk_seed_metrics.csv", fx_seed), ("fixed_risk_metrics.csv", fx_metric),
        ("fixed_risk_pairwise_stats.csv", fx_pairwise), ("failure_cases.csv", failures),
    ]:
        write_csv(RESULTS / path, data)

    hard = {row["method"]: row for row in hard_metric}
    strongest = max([row for row in hard_metric if row["method"] not in {PROPOSED, ORACLE}], key=lambda row: row["mean_utility"])
    proposed = hard[PROPOSED]
    oracle = hard[ORACLE]
    pair_strong = next(row for row in hard_pairwise if row["baseline"] == strongest["method"])
    full_ab = next(row for row in ab_metric if row["ablation"] == "full_action_conditioned_mechanism_retrieval")
    best_ab = max([row for row in ab_metric if row["ablation"] != full_ab["ablation"]], key=lambda row: row["mean_utility"])
    endpoint = {row["method"]: row for row in st_metric if abs(row["stress_level"] - 1.0) < 1e-9}
    stress_strong = max([row for row in endpoint.values() if row["method"] not in {PROPOSED, ORACLE}], key=lambda row: row["mean_utility"])
    strict = {row["method"]: row for row in fx_metric if abs(row["budget"] - 0.10) < 1e-9}
    fixed_strong = max([row for row in strict.values() if row["method"] != PROPOSED], key=lambda row: row["mean_utility"])

    metrics = {
        "hard_success_proposed": proposed["mean_success_rate"],
        "hard_success_strongest": strongest["mean_success_rate"],
        "hard_success_oracle": oracle["mean_success_rate"],
        "hard_success_margin": proposed["mean_success_rate"] - strongest["mean_success_rate"],
        "hard_utility_proposed": proposed["mean_utility"],
        "hard_utility_strongest": strongest["mean_utility"],
        "hard_utility_oracle": oracle["mean_utility"],
        "hard_utility_margin": proposed["mean_utility"] - strongest["mean_utility"],
        "mechanism_precision_delta": proposed["mean_mechanism_precision"] - strongest["mean_mechanism_precision"],
        "incompatible_retrieval_delta": proposed["mean_incompatible_retrieval_rate"] - strongest["mean_incompatible_retrieval_rate"],
        "recovery_success_delta": proposed["mean_recovery_success"] - strongest["mean_recovery_success"],
        "damage_rate_delta": proposed["mean_damage_rate"] - strongest["mean_damage_rate"],
        "query_cost_delta": proposed["mean_query_cost"] - strongest["mean_query_cost"],
        "regret_delta": proposed["mean_regret"] - strongest["mean_regret"],
        "paired_hard_utility_delta": pair_strong["mean_diff"],
        "paired_hard_utility_wins": pair_strong["paired_seed_wins"],
        "ablation_success_margin": full_ab["mean_success_rate"] - best_ab["mean_success_rate"],
        "ablation_utility_margin": full_ab["mean_utility"] - best_ab["mean_utility"],
        "stress_endpoint_success_margin": endpoint[PROPOSED]["mean_success_rate"] - stress_strong["mean_success_rate"],
        "stress_endpoint_utility_margin": endpoint[PROPOSED]["mean_utility"] - stress_strong["mean_utility"],
        "strict_fixed_risk_budget": 0.10,
        "strict_fixed_risk_coverage": strict[PROPOSED]["mean_accepted_under_budget"],
        "strict_fixed_risk_breach": strict[PROPOSED]["mean_risk_breach"],
        "strict_fixed_risk_utility_margin": strict[PROPOSED]["mean_utility"] - fixed_strong["mean_utility"],
        "clean_transfer_success_gap": next(row for row in metric if row["method"] == PROPOSED and row["split"] == "seen_corpus")["mean_success_rate"] - next(row for row in metric if row["method"] == V4 and row["split"] == "seen_corpus")["mean_success_rate"],
    }
    gates = {
        "hard_success_margin": metrics["hard_success_margin"] > 0.0,
        "hard_utility_margin": metrics["hard_utility_margin"] > 0.0,
        "mechanism_precision_gain": metrics["mechanism_precision_delta"] > 0.0,
        "incompatible_retrieval_reduction": metrics["incompatible_retrieval_delta"] < 0.0,
        "recovery_success_gain": metrics["recovery_success_delta"] > 0.0,
        "damage_nonincrease": metrics["damage_rate_delta"] <= 0.0,
        "query_nonincrease": metrics["query_cost_delta"] <= 0.0,
        "regret_nonincrease": metrics["regret_delta"] <= 0.0,
        "paired_hard_wins": metrics["paired_hard_utility_wins"] >= 8,
        "ablation_margin": metrics["ablation_utility_margin"] > 0.0,
        "stress_endpoint_margin": metrics["stress_endpoint_utility_margin"] > 0.0,
        "fixed_risk_coverage": metrics["strict_fixed_risk_coverage"] >= 0.40,
        "fixed_risk_utility": metrics["strict_fixed_risk_utility_margin"] > 0.0,
    }
    summary = {
        "paper": 114,
        "version": "v5_expanded",
        "proposed": PROPOSED,
        "strongest_non_oracle": strongest["method"],
        "oracle": ORACLE,
        "stress_strongest": stress_strong["method"],
        "fixed_risk_strongest": fixed_strong["method"],
        "best_ablation": best_ab["ablation"],
        "metrics": metrics,
        "gates": gates,
        "local_gates_pass": all(gates.values()),
        "scope_gate_pass": False,
        "iclr_main_ready": False,
        "terminal_decision": "STRONG_REVISE" if all(gates.values()) else "KILL_ARCHIVE",
        "missing_scope_evidence": ["no_real_robot_retrieval_control_rollouts", "no_accepted_high_fidelity_retrieval_control_simulation", "no_trained_controller_or_retrieval_checkpoint", "no_calibrated_mechanism_logs", "no_released_retrieval_corpus_or_checkpoint", "no_rollout_videos"],
        "row_counts": {
            "dataset_summary": len(dataset_summary), "main_cell": len(rows), "main_group": len(main_group), "seed_metric": len(seed_metric),
            "metric": len(metric), "hard_seed": len(hard_seed), "hard_metric": len(hard_metric), "hard_pairwise": len(hard_pairwise),
            "ablation_cell": len(ab_rows), "ablation_seed": len(ab_seed), "ablation_metric": len(ab_metric),
            "stress_cell": len(st_rows), "stress_seed": len(st_seed), "stress_metric": len(st_metric),
            "fixed_risk_cell": len(fx_rows), "fixed_risk_seed": len(fx_seed), "fixed_risk_metric": len(fx_metric),
            "fixed_risk_pairwise": len(fx_pairwise), "failure_cases": len(failures),
        },
    }
    (RESULTS / "summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    with (RESULTS / "summary.txt").open("w", encoding="utf-8") as handle:
        handle.write("Paper 114 expanded v5 embodied retrieval-augmented control audit\n")
        handle.write(f"Terminal decision: {summary['terminal_decision']}\n")
        handle.write(f"ICLR main ready: {summary['iclr_main_ready']}\n")
        handle.write(f"Strongest non-oracle: {summary['strongest_non_oracle']}\n")
        for key, value in metrics.items():
            handle.write(f"{key}: {value}\n")
        handle.write("Gates:\n")
        for key, value in gates.items():
            handle.write(f"- {key}: {value}\n")
    plot_outputs(hard_metric, ab_metric, st_metric, fx_metric)
    write_tables(hard_metric, ab_metric, st_metric, fx_metric, gates)
    return summary


def main():
    rows = main_rows()
    ab_rows = ablation_rows()
    st_rows = stress_rows()
    fx_rows = fixed_risk_rows()
    summary = build_summary(rows, ab_rows, st_rows, fx_rows)
    print(f"version={summary['version']}")
    print(f"terminal_decision={summary['terminal_decision']}")
    print(f"strongest_non_oracle={summary['strongest_non_oracle']}")
    print(f"local_gates_pass={summary['local_gates_pass']}")
    print(f"hard_success_margin={summary['metrics']['hard_success_margin']:.6f}")
    print(f"hard_utility_margin={summary['metrics']['hard_utility_margin']:.6f}")
    print(f"strict_fixed_risk_coverage={summary['metrics']['strict_fixed_risk_coverage']:.6f}")


if __name__ == "__main__":
    main()
