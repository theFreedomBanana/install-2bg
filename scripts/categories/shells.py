"""Shell selection, and the plugin manager that goes with each shell."""

from scripts.prompt import choose, choose_one

CHOICES = [
    {"name": "Elvish", "value": "elvish"},
    {"name": "Fish", "value": "fish"},
    {"name": "Nushell", "value": "nushell"},
    {"name": "Xonsh", "value": "xonsh"},
    {"name": "Zsh", "value": "zsh"},
]

# A plugin manager is only worth offering once its shell is selected.
PLUGIN_CHOICES = {
    "zsh": {"name": "Oh My Zsh (framework for Zsh)", "value": "oh-my-zsh"},
    "fish": {"name": "Fisher (plugin manager for Fish)", "value": "fisher"},
}


def select_shells():
    """Display a multi-select menu for shells."""

    return choose("Which shells would you like to install?", CHOICES)


def select_shell_plugins(shells):
    """Offer a plugin manager for each selected shell, if any."""

    choices = [PLUGIN_CHOICES[shell] for shell in shells if shell in PLUGIN_CHOICES]

    if not choices:
        return []

    return choose(
        "Which shell plugin managers would you like to install?",
        choices,
    )


def select_login_shell(shells):
    """Offer to make one of the selected shells the login shell."""

    if not shells:
        return ""

    labels = {choice["value"]: choice["name"] for choice in CHOICES}

    choices = [{"name": "Keep my current login shell", "value": ""}]
    choices += [{"name": labels[shell], "value": shell} for shell in shells]

    return choose_one("Would you like to switch your login shell?", choices)
