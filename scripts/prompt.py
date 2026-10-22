"""Shared pieces for the selection menus."""

from InquirerPy import inquirer

NAVIGATION_HINT = "(Use ↑/↓ to navigate, Space to select, Enter to confirm)"
SINGLE_HINT = "(Use ↑/↓ to navigate, Enter to confirm)"


def choose(message, choices, note="", validate=None, invalid_message="Invalid input"):
    """Display a multi-select menu and return the chosen values.

    note is shown under the menu, to warn about a restriction before the user
    hits it. validate rejects a selection on Enter and keeps the menu open,
    showing invalid_message instead. The defaults mirror InquirerPy's own,
    which reject None.
    """

    return inquirer.checkbox(
        message=message,
        choices=choices,
        instruction=NAVIGATION_HINT,
        long_instruction=note,
        validate=validate,
        invalid_message=invalid_message,
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
