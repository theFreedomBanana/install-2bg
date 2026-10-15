"""Tunneling tool selection."""

from scripts.prompt import choose

CHOICES = [
    {"name": "Localtunnel", "value": "localtunnel"},
    {"name": "Ngrok", "value": "ngrok"},
    {"name": "Zrok", "value": "zrok"},
]


def select_tunneling():
    """Display a multi-select menu for tunneling tools."""

    return choose("Which tunneling tools would you like to install?", CHOICES)
