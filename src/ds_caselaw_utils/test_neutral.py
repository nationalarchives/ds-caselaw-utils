import unittest

from .neutral import neutral_url
from .types import NeutralCitationString


class TestNeutralURL(unittest.TestCase):
    def test_good_neutral_urls(self):
        self.assertEqual(neutral_url(NeutralCitationString("[2022] UKSC 1")), "/uksc/2022/1")
        self.assertEqual(neutral_url(NeutralCitationString("[1604] EWCA Crim 555")), "/ewca/crim/1604/555")
        self.assertEqual(neutral_url(NeutralCitationString("[2022] EWHC 1 (Comm)")), "/ewhc/comm/2022/1")
        self.assertEqual(neutral_url(NeutralCitationString("[1999] EWCOP 7")), "/ewcop/1999/7")
        self.assertEqual(neutral_url(NeutralCitationString("[2022] UKUT 1 (IAC)")), "/ukut/iac/2022/1")
        self.assertEqual(neutral_url(NeutralCitationString("[2022] EAT 1")), "/eat/2022/1")
        self.assertEqual(neutral_url(NeutralCitationString("[2022] UKFTT 1 (TC)")), "/ukftt/tc/2022/1")
        self.assertEqual(neutral_url(NeutralCitationString("[2022] UKFTT 1 (GRC)")), "/ukftt/grc/2022/1")
        self.assertEqual(neutral_url(NeutralCitationString("[2022] EWHC 1 (KB)")), "/ewhc/kb/2022/1")
        self.assertEqual(neutral_url(NeutralCitationString("[2023] UKAIT 1")), "/ukait/2023/1")
        self.assertEqual(neutral_url(NeutralCitationString("[2024] EWCOP 17 (T2)")), "/ewcop/t2/2024/17")
        self.assertEqual(neutral_url(NeutralCitationString("[2000] UKIPTrib 99")), "/ukiptrib/2000/99")
        self.assertEqual(neutral_url(NeutralCitationString("[2000] EWCR 99")), "/ewcr/2000/99")
        self.assertEqual(neutral_url(NeutralCitationString("[2000] EWCC 99")), "/ewcc/2000/99")

    def test_bad_neutral_urls(self):
        self.assertEqual(neutral_url(NeutralCitationString("")), None)
        self.assertEqual(neutral_url(NeutralCitationString("1604] EWCA Crim 555")), None)
        self.assertEqual(neutral_url(NeutralCitationString("[2022 EWHC 1 Comm")), None)
        self.assertEqual(neutral_url(NeutralCitationString("[1999] EWCOP")), None)
        self.assertEqual(
            neutral_url(NeutralCitationString("[2022] UKUT B1 IAC")), None
        )  # Could be a Bailii reference, might want to drop B in future.
        self.assertEqual(neutral_url(NeutralCitationString("[2022] EAT A")), None)
        self.assertEqual(neutral_url(NeutralCitationString("[2022] NOTACOURT 1 TC")), None)
        self.assertEqual(neutral_url(NeutralCitationString("[2022] EWHC 1 (T2)")), None)
        self.assertEqual(neutral_url(NeutralCitationString("[2000] EWCRC 99")), None)
