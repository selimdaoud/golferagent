# Launching the Golfer Simulator

When merging branches that each changed the launch instructions, the README can
end up with conflicts. To avoid that, this guide collects every supported
execution mode in one place so branches only need to link here.

## Packaged release (`golfer-sim` entry point)

Use this flow when testing the published build or verifying distribution
artifacts:

```bash
pip install golfer-sim
# or install from a local wheel: pip install dist/golfer_sim-<version>-py3-none-any.whl

golfer-sim
```

The console script invokes the curses dashboard bundled in the package. It
relies on the same weekly simulation loop as the development workflow.

## Module execution (`python -m`)

During development you usually want to run the code directly from your clone so
changes are picked up immediately:

```bash
python -m golfer_sim.ui.curses_app
```

This respects any editable installation (`pip install -e .`) and requires only
Python and the `curses` dependency (Windows users should install
`windows-curses`).

## Legacy compatibility script (`golf_menu.py`)

Some environments—especially minimal containers or older tutorials—still point
to the historical `golf_menu.py`. The script now delegates to the packaged
entry point while preserving the exact invocation signature:

```bash
python3 golf_menu.py
```

Navigation mirrors the packaged dashboard: arrow keys (or `j`/`k`) move the
selection, **Enter** confirms, and **q** exits.

## Troubleshooting

If the interface fails to render, confirm that Python can import `curses`:

```bash
python3 -c "import curses"
```

On Windows, install the pre-built dependency first:

```bash
pip install windows-curses
```

For merge conflict resolution tips around these files, see
[`docs/merge_conflicts.md`](merge_conflicts.md).
