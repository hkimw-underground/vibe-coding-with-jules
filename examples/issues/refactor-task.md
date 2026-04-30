# [Jules Task] Extract string formatting logic to a utility module

## Problem

The `src/report_generator.ts` file has become too large. It contains several helper functions for formatting dates and currencies that are mixed in with the core report generation logic.

## Scope

- Create a new file: `src/utils/formatters.ts`.
- Move the `formatDate`, `formatCurrency`, and `capitalizeTitle` functions from `src/report_generator.ts` to `src/utils/formatters.ts`.
- Export these functions and import them back into `src/report_generator.ts`.
- Update any corresponding test imports if necessary.

## Non-goals

- Do not change the behavior of the formatting functions.
- Do not add new formatting features.
- Do not refactor other parts of `report_generator.ts`.

## Acceptance Criteria

- [ ] Formatting logic is isolated in `src/utils/formatters.ts`.
- [ ] `src/report_generator.ts` uses the imported functions.
- [ ] Existing unit tests pass without modifying the test assertions.

## Validation

The PR should confirm:
- The project builds successfully (`npm run build`).
- All tests pass (`npm run test`).

## Jules Instructions

Perform a pure refactor. The public API of the functions should not change. Ensure you run the test suite to verify no regressions were introduced.
