"""Server selection."""

from scripts.prompt import choose

CHOICES = [
    {"name": "Nginx", "value": "nginx"},
]


def select_servers():
    """Display a multi-select menu for servers."""

    return choose("Which servers would you like to install?", CHOICES)
