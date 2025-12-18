# Parser metadata output checker

If you want to check that any particular `metadata.json` output from the parser (either directly or via TRE) matches the specification then you can put the file into this folder and run `check_examples`.

## Dependencies

`check_examples` uses [check-jsonschema](https://github.com/python-jsonschema/check-jsonschema), which must be available on your command line.
