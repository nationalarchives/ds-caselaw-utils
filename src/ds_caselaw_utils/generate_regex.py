"""This utility creates neutral_citation_regex.yaml"""

from courts import courts

year_regex = r"\[(\d{4})\]"
num_regex = r"(\d+)"


class URLPatternParserError(RuntimeError):
    pass


class ParsedURLPattern:
    def __init__(self, regex: str):
        self.regex = regex
        self.pattern = regex.split(" ")

    @property
    def court(self):
        return self.url_order[0].strip("()")

    @property
    def subcourt(self):
        if len(self.pattern) != 4:
            return None
        return self.url_order[1].strip(r"()\\")

    @property
    def url_order(self) -> list[str]:
        return [self.pattern[item - 1] for item in self.url_order_numbers]

    @property
    def url_order_numbers(self) -> list[int]:
        if self.pattern[0] != year_regex:
            raise URLPatternParserError(
                f"Pattern {self.regex} does not start with year"
            )

        if num_regex not in self.pattern:
            raise URLPatternParserError(
                f"Pattern {self.regex} does not contain judgment number"
            )

        "the sub court is in the late position the judgment number is not."
        "Note: these are 1-indexed"

        num_position = self.pattern.index(num_regex) + 1
        if num_position == 4:
            subcourt_position = 3
        elif num_position == 3:
            if len(self.pattern) == 4:
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


def all_patterns() -> list[ParsedURLPattern]:
    url_patterns = [court.ncn for court in courts.get_all() if court.ncn]
    for url_pattern in url_patterns:
        pattern = ParsedURLPattern(url_pattern)
        print(pattern.regex, pattern.url_order_numbers, pattern.url_order)
        yield pattern


def all_court_regex():
    return "|".join({pattern.court for pattern in all_patterns()})


def all_subcourt_regex():
    return "|".join(
        {pattern.subcourt for pattern in all_patterns() if pattern.subcourt}
    )


print(all_court_regex(), all_subcourt_regex())
