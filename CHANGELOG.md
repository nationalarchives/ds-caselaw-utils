# Changelog

All notable changes to this project will be documented in this file.

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
