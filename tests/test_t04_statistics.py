"""Statistics verification through the comparison boundary approved in T04."""

import pytest

from experiments.t04.statistics import BinarySample, FrozenRule, compare


def test_zero_success_keeps_uncertainty_and_percentage_point_direction():
    result = compare(BinarySample(0, 10), BinarySample(10, 10), independent=True)
    assert result.current_interval == pytest.approx((0, 0.2775327998628892))
    assert result.reference_interval == pytest.approx((0.7224672001371107, 1))
    assert result.difference_pp == -100
    assert result.method == "Wilson / Newcombe hybrid score"
    assert result.status == "insufficient_precision"


@pytest.mark.parametrize("successes,users", [(-1, 10), (11, 10), (0, -1), (0.5, 10), (True, 10), (1, 1.5)])
def test_invalid_counts_are_rejected(successes, users):
    with pytest.raises(ValueError):
        BinarySample(successes, users)


@pytest.mark.parametrize("quality,reason", [
    ({"complete": False}, "incomplete_collection"),
    ({"deduplicated": False}, "repeated_users"),
    ({"overlapping": True}, "overlapping_users"),
    ({"independent": False}, "independence_not_established"),
    ({"homogeneous": False}, "heterogeneous_or_clustered_structure"),
])
def test_unsupported_structures_keep_counts_but_suppress_intervals(quality, reason):
    result = compare(BinarySample(3, 10), BinarySample(6, 10), **{"independent": True, **quality})
    assert result.current.successes == 3
    assert result.difference_pp == -30
    assert result.difference_interval_pp is None
    assert result.current_interval is None
    assert result.status == "insufficient_evidence"
    assert result.reason == reason


def test_empty_is_not_zero_or_no_anomaly():
    result = compare(BinarySample(0, 0), BinarySample(10, 10), independent=True)
    assert result.current.rate is None
    assert result.difference_pp is None
    assert result.status == "insufficient_evidence"


def test_threshold_distinguishes_precision_ambiguity_and_no_anomaly():
    assert compare(BinarySample(500, 1000), BinarySample(500, 1000), independent=True).status == "below_anomaly_standard"
    assert compare(BinarySample(450, 1000), BinarySample(500, 1000), independent=True).status == "indeterminate"
    assert compare(BinarySample(300, 1000), BinarySample(500, 1000), independent=True).status == "anomaly_supported"
    increased = compare(BinarySample(700, 1000), BinarySample(500, 1000), independent=True,
                        rule=FrozenRule(direction="increase"))
    assert increased.status == "anomaly_supported"
    assert "no causal proof" in increased.limitation


def test_user_identity_validation_and_weighted_derived_values():
    from experiments.t04.statistics import compare_users, standardized

    result = compare_users([("a", True), ("a", True)], [("b", False)], independent=True)
    assert result.current.users == 1
    assert result.reason == "repeated_users"
    overlap = compare_users([("a", True)], [("a", False)], independent=True)
    assert overlap.reason == "overlapping_users"
    with pytest.raises(ValueError, match="Conflicting"):
        compare_users([("a", True), ("a", False)], [("b", True)], independent=True)
    derived = standardized({"Android": 1, "iOS": 1},
                           {"Android": BinarySample(30, 100), "iOS": BinarySample(90, 100)})
    assert derived["rate"] == pytest.approx(0.6)
    assert derived["interval"] is None
    assert derived["status"] == "descriptive_only"


@pytest.mark.parametrize("flag,value", [("independent", "yes"), ("complete", 1), ("deduplicated", None)])
def test_quality_attestations_require_boolean_values(flag, value):
    with pytest.raises(ValueError, match="boolean"):
        compare(BinarySample(1, 2), BinarySample(1, 2), **{flag: value})


def test_two_sided_rule_does_not_treat_zero_crossing_as_equivalence():
    uncertain = compare(BinarySample(50, 100), BinarySample(50, 100), independent=True,
                        rule=FrozenRule(direction="both", max_width_pp=30))
    assert uncertain.status == "indeterminate"
    precise = compare(BinarySample(5000, 10000), BinarySample(5000, 10000), independent=True,
                      rule=FrozenRule(direction="both"))
    assert precise.status == "below_anomaly_standard"
