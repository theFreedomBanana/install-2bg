"""Terminal selection."""

from scripts.prompt import choose

CHOICES = [
    {"name": "Alacritty", "value": "alacritty"},
    {"name": "Ghostty", "value": "ghostty"},
    {"name": "iTerm2", "value": "iterm2"},
    {"name": "Kitty", "value": "kitty"},
    {"name": "Terminator", "value": "terminator"},
    {"name": "WezTerm", "value": "wezterm"},
]


def select_terminals():
    """Display a multi-select menu for terminals."""

    return choose("Which terminals would you like to install?", CHOICES)
