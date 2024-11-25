import pytest

from .neutral import neutral_url
from .types import NeutralCitationString


class TestNeutralURL:
    @pytest.mark.parametrize(
        "ncn, expected_uri",
        [
            ("[2022] UKSC 1", "uksc/2022/1"),
            ("[1604] EWCA Crim 555", "ewca/crim/1604/555"),
            ("[2022] EWHC 1 (Comm)", "ewhc/comm/2022/1"),
            ("[1999] EWCOP 7", "ewcop/1999/7"),
            ("[2022] UKUT 1 (IAC)", "ukut/iac/2022/1"),
            ("[2022] EAT 1", "eat/2022/1"),
            ("[2022] UKFTT 1 (TC)", "ukftt/tc/2022/1"),
            ("[2022] UKFTT 1 (GRC)", "ukftt/grc/2022/1"),
            ("[2022] EWHC 1 (KB)", "ewhc/kb/2022/1"),
            ("[2023] UKAIT 1", "ukait/2023/1"),
            ("[2024] EWCOP 17 (T2)", "ewcop/t2/2024/17"),
            ("[2000] UKIPTrib 99", "ukiptrib/2000/99"),
            ("[2000] EWCR 99", "ewcr/2000/99"),
        ],
    )
    def test_good_neutral_urls(self, ncn, expected_uri):
        assert neutral_url(NeutralCitationString(ncn)) == expected_uri

    @pytest.mark.parametrize(
        "ncn",
        [
            "",
            "1604] EWCA Crim 555",
            "[2022 EWHC 1 Comm",
            "[1999] EWCOP",
            "[2022] UKUT B1 IAC",  # Could be a Bailii reference, might want to drop B in future.
            "[2022] EAT A",
            "[2022] NOTACOURT 1 TC",
            "[2022] EWHC 1 (T2)",
            "[2000] EWCRC 99",
        ],
    )
    def test_bad_neutral_urls(self, ncn):
        assert neutral_url(NeutralCitationString(ncn)) is None
