"""Command line tool selection."""

from scripts.prompt import choose

CHOICES = [
    {"name": "curl", "value": "curl"},
    {"name": "eza (modern ls)", "value": "eza"},
    {"name": "htop", "value": "htop"},
    {"name": "fzf", "value": "fzf"},
    {"name": "fzy", "value": "fzy"},
    {"name": "tmux", "value": "tmux"},
    {"name": "wget", "value": "wget"},
]


def select_cli_tools():
    """Display a multi-select menu for command line tools."""

    return choose(
        "Which command line tools would you like to install?",
        CHOICES,
    )
