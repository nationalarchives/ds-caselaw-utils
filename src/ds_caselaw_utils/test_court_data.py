from re import compile

from .courts import courts


def test_court_ncn_example_integrity():
    """Check that each court's example NCNs match that court's NCN pattern."""

    for court in courts.get_all():
        if (
            court.ncn_pattern and court.ncn_examples
        ):  # The schema for court data enforces both of these being present, but check anyway to prevent test issues
            pattern = compile(court.ncn_pattern)
            for ncn_example in court.ncn_examples:
                assert pattern.match(ncn_example)
