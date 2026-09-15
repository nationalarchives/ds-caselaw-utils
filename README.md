# The National Archives: Find Case Law

This repository is part of the [Find Case Law](https://caselaw.nationalarchives.gov.uk/) project at [The National Archives](https://www.nationalarchives.gov.uk/). For more information on the project, check [the documentation](https://github.com/nationalarchives/ds-find-caselaw-docs).

# Python Utilities

![PyPI](https://img.shields.io/pypi/v/ds-caselaw-utils) ![Libraries.io dependency status for latest release](https://img.shields.io/librariesio/release/pypi/ds-caselaw-utils)

This repository predominantly contains information about [the courts in the Find Case Law project](courts.md).

pypi name: [ds-caselaw-utils](https://pypi.org/project/ds-caselaw-utils)
python import name: `ds_caselaw_utils`

## Examples

```python
from ds_caselaw_utils import neutral_url
neutral_url("[2022] EAT 1")  # '/eat/2022/4'

from ds_caselaw_utils import courts

courts.get_all() # return a list of all courts

courts.get_by_param("ewhc/ch") # get a court by its parameter value

courts.get_show_in_search_filters() # returns a list of all courts that appear as
                        # searchable options

courts.get_show_in_search_filters_groups() # returns a grouped list of all courts and tribunals
                               # that appear as search-filter options

courts.get_grouped_show_in_search_filters_courts() # returns show_in_search_filters courts grouped for display

courts.get_grouped_show_in_search_filters_tribunals() # returns show_in_search_filters tribunals grouped for display

courts.get_show_in_public_directory() # returns a list of courts included in the public directory

courts.get_show_in_public_directory_groups() # returns public-directory courts grouped by category

courts.get_grouped_show_in_public_directory_courts() # returns public-directory courts grouped for display

courts.get_grouped_show_in_public_directory_tribunals() # returns public-directory tribunals grouped for display

courts.get_show_to_editors_groups() # returns a grouped list of courts visible to editors

courts.get_grouped_show_to_editors_courts() # returns courts visible to editors grouped for display

courts.get_grouped_show_to_editors_tribunals() # returns tribunals visible to editors grouped for display

courts.get_show_to_editors_courts() # returns a list of all *courts* (ie not tribunals)
                             # visible to editors

courts.get_show_to_editors_tribunals() # returns a list of all *tribunals* visible to editors
```

The list of courts is defined in `src/ds_caselaw_utils/data/court_names.yml`. The format is as follows:

```yaml
- name: high_court # Internal name of a group of courts to be displayed together
  display_name: "High Court" # An optional public facing name for this group.
  is_tribunal: false # Whether this group contains courts or tribunals
  courts: # List of courts to be displayed under this group
    - # An internal code for this court:
      code: EWHC-SeniorCourtsCosts
      # The public facing name of the court:
      name: High Court (Senior Courts Costs Office)
      # An optional alternative wording for use when displayed in grouped format (defaults to 'name'):
      grouped_name: Senior Court Costs Office
      # A URL to link to for more information on this court:
      link: https://www.gov.uk/courts-tribunals/senior-courts-costs-office
      # A regex matching neutral citations for this court's judgments:
      ncn: \[(\d{4})\] (EWHC) (\d+) \((SCCO)\)
      # The canonical parameter value used in searches for this court:
      param: "ewhc/scco"
      # Any additional parameter aliases which display judgments from this court:
      extra_params: ["ewhc/costs"]
      # The year of the first judgment we have on file for this court:
      start_year: 2003
      # The year of the last judgment we have on file for this court
      # (optional, defaults to current year):
      end_year: ~
      # Whether this court appears as an option in search filters:
      show_in_search_filters: true
      # Whether to include this court in the public directory:
      show_in_public_directory: true
      # Whether this court is visible to editors:
      show_to_editors: true
      # Whether this court has ended yet
      ended: false
      # Whether this court is a court of record (optional):
      court_of_record: true
```

## Requirements

The environment you develop this repo in requires the following to be installed:

- `python 3.12` (as the project is pinned to python 3.12)
- `poetry` (as this is used for depdenency management and virtual environment management)
- `pre-commit` (to install git hooks defined in `.pre-commit-config.yaml`)

## Getting set up

- Run `pre-commit install` inside the root directory of the repo to install the git hooks defined in `.pre-commit-config.yaml`.

```bash
$ poetry shell
$ poetry install
```

## Testing

While in a poetry shell:

```bash
$ poetry run pytest
```

## Building

```bash
$ rm -rf dist
$ poetry build
$ python3 -m twine upload --repository testpypi dist/* --verbose
```

## Release process

<!-- last_review: 2026-04-14 -->

When making a new release, update the [changelog](CHANGELOG.md) in the release
pull request.

The package will **only** be released to PyPI if a new tag is created. A merge
to main alone will **not** trigger a release to PyPI.

If the release fails to push to PyPI, you can delete the tag with `git pull`, `git push --delete origin v1.2.3` and try again.

To create a release:

0. Update the version number in `pyproject.toml`
1. Create a branch `release/v{major}.{minor}.{patch}`
2. Update `CHANGELOG.md` and `pyproject.toml` for the release
3. Commit and push
4. Open a PR from that branch to main
5. Get approval on the PR
6. Tag the HEAD of the PR `v{major}.{minor}.{patch}` and push the tag
7. Merge the PR to main and push
8. Add a new release to Github for that tag for consistency's sake
