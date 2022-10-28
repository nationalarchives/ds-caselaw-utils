# Caselaw utility functions

pypi name: [ds-caselaw-utils](https://pypi.org/project/ds-caselaw-utils)
python import name: `ds_caselaw_utils`

This repo contains functions of general use throughout the National Archives Caselaw project
so that we can have a single point of truth potentially across many repositories.

## Examples

```
from ds_caselaw_utils import neutral_url
neutral_url("[2022] EAT 1")  # '/eat/2022/4'

from ds_caselaw_utils import courts

courts.get_all() # return a list of all courts

courts.get_by_param("ewhc/ch") # get a court by its parameter value

courts.get_selectable() # returns a list of all courts that are whitelisted to
                        # appear as searchable options

courts.get_listable_groups() # returns a grouped list of courts that are whitelisted to
                             # be listed publicly

courts.get_listable_courts() # returns a list of all *courts* (ie not tribunals)
                             # which are whitelisted to be listed publicly

courts.get_listable_tribunals() # return a list of all *tribunals*  which are
                                # whitelisted to be listed publicly


```

The list of courts is defined in `src/ds_caselaw_utils/data/court_names.yml`. The format is as follows:

```
- name: high_court # Internal name of a group of courts to be displayed together
  display_name: "High Court" # An optional public facing name for this group.
  is_tribunal: false # Whether this group contains courts or tribunals
  courts: # List of courts to be displayed under this group
    -
        # An internal code for this court:
        code: EWHC-SeniorCourtsCosts
         # The public facing name of the court:
        name: Senior Courts Costs Office
        # An alternative wording for use in listings (optional, defaults to `name`)
        list_name: High Court (Senior Court Costs Office)
        # A URL to link to for more information on this court:
        link: https://www.gov.uk/courts-tribunals/senior-courts-costs-office
        # A regex matching neutral citations for this court's judgments:
        ncn: \[(\d{4})\] (EWHC) (\d+) \((SCCO)\)
        # The canonical parameter value used in searches for this court:
        param: 'ewhc/scco'
        # Any additional parameter aliases which display judgments from this court:
        extra_params: ['ewhc/costs']
        # The year of the first judgment we have on file for this court:
        start_year: 2003
        # The year of the last judgment we have on file for this court
        # (optional, defaults to current year):
        end_year: ~
        # Whether to expose this court publicly as selectable in search filters:
        selectable: true
        # Whether to expose this court publicly in listings:
        listable: true
```

## Testing

```bash
$ poetry shell
$ cd src/ds_caselaw_utils
$ python -m unittest
```

## Building

```bash
$ rm -rf dist
$ poetry build
$ python3 -m twine upload --repository testpypi dist/* --verbose
```

## Releasing

When making a new release, update the [changelog](CHANGELOG.md) in the release
pull request.

The package will **only** be released to PyPI if the branch is tagged. A merge
to main alone will **not** trigger a release to PyPI.

To create a release:

0. Update the version number in `pyproject.toml`
1. Create a branch `release/v{major}.{minor}.{patch}`
2. Update changelog for the release
3. Commit and push
4. Open a PR from that branch to main
5. Get approval on the PR
6. Tag the HEAD of the PR `v{major}.{minor}.{patch}` and push the tag
7. Merge the PR to main and push
