# [Jules Task] Update README with new configuration options

## Problem

The new `v2.0` release added three new configuration options (`max_retries`, `timeout_ms`, `fallback_url`), but these are not documented in the main `README.md`. Users are confused about how to configure the client properly.

## Scope

- Update the "Configuration" section in `README.md`.
- Add a new table or list explaining:
  - `max_retries` (default: 3)
  - `timeout_ms` (default: 5000)
  - `fallback_url` (optional, no default)
- Ensure the Markdown formatting matches the existing document.

## Non-goals

- Do not update `CHANGELOG.md`.
- Do not refactor the existing configuration code.
- Do not translate the changes to other languages yet.

## Acceptance Criteria

- [ ] `README.md` includes the three new options.
- [ ] Defaults are clearly stated.
- [ ] Markdown hygiene passes (no trailing spaces, correct heading levels).

## Validation

The PR should confirm:
- `README.md` renders correctly locally.
- Markdown linter passes (`npm run lint:md`).

## Jules Instructions

Create a PR focusing strictly on updating `README.md`. Do not modify source code or translation files.
