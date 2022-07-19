"""
Convert neutral Citations to URL
"""

import re

from ruamel.yaml import YAML

yaml = YAML()
with open("data/neutral_citation_regex.yaml") as f:
    citation_data = yaml.load(f)


def neutral_url(citation):
    for regex, groups in citation_data:
        if match := re.match(regex, citation):
            url_components = "/".join([match.groups()[x - 1] for x in groups])
            return f"/{url_components}".lower()
    return None
