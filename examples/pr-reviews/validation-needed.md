# Example PR Review: Validation Needed

This is an example of a maintainer asking for more validation.

---

**Reviewer:** @maintainer
**Status:** Comment

Thanks for the PR. The code changes in `src/auth.js` look reasonable, but I don't see any evidence that this has been tested with the edge cases mentioned in #789 (specifically, the expired token scenario).

Could you please:
1. Run the existing authentication tests and post the results here?
2. Add a new test case for the expired token scenario if it doesn't already exist?
3. Provide a log output showing how the system handles an expired token with your changes?

I will review again once the validation notes are added to the PR description.
