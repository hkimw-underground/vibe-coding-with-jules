# [Jules Task] Scoped Refactor: Extract Validation Logic

## Problem
The validation logic in `src/utils/validator.js` has grown too large and is becoming difficult to maintain. It should be split into smaller, more focused functions.

## Scope
- Identify reusable validation patterns in `src/utils/validator.js`.
- Extract these patterns into separate functions within the same file or a new `src/utils/validation-rules.js` file.
- Update the main `validate` function to use these new helper functions.

## Non-goals
- Do not change the external API of the validator.
- Do not add new validation rules.
- Do not modify any other files in `src/utils/` or `src/`.

## Acceptance Criteria
- [ ] `src/utils/validator.js` is more readable and follows the Single Responsibility Principle.
- [ ] All existing tests for the validator pass without modification.
- [ ] No changes to the public `validate` function's behavior.

## Validation
- Run existing unit tests: `npm test src/utils/validator.test.js`.
- Verify code readability with a manual review of the diff.

## Workflow Level
- Level 1 - Human-led Jules workflow
