"""Network tool selection."""

from scripts.prompt import choose

CHOICES = [
    {"name": "ss (socket statistics)", "value": "ss"},
    {"name": "nmap", "value": "nmap"},
    {"name": "Wireshark", "value": "wireshark"},
]


def select_network_tools():
    """Display a multi-select menu for network tools."""

    return choose("Which network tools would you like to install?", CHOICES)
