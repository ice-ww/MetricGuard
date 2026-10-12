"""Scalar score intervals for explicitly independent Bernoulli samples.

Counts describe the observed snapshot. Intervals refer only to a declared latent
Bernoulli process, never to the correctness of the snapshot or to causal effects.
"""

from dataclasses import dataclass
from math import hypot, isfinite, sqrt
from statistics import NormalDist
from typing import Any


@dataclass(frozen=True)
class BinarySample:
    successes: int
    users: int

    def __post_init__(self) -> None:
        if type(self.successes) is not int or type(self.users) is not int:
            raise ValueError("Counts must be integers, excluding booleans")
        if self.users < 0 or not 0 <= self.successes <= self.users:
            raise ValueError("Require 0 <= successes <= users")

    @property
    def rate(self) -> float | None:
        return self.successes / self.users if self.users else None


@dataclass(frozen=True)
class FrozenRule:
    version: str = "t04-v1"
    threshold_pp: float = 5.0
    max_width_pp: float = 20.0
    direction: str = "decrease"

    def __post_init__(self) -> None:
        if (not isfinite(self.threshold_pp) or not 0 < self.threshold_pp <= 100
                or not isfinite(self.max_width_pp) or not 0 < self.max_width_pp <= 200
                or self.direction not in {"decrease", "increase", "both"}):
            raise ValueError("Invalid decision rule")


@dataclass(frozen=True)
class Comparison:
    current: BinarySample
    reference: BinarySample
    difference_pp: float | None
    current_interval: tuple[float, float] | None
    reference_interval: tuple[float, float] | None
    difference_interval_pp: tuple[float, float] | None
    status: str
    reason: str
    rule: FrozenRule
    confidence: float = 0.95
    method: str = "Wilson / Newcombe hybrid score"
    limitation: str = ("Exploratory nominal 95% interval for one prespecified comparison under "
                       "independent homogeneous Bernoulli sampling. No adaptive-selection correction; "
                       "no 95% guarantee for a selected diagnosis and no causal proof.")


def _wilson(sample: BinarySample) -> tuple[float, float]:
    z = NormalDist().inv_cdf(0.975)
    n, p = sample.users, sample.successes / sample.users
    denominator = 1 + z*z/n
    center = (p + z*z/(2*n)) / denominator
    half = z * sqrt(p*(1-p)/n + z*z/(4*n*n)) / denominator
    return max(0.0, center-half), min(1.0, center+half)


def compare(current: BinarySample, reference: BinarySample, *, independent: bool = False,
            complete: bool = True, deduplicated: bool = True, overlapping: bool = False,
            homogeneous: bool = True, rule: FrozenRule = FrozenRule()) -> Comparison:
    """Caller must establish independence, deduplication and source completeness.

    Unknown independence fails closed. These flags are an explicit integration
    contract, not a proof inferred from aggregate counts. No intervals for repeated,
    overlapping, clustered or heterogeneous unsupported structures.
    """
    if any(type(flag) is not bool for flag in (independent, complete, deduplicated, overlapping, homogeneous)):
        raise ValueError("Quality attestations must be boolean")
    a, b = current.rate, reference.rate
    difference = 100*(a-b) if a is not None and b is not None else None
    reason = next((message for valid, message in (
        (complete, "incomplete_collection"), (deduplicated, "repeated_users"),
        (not overlapping, "overlapping_users"), (independent, "independence_not_established"),
        (homogeneous, "heterogeneous_or_clustered_structure"),
        (bool(current.users and reference.users), "empty_sample")) if not valid), None)
    if reason:
        return Comparison(current, reference, difference, None, None, None,
                          "insufficient_evidence", reason, rule)
    assert a is not None and b is not None
    aci, bci = _wilson(current), _wilson(reference)
    delta = a-b
    lower = 100*(delta-hypot(a-aci[0], bci[1]-b))
    upper = 100*(delta+hypot(aci[1]-a, b-bci[0]))
    if upper-lower > rule.max_width_pp:
        status, detail = "insufficient_precision", "interval_exceeds_frozen_width"
    else:
        threshold = rule.threshold_pp
        if rule.direction == "decrease":
            abnormal, below = upper < -threshold, lower > -threshold
        elif rule.direction == "increase":
            abnormal, below = lower > threshold, upper < threshold
        else:
            abnormal = upper < -threshold or lower > threshold
            below = lower > -threshold and upper < threshold
        status = "anomaly_supported" if abnormal else "below_anomaly_standard" if below else "indeterminate"
        detail = "interval_vs_frozen_business_threshold"
    return Comparison(current, reference, difference, aci, bci, (lower, upper), status, detail, rule)


def compare_users(current: list[tuple[str, bool]], reference: list[tuple[str, bool]], *,
                  independent: bool = False, complete: bool = True, homogeneous: bool = True,
                  rule: FrozenRule = FrozenRule()) -> Comparison:
    """Validate user-level observations before deciding interval applicability."""
    samples: list[dict[str, bool]] = []
    for observations in (current, reference):
        unique: dict[str, bool] = {}
        for identity, success in observations:
            if not isinstance(identity, str) or not identity or type(success) is not bool:
                raise ValueError("Require nonempty user IDs and binary boolean outcomes")
            if identity in unique and unique[identity] != success:
                raise ValueError("Conflicting outcomes for one user")
            unique[identity] = success
        samples.append(unique)
    a, b = samples
    return compare(BinarySample(sum(a.values()), len(a)), BinarySample(sum(b.values()), len(b)),
                   independent=independent, complete=complete, homogeneous=homogeneous,
                   deduplicated=len(a) == len(current) and len(b) == len(reference),
                   overlapping=bool(a.keys() & b.keys()), rule=rule)


def standardized(base_users: dict[str, int], current: dict[str, BinarySample]) -> dict[str, Any]:
    """A4 point estimate only; never encode weighted rates as binomial counts."""
    if not base_users or base_users.keys() != current.keys():
        raise ValueError("Identical nonempty strata required")
    if any(type(n) is not int or n < 0 for n in base_users.values()):
        raise ValueError("Nonnegative integer baseline counts required")
    total = sum(base_users.values())
    unavailable = not total or any(base_users[key] and not sample.users for key, sample in current.items())
    rate = None if unavailable else sum(base_users[key] / total * (sample.rate or 0)
                                       for key, sample in current.items())
    return {"rate": rate, "interval": None,
            "status": "insufficient_evidence" if unavailable else "descriptive_only",
            "reason": "weighted_derived_quantity_has_no_validated_interval"}
