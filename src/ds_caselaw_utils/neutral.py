"""
Convert neutral Citations to URL
"""

import pathlib
import re

from ruamel.yaml import YAML

yaml = YAML()
datafile = pathlib.Path(__file__).parent / "data/neutral_citation_regex.yaml"
with open(datafile) as f:
    citation_data = yaml.load(f)


def neutral_url(citation):
    """Given a neutral citation such as `[2020] EAT 17`,
    return a public-API URL like `/eat/2020/17`, or None
    if no match is found.
    """
    for regex, groups in citation_data:
        if match := re.match(regex, citation):
            url_components = "/".join([match.groups()[x - 1] for x in groups])
            return f"/{url_components}".lower()
    return None
