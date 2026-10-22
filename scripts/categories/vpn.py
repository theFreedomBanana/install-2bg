"""VPN client selection."""

from scripts.prompt import choose

CHOICES = [
    {"name": "MullvadVPN (Linux only)", "value": "mullvad"},
    {"name": "NordVPN", "value": "nordvpn"},
    {"name": "Proton VPN", "value": "protonvpn"},
    {"name": "WireGuard (tools only)", "value": "wireguard"},
]


def select_vpn():
    """Display a multi-select menu for VPN clients."""

    return choose("Which VPN clients would you like to install?", CHOICES)
