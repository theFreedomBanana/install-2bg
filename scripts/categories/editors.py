"""Text editor selection."""

from scripts.prompt import choose

CHOICES = [
    {"name": "Codex (terminal agent)", "value": "codex"},
    {"name": "Cursor", "value": "cursor"},
    {"name": "Devin Desktop (Windsurf)", "value": "windsurf"},
    {"name": "Emacs", "value": "emacs"},
    {"name": "Neovim", "value": "neovim"},
    {"name": "PyCharm Community", "value": "pycharm"},
    {"name": "Sublime Text", "value": "sublimetext"},
    {"name": "Visual Studio Code", "value": "vscode"},
    {"name": "Zed", "value": "zed"},
]


def select_editors():
    """Display a multi-select menu for text editors."""

    return choose("Which text editors would you like to install?", CHOICES)
