"""Web browser selection."""

from scripts.prompt import choose

CHOICES = [
    {"name": "Brave", "value": "brave"},
    {"name": "Chromium (Linux only)", "value": "chromium"},
    {"name": "Comet (Perplexity)", "value": "comet"},
    {"name": "Firefox", "value": "firefox"},
    {"name": "Google Chrome", "value": "chrome"},
    {"name": "Microsoft Edge", "value": "edge"},
    {"name": "Opera", "value": "opera"},
    {"name": "Zen", "value": "zen"},
]


def select_browsers():
    """Display a multi-select menu for web browsers."""

    return choose("Which web browsers would you like to install?", CHOICES)
