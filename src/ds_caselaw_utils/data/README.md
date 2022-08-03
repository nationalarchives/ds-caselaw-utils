## court_names

Court codes, human readable names and links for more information about the court.
Whilst there are regex for that court, it's worth noting that in some cases there isn't
a simple one-to-one mapping between Neutral Citation type and court -- some courts deal
with multiple Neutral Citation types, some Neutral Citation types are split amongst
multiple courts.

Not yet used anywhere.

## neutral_citation_regex

Used to transform neutral citations into Caselaw URLs. Used by neutral.py.

Reading the match_data:
`['^\[(\d{4})\] (EAT) (\d+)$', [2, 1, 3]]`
the components of the URL for `[2022] EAT 1` are the
2nd, 1st and 3rd components of the neutral citation, so the URL becomes `eat/2022/1`.
