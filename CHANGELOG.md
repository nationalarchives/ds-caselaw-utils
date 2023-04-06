# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog 1.0.0].

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

[Unreleased]: https://github.com/nationalarchives/ds-caselaw-utils/compare/v0.5.0...HEAD
[Release 0.5.0]: https://github.com/nationalarchives/ds-caselaw-utils/compare/v0.4.5...v0.5.0
[Release 0.4.5]: https://github.com/nationalarchives/ds-caselaw-utils/compare/v0.4.4...v0.4.5
[Release 0.4.4]: https://github.com/nationalarchives/ds-caselaw-utils/compare/v0.4.3...v0.4.4
[Release 0.4.3]: https://github.com/nationalarchives/ds-caselaw-utils/compare/v0.4.2...v0.4.3
[Release 0.4.2]: https://github.com/nationalarchives/ds-caselaw-utils/compare/v0.4.1...v0.4.2
[Release 0.4.1]: https://github.com/nationalarchives/ds-caselaw-utils/compare/v0.4.0...v0.4.1
[Release 0.4.0]: https://github.com/nationalarchives/ds-caselaw-utils/compare/v0.3.2...v0.4.0
[Release 0.3.2]: https://github.com/nationalarchives/ds-caselaw-utils/compare/v0.3.1...v0.3.2
[Release 0.3.1]: https://github.com/nationalarchives/ds-caselaw-utils/compare/v0.3.0...v0.3.1
[Release 0.3.0]: https://github.com/nationalarchives/ds-caselaw-utils/compare/v0.2.0...v0.3.0
[Release 0.2.0]: https://github.com/nationalarchives/ds-caselaw-utils/compare/v0.1.6...v0.2.0
[Release 0.1.6]: https://github.com/nationalarchives/ds-caselaw-utils/compare/v0.1.4...v0.1.6
[Release 0.1.4]: https://github.com/nationalarchives/ds-caselaw-utils/releases/tag/v0.1.4
[keep a changelog 1.0.0]: https://keepachangelog.com/en/1.0.0/
