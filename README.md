# Golf Agent Curses Menu

This repository contains a terminal user interface (TUI) that mirrors the provided Golf Agent simulator flowchart using Python's `curses` module.

## Requirements
- Python 3.9+
- A terminal that supports ANSI escape sequences.
- macOS/Linux: `curses` is bundled with Python.
- Windows: install the `windows-curses` wheel before running the script.

```bash
pip install windows-curses
```

## How to run
1. Open a terminal that supports full-screen applications.
2. Change into the project directory (the folder that contains `golf_menu.py`).
3. Execute the script with Python:
   ```bash
   python3 golf_menu.py
   ```
4. Navigate with the arrow keys (or `j`/`k`), press **Enter** to select an item, `b` to go back, and `q` to quit.

If you encounter issues launching the interface in a terminal, you can verify that Python can import `curses` by running `python3 -c "import curses"`.
