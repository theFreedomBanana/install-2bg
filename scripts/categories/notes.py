"""Note taking app selection."""

from scripts.prompt import choose

CHOICES = [
    {"name": "Notion", "value": "notion"},
    {"name": "Obsidian", "value": "obsidian"},
]


def select_notes():
    """Display a multi-select menu for note taking apps."""

    return choose("Which note taking apps would you like to install?", CHOICES)
