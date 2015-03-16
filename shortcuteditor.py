"""A shortcut-key editor for Nuke's menus


homepage: https://github.com/dbr/shortcuteditor-nuke
license: GPL v2


To use, in ~/.nuke/menu.py add this:

try:
    import shortcuteditor
    shortcuteditor.nuke_setup()
except Exception:
    import traceback
    traceback.print_exc()
"""

__version__ = "1.1"


