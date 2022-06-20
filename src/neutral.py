"""
Convert neutral Citations to URL
"""

import re

match_data = {
    # fmt: off
    r"^\[(\d{4})\] (UKSC|UKPC) (\d+)$": [2, 1, 3],
    r"^\[(\d{4})\] (EWCA) (Civ|Crim) (\d+)$": [2, 3, 1, 4],
    r"^\[(\d{4})\] (EWHC) (\d+) \((Admin|Admlty|Ch|Comm|Costs|Fam|IPEC|Pat|QB|SCCO|TCC)\)$": [2, 4, 1, 3],  # noqa: E501
    r"^\[(\d{4})\] (EWFC|EWCOP) (\d+)$": [2, 1, 3],
    r"^\[(\d{4})\] (UKUT) (\d+) \((AAC|IAC|LC|TCC)\)$": [2, 4, 1, 3],
    r"^\[(\d{4})\] (EAT) (\d+)$": [2, 1, 3],
    r"^\[(\d{4})\] (UKFTT) (\d+) \((TC)\)$": [2, 4, 1, 3],
    # fmt: on
}


def neutral_url(citation):
    for regex, groups in match_data.items():
        if match := re.match(regex, citation):
            url_components = "/".join([match.groups()[x - 1] for x in groups])
            return f"/{url_components}".lower()
    return None

while True:
    citation = input()
    print(neutral_url(citation))
