# Caselaw utility functions

pypi name: [ds-caselaw-utils](https://pypi.org/project/ds-caselaw-utils)
python import name: `ds_caselaw_utils`

This repo contains functions of general use throughout the National Archives Caselaw project
so that we can have a single point of truth potentially across many repositories.

## Examples

```
from ds_caselaw_utils import neutral_url
neutral_url("[2022] EAT 1")  # '/eat/2022/4'
```

## Testing

```bash
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
