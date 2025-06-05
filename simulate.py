"""
simulate.py – Monte-Carlo economics for DoorDash New Verticals.
Usage:
    from simulate import run_scenario
    run_scenario(clat_boost=0.02, inventory_boost=0.05)
"""
from __future__ import annotations
import numpy as np
from dataclasses import dataclass

@dataclass
class Params:
    n_orders: int = 13_085
    p_late: float = 0.048
    p_miss: float = 0.062
    clat_boost: float = 0.0
    inventory_boost: float = 0.0
    value_per_order: float = 27.5
    refund_rate: float = 0.45

def simulate_once(p: Params) -> dict[str, float]:
    rng = np.random.default_rng()
    late = rng.random(p.n_orders) < (p.p_late - p.clat_boost)
    miss = rng.random(p.n_orders) < (p.p_miss - p.inventory_boost)
    refund_cost = miss.mean() * p.value_per_order * p.refund_rate * p.n_orders
    return {
        "on_time_rate": 1 - late.mean(),
        "refund_cost": refund_cost,
        "net_gmv": p.value_per_order * p.n_orders - refund_cost,
    }

def run_scenario(runs: int = 10_000, **kwargs) -> dict[str, float]:
    p = Params(**kwargs)
    outs = np.array([list(simulate_once(p).values()) for _ in range(runs)])
    return dict(zip(["on_time_rate", "refund_cost", "net_gmv"], outs.mean(0)))
