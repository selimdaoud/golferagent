# Resolving README launch instruction conflicts

Branches often touch the README when adding new launch instructions. If two
branches diverge—one documenting packaging and another describing the legacy
script—Git will mark the overlapping block as a conflict. Use the following
approach to reconcile them cleanly:

1. **Keep both perspectives** – ensure the packaged `golfer-sim` flow, module
   execution, and `golf_menu.py` script all remain documented. They serve
   different use cases and should coexist.
2. **Link to `docs/RUN_MODES.md`** – instead of duplicating the detailed steps in
   every branch, keep the README concise and defer to the shared guide. That way
   future edits touch a single file, dramatically reducing conflict surface.
3. **Adjust headings rather than deleting text** – renaming a section (for
   example, from "Running the Dashboard" to "Launch options") keeps the history
   readable and prevents repeated reintroductions of the same heading.
4. **Verify navigation instructions** – after merging, open both the README and
   the new guide to ensure arrow key shortcuts and exit instructions are still
   visible.

When conflicts appear, edit the combined file so it matches the structure above,
then stage the result and continue the merge:

```bash
git add README.md docs/RUN_MODES.md
git merge --continue  # or git rebase --continue if rebasing
```

The repository tests (`pytest`) do not depend on documentation, but running them
can confirm the working tree stays healthy after resolving conflicts.
