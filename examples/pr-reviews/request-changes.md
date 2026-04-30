# Example: Request Changes (Scope Creep)

**Context:** Jules has opened a PR that solves the issue but also includes an unrequested refactor of a neighboring function.

---

**Reviewer Action:** Request Changes

**Comment:**

> Jules, the fix for the `NullReferenceException` is correct. However, you also reformatted the `processUserData` function which was explicitly outside the scope of issue #15.
>
> Please revert the changes to `processUserData` so that this PR only contains the null check. Once that is reverted and the tests still pass, I will approve.
