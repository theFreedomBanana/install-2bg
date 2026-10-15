"""API client selection."""

from scripts.prompt import choose

CHOICES = [
    {"name": "Bruno", "value": "bruno"},
    {"name": "HTTPie (command line)", "value": "httpie"},
    {"name": "Hurl", "value": "hurl"},
    {"name": "Insomnia", "value": "insomnia"},
    {"name": "Postman", "value": "postman"},
]


def select_api_clients():
    """Display a multi-select menu for API clients."""

    return choose("Which API clients would you like to install?", CHOICES)
