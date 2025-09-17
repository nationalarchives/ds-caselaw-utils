from re import compile

from .courts import courts
from .neutral import neutral_url
from .types import NeutralCitationString


def test_court_ncn_example_integrity():
    """Check that each court's example NCNs match that court's NCN pattern."""

    for court in courts.get_all():
        if (
            court.ncn_pattern and court.ncn_examples
        ):  # The schema for court data enforces both of these being present, but check anyway to prevent test issues
            pattern = compile(court.ncn_pattern)
            for ncn_example in court.ncn_examples:
                assert pattern.match(ncn_example)


def test_all_example_ncns_have_conversion_pattern():
    """Check that each example NCN in the court data will convert to a valid URL pattern."""

    for court in courts.get_all():
        if court.ncn_examples:
            for ncn_example in court.ncn_examples:
                assert neutral_url(NeutralCitationString(ncn_example))
