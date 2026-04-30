# Example PR Review: Request Changes

This is an example of a maintainer requesting changes on a Jules PR.

---

**Reviewer:** @maintainer
**Status:** Changes Requested

The core logic is correct, but there are a few minor issues that need to be addressed before merging:

1. **Unrelated Change:** In `src/utils/validator.js`, you modified the `config` object on line 45. This was not in the original scope of #456. Please revert this change.
2. **Variable Naming:** Please rename `tempVar` to something more descriptive like `isValidEmail` to match our naming conventions.
3. **Missing Newline:** `docs/api.md` is missing a trailing newline.

Please address these points and update the PR.
