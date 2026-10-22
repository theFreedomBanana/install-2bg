"""Social and communication app selection."""

from scripts.prompt import choose

CHOICES = [
    {"name": "Discord", "value": "discord"},
    {"name": "Slack", "value": "slack"},
    {"name": "Zoom (Linux only)", "value": "zoom"},
]


def select_socials():
    """Display a multi-select menu for social and communication apps."""

    return choose("Which social apps would you like to install?", CHOICES)
