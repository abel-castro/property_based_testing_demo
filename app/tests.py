import pytest
from hypothesis_auto import auto_pytest_magic

from hypothesis import example, given, settings, strategies, Verbosity

from app.main import sum_simple, sum_buggy, sum_typed


@pytest.mark.parametrize(
    "num_1, num_2, expected",
    [(3, 5, 8), (-2, -2, -4), (-1, 5, 4), (3, -5, -2), (0, 5, 5)],
)
def test__sum_simple__with_parametrize(num_1, num_2, expected):
    """
    Test sum_simple using parametrize.

    How exhaustive are the cases depends mostly on the person writing the tests.
    """
    assert sum_simple(num_1, num_2) == expected


@settings(verbosity=Verbosity.verbose)
@given(strategies.integers(), strategies.integers())
@example(1, 2)
def test__sum_simple__with_hypothesis(num_1, num_2):
    """
    Test sum_simple using hypothesis-strategies.

    This creates more robust cases but also implicates that we know
    the arguments num_1 and num_2 are integers.

    @example ensures the test-case runs with num_1=1, and num_2=2
    """
    assert sum_simple(num_1, num_2) == num_1 + num_2


@pytest.mark.parametrize(
    "num_1, num_2, expected",
    [(3, 5, 8), (-2, -2, -4), (-1, 5, 4), (3, -5, -2), (0, 5, 5)],
)
def test__sum_buggy__with_parametrize(num_1, num_2, expected):
    """
    Test sum_buggy using parametrize.

    With parametrize looks like the sum_buggy really adds
    num_1 and num_2.
    """
    assert sum_buggy(num_1, num_2) == expected


@settings(verbosity=Verbosity.verbose)
@given(strategies.integers(), strategies.integers())
@pytest.mark.xfail(reason="Buggy logic causes fail.")
def test__sum_buggy__with_hypothesis(num_1, num_2):
    """
    Test sum_buggy using hypothesis-strategies.

    The buggy logic in sum_buggy causes fails.
    """
    assert sum_buggy(num_1, num_2) == num_1 + num_2


auto_pytest_magic(sum_typed, auto_runs_=100)
"""
This auto-generates 100 test cases (default_amount is 50) based on the
type annotations of the function sum_typed.
"""
