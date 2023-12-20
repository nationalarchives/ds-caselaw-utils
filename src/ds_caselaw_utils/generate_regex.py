"""This utility creates neutral_citation_regex.yaml"""

from courts import courts


class ParsedURLPattern:
    def __init__(self, regex):
        self.regex = regex


class URLPatternParserError(RuntimeError):
    pass


def url_order(pattern_string: str) -> list[str]:
    builder = []
    pattern = split_ncn(pattern_string)
    for item in url_order_numbers(pattern_string):
        builder.append(pattern[item - 1])
    return builder


def split_ncn(pattern_string: str) -> list[str]:
    return pattern_string.split(" ")


def url_order_numbers(pattern_string: str) -> list[int]:
    pattern = split_ncn(pattern_string)
    if pattern[0] != year_regex:
        raise URLPatternParserError(
            f"Pattern {pattern_string} does not start with year"
        )

    if num_regex not in pattern:
        raise URLPatternParserError(
            f"Pattern {pattern_string} does not contain judgment number"
        )

    "the sub court is in the late position the judgment number is not."
    "Note: these are 1-indexed"

    num_position = pattern.index(num_regex) + 1
    if num_position == 4:
        subcourt_position = 3
    elif num_position == 3:
        if len(pattern) == 4:
            subcourt_position = 4
        else:
            subcourt_position = None
    else:
        raise URLPatternParserError(
            f"Did not expect judgment number at position {num_position}"
        )

    if subcourt_position:
        return [2, subcourt_position, 1, num_position]
    else:
        return [2, 1, 3]


year_regex = r"\[(\d{4})\]"
num_regex = r"(\d+)"

courtlist = courts.get_all()
url_patterns = sorted(list(set(court.ncn for court in courtlist if court.ncn)))

court_strings = set()
subcourt_strings = set()
for url_pattern in url_patterns:
    print(url_pattern, url_order_numbers(url_pattern), url_order(url_pattern))
    court_strings.add(url_pattern[0])

print(court_strings, subcourt_strings)
