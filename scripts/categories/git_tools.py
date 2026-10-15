"""Git and UI client selection."""

from scripts.prompt import choose

CHOICES = [
    {"name": "Git", "value": "git"},
    {"name": "GitHub CLI", "value": "gh"},
    {"name": "Git-delta", "value": "git-delta"},
    {"name": "Git LFS", "value": "git-lfs"},
    {"name": "Lazygit", "value": "lazygit"},
]


def select_git_tools():
    """Display a multi-select menu for Git tooling."""

    return choose("Which Git tools would you like to install?", CHOICES)
