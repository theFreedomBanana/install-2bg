"""Shared pieces for the selection menus."""

from InquirerPy import inquirer

NAVIGATION_HINT = "(Use ↑/↓ to navigate, Space to select, Enter to confirm)"
SINGLE_HINT = "(Use ↑/↓ to navigate, Enter to confirm)"


def choose(message, choices):
    """Display a multi-select menu and return the chosen values."""

    return inquirer.checkbox(
        message=message,
        choices=choices,
        instruction=NAVIGATION_HINT,
        cycle=True,
    ).execute()


def choose_one(message, choices):
    """Display a single-select menu and return the chosen value."""

    return inquirer.select(
        message=message,
        choices=choices,
        instruction=SINGLE_HINT,
        cycle=True,
    ).execute()
