import statistics


def derive_behaviour_signals(events):
    """
    Derives illustrative runtime behaviour signals
    from a single execution trace.

    These signals are heuristic and demo-only.
    """

    token_events = [
        e for e in events
        if e.type == "token_observed"
    ]

    if len(token_events) < 2:
        return {
            "signal_mode": "demo",
            "derived_from": "single_execution",
            "behaviour_state": "stable"
        }

    elapsed_times = [
        e.data.get("elapsed", 0)
        for e in token_events
    ]

    # latency deviation (relative variance)
    mean_latency = statistics.mean(elapsed_times)
    stdev_latency = statistics.pstdev(elapsed_times)

    latency_deviation_percent = (
        (stdev_latency / mean_latency) * 100
        if mean_latency > 0 else 0
    )

    # generation pacing
    pacing = (
        "irregular"
        if latency_deviation_percent > 10
        else "regular"
    )

    # structural consistency (very rough heuristic)
    structural_consistency = (
        "high"
        if len(token_events) <= 20
        else "medium"
    )

    # output structure entropy (illustrative)
    unique_tokens = len(
        set(e.data.get("token") for e in token_events)
    )

    entropy = (
        "low"
        if unique_tokens / len(token_events) < 0.5
        else "medium"
    )

    behaviour_state = (
        "stable"
        if pacing == "regular"
        else "irregular"
    )

    return {
        "signal_mode": "demo",
        "derived_from": "single_execution",
        "latency_deviation_percent": round(latency_deviation_percent, 2),
        "generation_pacing": pacing,
        "structural_consistency": structural_consistency,
        "output_structure_entropy": entropy,
        "behaviour_state": behaviour_state
    }
