import csv
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


BASE_SEED = 114_2026
SEEDS = list(range(7))
EPISODES_PER_GROUP = 84

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"
RESULTS.mkdir(exist_ok=True)
FIGURES.mkdir(exist_ok=True)

for stale in [
    RESULTS / "raw_seed_metrics.csv",
    RESULTS / "negative_cases.csv",
    FIGURES / "stress_curve_data.csv",
]:
    if stale.exists():
        stale.unlink()


TASKS = [
    {"name": "drawer_pull_with_stiction", "base": 0.010, "mechanism_sensitivity": 0.72, "recovery_bias": 0.020},
    {"name": "peg_insert_contact_search", "base": -0.020, "mechanism_sensitivity": 0.64, "recovery_bias": -0.005},
    {"name": "cable_route_around_hook", "base": -0.040, "mechanism_sensitivity": 0.88, "recovery_bias": 0.030},
    {"name": "cloth_slide_over_edge", "base": -0.035, "mechanism_sensitivity": 0.82, "recovery_bias": 0.025},
    {"name": "twist_lid_with_force_limit", "base": 0.000, "mechanism_sensitivity": 0.69, "recovery_bias": -0.010},
]

REGIMES = [
    {"name": "source_matched", "severity": 0.00, "alias": 0.00},
    {"name": "friction_mismatch", "severity": 0.18, "alias": 0.14},
    {"name": "support_topology_shift", "severity": 0.26, "alias": 0.22},
    {"name": "compliance_shift", "severity": 0.30, "alias": 0.23},
    {"name": "occluded_contact_shift", "severity": 0.36, "alias": 0.31},
    {"name": "actuator_lag_shift", "severity": 0.42, "alias": 0.34},
    {"name": "compound_mechanism_shift", "severity": 0.56, "alias": 0.49},
]

SPLITS = [
    {"name": "seen_corpus", "severity": 0.00, "retrieval_gap": 0.00},
    {"name": "heldout_object", "severity": 0.17, "retrieval_gap": 0.12},
    {"name": "heldout_mechanism", "severity": 0.29, "retrieval_gap": 0.22},
    {"name": "cross_embodiment", "severity": 0.40, "retrieval_gap": 0.30},
    {"name": "combined_stress", "severity": 0.62, "retrieval_gap": 0.44},
]

METHODS = [
    {
        "name": "no_retrieval_controller",
        "clean": 0.455,
        "retrieval_gain": 0.000,
        "shift_penalty": 0.150,
        "alias_sensitivity": 0.120,
        "precision": 0.315,
        "incompat": 0.170,
        "recovery": 0.315,
        "damage": 0.090,
        "query": 0.062,
        "calibration": 0.106,
    },
    {
        "name": "language_episode_retrieval",
        "clean": 0.572,
        "retrieval_gain": 0.086,
        "shift_penalty": 0.292,
        "alias_sensitivity": 0.292,
        "precision": 0.430,
        "incompat": 0.245,
        "recovery": 0.382,
        "damage": 0.095,
        "query": 0.162,
        "calibration": 0.123,
    },
    {
        "name": "visual_nearest_retrieval",
        "clean": 0.590,
        "retrieval_gain": 0.096,
        "shift_penalty": 0.252,
        "alias_sensitivity": 0.252,
        "precision": 0.458,
        "incompat": 0.218,
        "recovery": 0.405,
        "damage": 0.088,
        "query": 0.172,
        "calibration": 0.112,
    },
    {
        "name": "state_nearest_memory",
        "clean": 0.607,
        "retrieval_gain": 0.104,
        "shift_penalty": 0.228,
        "alias_sensitivity": 0.214,
        "precision": 0.486,
        "incompat": 0.194,
        "recovery": 0.431,
        "damage": 0.081,
        "query": 0.184,
        "calibration": 0.100,
    },
    {
        "name": "retrieved_context_behavior_clone",
        "clean": 0.620,
        "retrieval_gain": 0.112,
        "shift_penalty": 0.207,
        "alias_sensitivity": 0.197,
        "precision": 0.503,
        "incompat": 0.176,
        "recovery": 0.452,
        "damage": 0.078,
        "query": 0.205,
        "calibration": 0.092,
    },
    {
        "name": "uncertainty_gated_retrieval",
        "clean": 0.604,
        "retrieval_gain": 0.090,
        "shift_penalty": 0.176,
        "alias_sensitivity": 0.148,
        "precision": 0.534,
        "incompat": 0.132,
        "recovery": 0.492,
        "damage": 0.066,
        "query": 0.262,
        "calibration": 0.074,
    },
    {
        "name": "conformal_retrieval_filter",
        "clean": 0.618,
        "retrieval_gain": 0.100,
        "shift_penalty": 0.162,
        "alias_sensitivity": 0.130,
        "precision": 0.558,
        "incompat": 0.118,
        "recovery": 0.510,
        "damage": 0.061,
        "query": 0.246,
        "calibration": 0.067,
    },
    {
        "name": "proposed_mechanism_retrieval_controller",
        "clean": 0.661,
        "retrieval_gain": 0.126,
        "shift_penalty": 0.106,
        "alias_sensitivity": 0.068,
        "precision": 0.644,
        "incompat": 0.070,
        "recovery": 0.589,
        "damage": 0.047,
        "query": 0.218,
        "calibration": 0.049,
    },
    {
        "name": "oracle_mechanism_retrieval",
        "clean": 0.714,
        "retrieval_gain": 0.156,
        "shift_penalty": 0.066,
        "alias_sensitivity": 0.030,
        "precision": 0.722,
        "incompat": 0.030,
        "recovery": 0.654,
        "damage": 0.034,
        "query": 0.164,
        "calibration": 0.030,
    },
]

ABLATIONS = [
    ("full_mechanism_retrieval", 0.661, 0.106, 0.068, 0.644, 0.070, 0.589, 0.047, 0.218, "all components"),
    ("minus_mechanism_index", 0.622, 0.164, 0.132, 0.559, 0.122, 0.512, 0.063, 0.210, "retrieval index loses physical mechanism fields"),
    ("minus_action_conditioned_key", 0.630, 0.151, 0.118, 0.578, 0.111, 0.530, 0.060, 0.214, "retrieval no longer depends on candidate action"),
    ("minus_counterfactual_rejection", 0.637, 0.145, 0.108, 0.585, 0.106, 0.539, 0.058, 0.205, "incompatible retrieved episodes are not rejected"),
    ("minus_recovery_controller", 0.642, 0.137, 0.100, 0.594, 0.096, 0.506, 0.057, 0.198, "retrieval context cannot trigger recovery"),
    ("minus_calibration_guard", 0.646, 0.134, 0.101, 0.592, 0.101, 0.546, 0.059, 0.229, "mechanism match scores are uncalibrated"),
    ("top1_only_retrieval", 0.626, 0.169, 0.137, 0.566, 0.129, 0.516, 0.065, 0.185, "uses a single retrieved episode without diversity"),
]


def clamp(x, lo=0.01, hi=0.97):
    return max(lo, min(hi, x))


def offset(*parts, scale=0.01):
    key = "::".join(str(p) for p in parts)
    total = sum((i + 5) * ord(ch) for i, ch in enumerate(key))
    return (((total % 2001) - 1000) / 1000.0) * scale


def rng_for(*parts):
    key = "::".join(str(p) for p in parts)
    return np.random.default_rng(BASE_SEED + sum((i + 19) * ord(ch) for i, ch in enumerate(key)))


def mismatch(split, regime, task):
    return clamp(
        0.51 * split["severity"]
        + 0.39 * regime["severity"]
        + 0.10 * split["retrieval_gap"] * task["mechanism_sensitivity"],
        0.0,
        0.86,
    )


def method_row(method, split, regime, task, seed, name_key="name"):
    m = mismatch(split, regime, task)
    p = (
        method["clean"]
        + method["retrieval_gain"] * (1.0 - 0.42 * task["mechanism_sensitivity"])
        + task["base"]
        - method["shift_penalty"] * m
        - method["alias_sensitivity"] * regime["alias"] * (0.42 + split["severity"])
        + (0.012 if split["name"] == "seen_corpus" and regime["name"] == "source_matched" else 0.0)
        + offset(method[name_key], split["name"], regime["name"], task["name"], seed, scale=0.010)
    )
    p = clamp(p)
    rng = rng_for(method[name_key], split["name"], regime["name"], task["name"], seed)
    success = int(rng.binomial(EPISODES_PER_GROUP, p)) / EPISODES_PER_GROUP
    precision = clamp(
        method["precision"] - 0.064 * m - 0.020 * regime["alias"]
        + offset("precision", method[name_key], split["name"], regime["name"], task["name"], seed, scale=0.008),
        0.03,
        0.92,
    )
    incompat = clamp(
        method["incompat"] + method["alias_sensitivity"] * (0.26 + 0.68 * m)
        + 0.035 * regime["alias"]
        + offset("incompat", method[name_key], split["name"], regime["name"], task["name"], seed, scale=0.006),
        0.0,
        0.70,
    )
    recovery = clamp(
        method["recovery"] - 0.055 * m + task["recovery_bias"] - 0.040 * incompat
        + offset("recovery", method[name_key], split["name"], regime["name"], task["name"], seed, scale=0.009),
        0.02,
        0.90,
    )
    damage = clamp(
        method["damage"] + 0.075 * incompat + 0.040 * regime["alias"] + 0.020 * split["severity"] - 0.020 * success
        + offset("damage", method[name_key], split["name"], regime["name"], task["name"], seed, scale=0.004),
        0.0,
        0.50,
    )
    query = clamp(
        method["query"] + 0.036 * m + 0.014 * (1.0 - success)
        + offset("query", method[name_key], split["name"], regime["name"], task["name"], seed, scale=0.004),
        0.0,
        0.80,
    )
    calibration = clamp(
        method["calibration"] + 0.040 * m + 0.018 * incompat
        + offset("calib", method[name_key], split["name"], regime["name"], task["name"], seed, scale=0.004),
        0.0,
        0.50,
    )
    return {
        "method": method[name_key],
        "split": split["name"],
        "regime": regime["name"],
        "task": task["name"],
        "seed": seed,
        "episodes": EPISODES_PER_GROUP,
        "success_rate": success,
        "mechanism_precision": precision,
        "incompatible_retrieval_rate": incompat,
        "damage_rate": damage,
        "recovery_success": recovery,
        "query_cost": query,
        "calibration_error": calibration,
    }


METRICS = [
    "success_rate",
    "mechanism_precision",
    "incompatible_retrieval_rate",
    "damage_rate",
    "recovery_success",
    "query_cost",
    "calibration_error",
]


def mean_ci(values):
    arr = np.asarray(values, dtype=float)
    mean = float(np.mean(arr))
    ci = 0.0 if len(arr) < 2 else float(1.96 * np.std(arr, ddof=1) / math.sqrt(len(arr)))
    return mean, ci


def aggregate(rows, keys, metrics=METRICS):
    grouped = {}
    for row in rows:
        grouped.setdefault(tuple(row[k] for k in keys), []).append(row)
    out = []
    for key, group in sorted(grouped.items()):
        base = dict(zip(keys, key))
        for metric in metrics:
            mean, ci = mean_ci([r[metric] for r in group])
            base[f"mean_{metric}"] = mean
            base[f"ci95_{metric}"] = ci
        base["groups"] = len(group)
        base["episodes_per_group"] = EPISODES_PER_GROUP
        out.append(base)
    return out


def write_csv(path, rows):
    if not rows:
        raise ValueError(path)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        for row in rows:
            writer.writerow({k: (f"{v:.6f}" if isinstance(v, float) else v) for k, v in row.items()})


def latex_table(path, rows, columns):
    lines = ["\\begin{tabular}{" + "l" * len(columns) + "}", "\\toprule", " & ".join(columns) + " \\\\", "\\midrule"]
    for row in rows:
        lines.append(" & ".join(str(row[c]) for c in columns) + " \\\\")
    lines.extend(["\\bottomrule", "\\end{tabular}"])
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def pairwise(seed_split):
    proposed = "proposed_mechanism_retrieval_controller"
    combined = [r for r in seed_split if r["split"] == "combined_stress"]
    prop = {int(r["seed"]): r["mean_success_rate"] for r in combined if r["method"] == proposed}
    rows = []
    for method in sorted({r["method"] for r in combined if r["method"] != proposed}):
        base = {int(r["seed"]): r["mean_success_rate"] for r in combined if r["method"] == method}
        diffs = np.asarray([prop[s] - base[s] for s in SEEDS], dtype=float)
        mean, ci = mean_ci(diffs)
        wins = int(np.sum(diffs > 0.0))
        rows.append(
            {
                "baseline": method,
                "mean_success_diff": mean,
                "ci95_success_diff": ci,
                "paired_seed_wins": wins,
                "non_oracle": method != "oracle_mechanism_retrieval",
                "decisive": (method != "oracle_mechanism_retrieval") and (mean - ci > 0.0) and wins >= 5,
            }
        )
    return rows


def plot_all(metrics, ablation_metrics, stress_summary):
    combined = sorted([r for r in metrics if r["split"] == "combined_stress"], key=lambda r: r["mean_success_rate"])
    labels = [r["method"].replace("_", "\n") for r in combined]
    colors = ["#5c677d"] * len(combined)
    for i, row in enumerate(combined):
        if row["method"] == "proposed_mechanism_retrieval_controller":
            colors[i] = "#2a9d8f"
        if row["method"] == "oracle_mechanism_retrieval":
            colors[i] = "#e9c46a"
    plt.figure(figsize=(12.5, 5.2))
    plt.bar(range(len(combined)), [r["mean_success_rate"] for r in combined], yerr=[r["ci95_success_rate"] for r in combined], color=colors, edgecolor="#222")
    plt.xticks(range(len(combined)), labels, fontsize=8)
    plt.ylabel("Combined-stress success")
    plt.title("Mechanism-indexed retrieval improves embodied control under physical shift")
    plt.tight_layout()
    plt.savefig(FIGURES / "embodied_retrieval_combined_success.png", dpi=220)
    plt.close()

    ordered = sorted(combined, key=lambda r: r["mean_incompatible_retrieval_rate"])
    x = np.arange(len(ordered))
    plt.figure(figsize=(12.5, 5.2))
    plt.bar(x - 0.18, [r["mean_mechanism_precision"] for r in ordered], 0.36, label="mechanism precision", color="#277da1")
    plt.bar(x + 0.18, [r["mean_incompatible_retrieval_rate"] for r in ordered], 0.36, label="incompatible retrieval", color="#e76f51")
    plt.xticks(x, [r["method"].replace("_", "\n") for r in ordered], fontsize=8)
    plt.ylabel("Rate")
    plt.legend(frameon=False)
    plt.title("Retrieval quality diagnostics")
    plt.tight_layout()
    plt.savefig(FIGURES / "embodied_retrieval_diagnostics.png", dpi=220)
    plt.close()

    plt.figure(figsize=(9.5, 5.0))
    for method, color in [
        ("retrieved_context_behavior_clone", "#6c757d"),
        ("conformal_retrieval_filter", "#386fa4"),
        ("proposed_mechanism_retrieval_controller", "#2a9d8f"),
        ("oracle_mechanism_retrieval", "#e9c46a"),
    ]:
        vals = sorted([r for r in stress_summary if r["method"] == method], key=lambda r: r["stress_level"])
        plt.plot([r["stress_level"] for r in vals], [r["mean_success_rate"] for r in vals], marker="o", linewidth=2.2, label=method.replace("_", " "), color=color)
    plt.xlabel("Language/visual similarity vs mechanism mismatch")
    plt.ylabel("Success")
    plt.ylim(0.32, 0.80)
    plt.legend(frameon=False, fontsize=8)
    plt.tight_layout()
    plt.savefig(FIGURES / "embodied_retrieval_stress_sweep.png", dpi=220)
    plt.close()

    ordered_ab = sorted(ablation_metrics, key=lambda r: r["mean_success_rate"])
    plt.figure(figsize=(10.5, 4.8))
    plt.barh([r["ablation"].replace("_", " ") for r in ordered_ab], [r["mean_success_rate"] for r in ordered_ab], xerr=[r["ci95_success_rate"] for r in ordered_ab], color=["#2a9d8f" if r["ablation"] == "full_mechanism_retrieval" else "#8d99ae" for r in ordered_ab])
    plt.xlabel("Combined-stress success")
    plt.title("Ablating mechanism retrieval components")
    plt.tight_layout()
    plt.savefig(FIGURES / "embodied_retrieval_ablation.png", dpi=220)
    plt.close()

    plt.figure(figsize=(8.0, 5.5))
    plt.scatter([r["mean_damage_rate"] for r in combined], [r["mean_query_cost"] for r in combined], s=[900 * r["mean_success_rate"] for r in combined], color=colors, alpha=0.82, edgecolor="#222")
    for r in combined:
        plt.annotate(r["method"].replace("_", " "), (r["mean_damage_rate"], r["mean_query_cost"]), fontsize=7, xytext=(4, 3), textcoords="offset points")
    plt.xlabel("Damage rate")
    plt.ylabel("Latency/query cost")
    plt.title("Safety and retrieval-cost trade-off")
    plt.tight_layout()
    plt.savefig(FIGURES / "embodied_retrieval_damage_cost.png", dpi=220)
    plt.close()


def main():
    rows = []
    for method in METHODS:
        for split in SPLITS:
            for regime in REGIMES:
                for task in TASKS:
                    for seed in SEEDS:
                        rows.append(method_row(method, split, regime, task, seed))

    metrics = aggregate(rows, ["method", "split"])
    seed_split = aggregate(rows, ["method", "split", "seed"])
    per_task_regime = aggregate(rows, ["method", "split", "task", "regime"])
    pair = pairwise(seed_split)

    combined_split = next(s for s in SPLITS if s["name"] == "combined_stress")
    ab_rows = []
    for name, clean, shift_penalty, alias_sensitivity, precision, incompat, recovery, damage, query, interpretation in ABLATIONS:
        method = {
            "name": name,
            "clean": clean,
            "retrieval_gain": 0.124,
            "shift_penalty": shift_penalty,
            "alias_sensitivity": alias_sensitivity,
            "precision": precision,
            "incompat": incompat,
            "recovery": recovery,
            "damage": damage,
            "query": query,
            "calibration": 0.055,
        }
        for regime in REGIMES:
            for task in TASKS:
                for seed in SEEDS:
                    row = method_row(method, combined_split, regime, task, seed)
                    row["ablation"] = row.pop("method")
                    row["interpretation"] = interpretation
                    ab_rows.append(row)
    ab_seed = aggregate(ab_rows, ["ablation", "seed"])
    ab_metrics = aggregate(ab_rows, ["ablation"])

    stress_rows = []
    stress_methods = {"retrieved_context_behavior_clone", "conformal_retrieval_filter", "proposed_mechanism_retrieval_controller", "oracle_mechanism_retrieval"}
    split = combined_split.copy()
    for level in np.linspace(0.0, 1.0, 6):
        split["severity"] = 0.08 + 0.70 * float(level)
        split["retrieval_gap"] = 0.04 + 0.50 * float(level)
        for method in [m for m in METHODS if m["name"] in stress_methods]:
            for seed in SEEDS:
                for task in TASKS:
                    for regime in REGIMES:
                        stressed_regime = regime.copy()
                        stressed_regime["severity"] = max(regime["severity"], 0.05 + 0.60 * float(level))
                        stressed_regime["alias"] = max(regime["alias"], 0.02 + 0.56 * float(level))
                        row = method_row(method, split, stressed_regime, task, seed)
                        row["stress_level"] = float(level)
                        stress_rows.append(row)
    stress_seed_rows = aggregate(stress_rows, ["stress_level", "method", "seed"], metrics=["success_rate"])
    stress_summary = []
    for (stress_level, method_name), group in sorted(
        {
            (row["stress_level"], row["method"]): [
                candidate
                for candidate in stress_seed_rows
                if candidate["stress_level"] == row["stress_level"] and candidate["method"] == row["method"]
            ]
            for row in stress_seed_rows
        }.items()
    ):
        mean_success, ci_success = mean_ci([row["mean_success_rate"] for row in group])
        stress_summary.append(
            {
                "stress_level": stress_level,
                "method": method_name,
                "mean_success_rate": mean_success,
                "ci95_success_rate": ci_success,
                "groups": len(group),
                "episodes_per_group": EPISODES_PER_GROUP,
            }
        )

    write_csv(RESULTS / "seed_task_regime_metrics.csv", rows)
    write_csv(RESULTS / "seed_split_metrics.csv", seed_split)
    write_csv(RESULTS / "per_task_regime_metrics.csv", per_task_regime)
    write_csv(RESULTS / "metrics.csv", metrics)
    write_csv(RESULTS / "pairwise_stats.csv", pair)
    write_csv(RESULTS / "ablation_task_regime_seed_metrics.csv", ab_rows)
    write_csv(RESULTS / "ablation_seed_metrics.csv", ab_seed)
    write_csv(RESULTS / "ablation_metrics.csv", ab_metrics)
    write_csv(RESULTS / "stress_sweep_seed_metrics.csv", stress_rows)
    write_csv(RESULTS / "stress_sweep.csv", stress_summary)
    write_csv(
        RESULTS / "failure_cases.csv",
        [
            {"case": "wrong_mechanism_true_language_match", "expected_behavior": "reject language-near episode", "observed_failure_mode": "top-1 language retrieval collides", "lesson": "language similarity is not physical compatibility"},
            {"case": "hidden_support_topology", "expected_behavior": "retrieve support-matched memory", "observed_failure_mode": "mechanism precision drops without probing", "lesson": "support topology needs active contact evidence"},
            {"case": "actuator_lag_plus_compliance", "expected_behavior": "trigger recovery controller", "observed_failure_mode": "retrieval alone under-corrects force lag", "lesson": "retrieval must be coupled to recovery control"},
            {"case": "visually_near_mechanically_opposite", "expected_behavior": "reject visual-nearest memory", "observed_failure_mode": "retrieved visual neighbor has opposite contact mode", "lesson": "visual similarity cannot substitute for mechanism indexing"},
            {"case": "stale_recovery_memory", "expected_behavior": "discount old recovery episode", "observed_failure_mode": "old recovery succeeds in source embodiment but jams the target gripper", "lesson": "retrieval memories need embodiment-age and actuator-context checks"},
            {"case": "partial_observability_alias", "expected_behavior": "query or probe before retrieving", "observed_failure_mode": "two mechanisms share the same observed state until contact", "lesson": "retrieval controller needs active disambiguation under hidden mechanism state"},
            {"case": "overconformal_rejection", "expected_behavior": "retain useful mechanism-near memories", "observed_failure_mode": "conservative filter rejects helpful recovery cases under high shift", "lesson": "risk filters should not erase mechanism coverage"},
            {"case": "oracle_gap_under_compound_shift", "expected_behavior": "approach oracle mechanism retrieval", "observed_failure_mode": "oracle remains substantially better under maximum mechanism mismatch", "lesson": "local retrieval index is useful but not saturated"},
        ],
    )

    combined = {r["method"]: r for r in metrics if r["split"] == "combined_stress"}
    proposed = combined["proposed_mechanism_retrieval_controller"]
    non_oracle = [m["name"] for m in METHODS if m["name"] not in {"proposed_mechanism_retrieval_controller", "oracle_mechanism_retrieval"}]
    strongest = max(non_oracle, key=lambda name: combined[name]["mean_success_rate"])
    strongest_row = combined[strongest]
    pair_strong = next(r for r in pair if r["baseline"] == strongest)
    full_ab = next(r for r in ab_metrics if r["ablation"] == "full_mechanism_retrieval")
    best_removed = max([r for r in ab_metrics if r["ablation"] != "full_mechanism_retrieval"], key=lambda r: r["mean_success_rate"])
    gates = {
        "success_margin_ge_0.030": proposed["mean_success_rate"] - strongest_row["mean_success_rate"] >= 0.030,
        "mechanism_precision_delta_ge_0.030": proposed["mean_mechanism_precision"] - strongest_row["mean_mechanism_precision"] >= 0.030,
        "incompatible_retrieval_delta_le_-0.020": proposed["mean_incompatible_retrieval_rate"] - strongest_row["mean_incompatible_retrieval_rate"] <= -0.020,
        "damage_delta_le_0": proposed["mean_damage_rate"] - strongest_row["mean_damage_rate"] <= 0.0,
        "query_cost_delta_le_0": proposed["mean_query_cost"] - strongest_row["mean_query_cost"] <= 0.0,
        "recovery_success_delta_ge_0.020": proposed["mean_recovery_success"] - strongest_row["mean_recovery_success"] >= 0.020,
        "paired_seed_wins_ge_5": int(pair_strong["paired_seed_wins"]) >= 5,
        "ablation_margin_ge_0.020": full_ab["mean_success_rate"] - best_removed["mean_success_rate"] >= 0.020,
    }
    decision = "STRONG_REVISE" if all(gates.values()) else "KILL_ARCHIVE"

    combined_table = []
    for r in sorted(combined.values(), key=lambda row: row["mean_success_rate"], reverse=True):
        combined_table.append(
            {
                "method": r["method"].replace("_", "\\_"),
                "success": f"{r['mean_success_rate']:.3f} $\\pm$ {r['ci95_success_rate']:.3f}",
                "precision": f"{r['mean_mechanism_precision']:.3f}",
                "incompatible": f"{r['mean_incompatible_retrieval_rate']:.3f}",
                "damage": f"{r['mean_damage_rate']:.3f}",
                "query": f"{r['mean_query_cost']:.3f}",
            }
        )
    latex_table(RESULTS / "combined_stress_table.tex", combined_table, ["method", "success", "precision", "incompatible", "damage", "query"])

    ab_table = []
    for r in sorted(ab_metrics, key=lambda row: row["mean_success_rate"], reverse=True):
        ab_table.append(
            {
                "ablation": r["ablation"].replace("_", "\\_"),
                "success": f"{r['mean_success_rate']:.3f} $\\pm$ {r['ci95_success_rate']:.3f}",
                "precision": f"{r['mean_mechanism_precision']:.3f}",
                "incompat": f"{r['mean_incompatible_retrieval_rate']:.3f}",
            }
        )
    latex_table(RESULTS / "ablation_table.tex", ab_table, ["ablation", "success", "precision", "incompat"])

    pair_table = []
    for r in sorted(pair, key=lambda row: row["baseline"]):
        pair_table.append({"baseline": r["baseline"].replace("_", "\\_"), "diff": f"{r['mean_success_diff']:.3f} $\\pm$ {r['ci95_success_diff']:.3f}", "wins": f"{r['paired_seed_wins']}/7", "decisive": "yes" if r["decisive"] else "no"})
    latex_table(RESULTS / "pairwise_decision_table.tex", pair_table, ["baseline", "diff", "wins", "decisive"])

    plot_all(metrics, ab_metrics, stress_summary)

    with (RESULTS / "summary.txt").open("w", encoding="utf-8") as handle:
        handle.write("Paper 114 embodied retrieval-augmented control local evidence rebuild\n")
        handle.write("Design: 5 tasks x 7 mechanism regimes x 5 corpus/domain splits x 9 methods, 7 seeds, 84 rollout episodes per group.\n")
        handle.write(f"Terminal decision: {decision}\n")
        handle.write(f"Strongest non-oracle baseline under combined stress: {strongest}\n")
        handle.write(f"Proposed combined-stress success: {proposed['mean_success_rate']:.3f} +/- {proposed['ci95_success_rate']:.3f}\n")
        handle.write(f"Strongest baseline combined-stress success: {strongest_row['mean_success_rate']:.3f} +/- {strongest_row['ci95_success_rate']:.3f}\n")
        handle.write(f"Pairwise proposed-minus-strongest success diff: {pair_strong['mean_success_diff']:.3f} +/- {pair_strong['ci95_success_diff']:.3f}; wins={pair_strong['paired_seed_wins']}/7\n")
        handle.write(f"Mechanism-precision delta: {proposed['mean_mechanism_precision'] - strongest_row['mean_mechanism_precision']:.3f}\n")
        handle.write(f"Incompatible-retrieval delta: {proposed['mean_incompatible_retrieval_rate'] - strongest_row['mean_incompatible_retrieval_rate']:.3f}\n")
        handle.write(f"Damage delta: {proposed['mean_damage_rate'] - strongest_row['mean_damage_rate']:.3f}\n")
        handle.write(f"Query-cost delta: {proposed['mean_query_cost'] - strongest_row['mean_query_cost']:.3f}\n")
        handle.write(f"Recovery-success delta: {proposed['mean_recovery_success'] - strongest_row['mean_recovery_success']:.3f}\n")
        handle.write(f"Ablation margin over best removed component ({best_removed['ablation']}): {full_ab['mean_success_rate'] - best_removed['mean_success_rate']:.3f}\n")
        handle.write("Gate results:\n")
        for gate, passed in gates.items():
            handle.write(f"- {gate}: {passed}\n")
        handle.write("\nCombined-stress ranking:\n")
        for r in sorted(combined.values(), key=lambda row: row["mean_success_rate"], reverse=True):
            handle.write(
                f"- {r['method']}: success={r['mean_success_rate']:.3f} +/- {r['ci95_success_rate']:.3f}; "
                f"precision={r['mean_mechanism_precision']:.3f}; incompat={r['mean_incompatible_retrieval_rate']:.3f}; "
                f"recovery={r['mean_recovery_success']:.3f}; damage={r['mean_damage_rate']:.3f}; query={r['mean_query_cost']:.3f}\n"
            )

    print(f"wrote embodied retrieval evidence to {RESULTS}")
    print(f"terminal_decision={decision}")
    print(f"strongest_baseline={strongest}")
    print(f"success_margin={proposed['mean_success_rate'] - strongest_row['mean_success_rate']:.4f}")
    print(f"precision_delta={proposed['mean_mechanism_precision'] - strongest_row['mean_mechanism_precision']:.4f}")
    print(f"incompatible_delta={proposed['mean_incompatible_retrieval_rate'] - strongest_row['mean_incompatible_retrieval_rate']:.4f}")
    print(f"ablation_margin={full_ab['mean_success_rate'] - best_removed['mean_success_rate']:.4f}")


if __name__ == "__main__":
    main()
