"""External software is the oracle, never the implementation's private helpers."""

from itertools import product

import pytest
from statsmodels.stats.proportion import confint_proportions_2indep, proportion_confint

from experiments.t04.statistics import BinarySample, compare


CASES = [(0, 1), (1, 1), (0, 10), (10, 10), (1, 2), (1, 10000), (9999, 10000), (40, 100)]


@pytest.mark.parametrize("current,reference", list(product(CASES, CASES)))
def test_intervals_match_independent_statsmodels_reference(current, reference):
    result = compare(BinarySample(*current), BinarySample(*reference), independent=True)
    assert result.current_interval == pytest.approx(proportion_confint(*current, alpha=0.05, method="wilson"), abs=1e-12)
    expected = confint_proportions_2indep(*current, *reference, method="newcomb", compare="diff", alpha=0.05)
    assert result.difference_interval_pp == pytest.approx(tuple(float(v)*100 for v in expected), abs=1e-10)
    assert result.difference_interval_pp[0] <= result.difference_pp <= result.difference_interval_pp[1]
