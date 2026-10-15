"""Media app selection."""

from scripts.prompt import choose

CHOICES = [
    {"name": "OBS Studio", "value": "obs"},
    {"name": "VLC", "value": "vlc"},
    {"name": "VokoscreenNG (Linux only)", "value": "vokoscreen"},
]


def select_media():
    """Display a multi-select menu for media apps."""

    return choose("Which media apps would you like to install?", CHOICES)
