# Changelog

All notable changes to this project will be documented in this file.

## v2.7.0 (2025-08-26)

### Feat

- support Land Registry (PC) NCNs

## v2.6.0 (2025-08-18)

### Feat

- Add Land Registration Division (Property Chamber) and Primary Health Lists

## v2.5.0 (2025-08-13)

### Feat

- Add court definitions and descriptions for FTT-Claims and FTT-Transport

### Fix

- Make all existing historic tribunals listable

## v2.4.7 (2025-06-06)

### Fix

- Fix estate agent tribunal dates

## v2.4.6 (2025-05-15)

### Fix

- Handle markdown with {target='blank'} when formatting

## v2.4.5 (2025-05-15)

### Feat

- Allow court descriptions take contextual data
- Updates the court start_date data

## v2.4.4 (2025-05-13)

### Fix

- Replace & in court names with "and"

## v2.4.3 (2025-04-23)

### Fix

- Mercantile court has wrong NCN pattern

## v2.4.2 (2025-04-22)

No changes in this version.

## v2.4.1 (2025-04-22)

### Fix

- make params obligatory where courts are selectable or listable

## v2.4.0 (2025-03-31)

### Feat

- Add new UKIST tribunal

## v2.3.0 (2025-02-25)

### Feat

- **Court**: add new `type` property to Court objects

## v2.2.1 (2025-01-31)

### Feat

- **Court**: updating court descriptions

## v2.2.0 (2025-01-24)

### Feat

- **Court**: add description data for all courts
- **Court**: add historical document data for all courts

## v2.1.0 (2025-01-21)

### Feat

- **Court**: add support text for old documents as HTML
- **Court**: add court descriptions as HTML

### Fix

- **deps**: update dependency ruamel.yaml to v0.18.10
- **deps**: update dependency ruamel.yaml to v0.18.8
- **deps**: update dependency ruamel.yaml to v0.18.7

### Refactor

- **Court**: make Markdown loading/rendering reusable

## v2.0.1 (2024-11-25)

### Fix

- **neutral_url**: neutral_url no longer returns URIs with a leading slash

## v2.0.0 (2024-10-02)

### BREAKING CHANGE

- `Court.ncn` is now `Court.ncn_pattern`, and now returns a `NeutralCitationPattern` which is a subtype of `re.Pattern[str]`.
- Existing calls to `neutral_url()` will need to be made type-aware in all downstream projects where typechecking is used.

### Feat

- **Court**: make it clearer what Court.ncn actually means
- **types**: add new types for NCN-related strings

### Fix

- **courts**: add additional type statements for stricter behaviour of courts repository

### Refactor

- **types**: move autogen court types to new types submodule

## v1.7.0 (2024-09-30)

### Feat

- **FCL-343**: Add typing to utils

## v1.6.0 (2024-09-24)

### Feat

- **FCL-323**: make Crown Court listable and selectable

## v1.5.7 (2024-09-23)

### Fix

- **FCL-299**: remove incorrect end_year values for courts

## [Release 1.5.6]

- Change Crown Courts to EWCRC
- Make Crown Courts visible

## [Release 1.5.5]

- [FCL-119] Make County Courts visible

## [Release 1.5.4]

- [FCL-119] Add Crown and County Courts (invisible)

## [Release 1.5.3]

- [FCL-134] Make IPT visible in Public and Editor UIs

## [Release 1.5.2]

- [FCL-176] Tooling configuration audit
- [FCL-134] Use ukiptrib as url, not ukipt

## [Release 1.5.1]

- Add T1/T2/T3 to EWCOP neutral citation regex
- Add IPT as a new court
- Remove parenthetical information from Family Court

## [Release 1.5.0]

- FCL91 - Change display name for Lower Courts to Other Courts
- FCL120 - Allow (T1) to (T3) for EWCOP neutral citations

## [Release 1.4.2]

- Remove redundant duplicate of patent court

## [Release 1.4.1]

- Fix bug where getting a nonexistent jurisdiction for a court raised an IndexError. Now we explicitly raise a CourtNotFoundError for unknown jurisdictions.

## [Release 1.4.0]

- Add jurisdiction metadata to courts to support GRC subdivisions

## [Release 1.3.5]

- Fix an issue with EWFC B's name taking priority for the 'ewfc' param

## [Release 1.3.4]

- Add data for EWFC B
- Fix brackets on a court NCN (that isn't used anywhere)

## [Release 1.3.3]

- Add regular expression to validate UKAIT NCNs and convert them to NCN-based URIs.

## [Release 1.3.2]

- Add a new unlisted court with the UKAIT court code in order that EUI court validation works.

## [Release 1.3.1]

- Don't list both aliases of the Immigration and Asylum tribunal, but keep the url alias.

## [Release 1.3.0]

- The Upper Tribunal (Immigation and Asylum Chamber) used to be called the "Asylum and Immigration Tribunal", with a different NCN format (and therefore URL param). This release ensures that cases with both NCN styles show for the Upper Tribunal (I&AC), and that the two court names are shown with the appropriate dates in contexts where we lists courts.

## [Release 1.2.1]

- Reorder tribunal groups so Employment Appeal is at the top

## [Release 1.2.0]

- Add accessors for grouped selectable courts and tribunals (`get_grouped_selectable_courts` / `get_grouped_selectable_tribunals`)
- Reorder and rename courts for hierarchical view
- Rename 'list_name' to 'grouped_name' to make it clearer in which contexts each name is used

## [Release 1.1.0]

- Add `display_heading` property to CourtGroups to determine if they are displayed in the PUI as groups.
- Add `get_selectable_groups` method to CourtsRepository to get all selectable courts, grouped.

## [Release 1.0.2]

- Add JSON Schema to validate courts data
- Ensure courts in alphabetical order in their parent courts
- Courts display their name in repr contexts

## [Release 1.0.1]

- Add King's Bench identifiers to the court list

## [Release 1.0.0]

- Raise a meaningful exception (CourtNotFoundException) when a court is not
  found for a given param or code.

## [Release 0.5.0]

- Added ability to look up court by code

## [Release 0.4.5]

- Assorted quality of life improvements

## [Release 0.4.4]

- Fix all court end dates to 2022, pending ingest of judgments for 2023
  (and/or an alternative solution for accessing this metadata dynamically)

## [Release 0.4.3]

- Standardise documentation (README and licence)
- Add CodeQL configuration
- Add a check for secrets

## [Release 0.4.2]

- Set the default search for all courts to be URI based, for now

## [Release 0.4.1]

- Correct two canonical params for courts which were incorrect.

## [Release 0.4.0]

- Add accessors to return all visible courts or tribunals ungrouped.

## [Release 0.3.2]

- Fix bug in court names - parameter values for upper tribunals were incorrect.

## [Release 0.3.1]

- Add newly supported first-tier tribunals to the court list

## [Release 0.3.0]

- Add helper to access court metadata by parameter value.

## [Release 0.2.0]

- Add helpers for accessing metadata about courts

## [Release 0.1.6]

- Add King's Bench to NCN parser regex
- Add github action to lint code on push
- Add court names and documentation
- Use YAML file for configuration
- Use Poetry for test workflow

## [Release 0.1.4]

- Initial tagged release
