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

```python -m unittest```

## Building

```
rm -rf dist
poetry build
python3 -m twine upload --repository testpypi dist/* --verbose ```

(Use `pypi` once happy)
(There's probably a way to do the last step with just poetry)
