"""Collect the user's installation choices and write them out for Ansible."""

import json
import sys

from categories.api_clients import select_api_clients
from categories.browsers import select_browsers
from categories.build_tools import select_build_tools
from categories.database_managers import select_database_managers
from categories.databases import select_databases
from categories.devops import select_devops
from categories.cli_tools import select_cli_tools
from categories.editors import select_editors
from categories.git_tools import select_git_tools
from categories.languages import select_languages
from categories.media import select_media
from categories.network_tools import select_network_tools
from categories.notes import select_notes
from categories.server import select_servers
from categories.shells import (
    select_login_shell,
    select_shell_plugins,
    select_shells,
)
from categories.socials import select_socials
from categories.terminals import select_terminals
from categories.vpn import select_vpn
from categories.tunneling import select_tunneling


def main():
    """Collect selections and write them to the JSON file named on the command line."""

    if len(sys.argv) != 2:
        print("usage: python -m scripts.select_apps OUTPUT_JSON_FILE", file=sys.stderr)
        sys.exit(2)

    try:
        browsers = select_browsers()
        editors = select_editors()
        terminals = select_terminals()
        databases = select_databases()
        database_managers = select_database_managers()
        devops = select_devops()
        tunneling = select_tunneling()
        socials = select_socials()
        vpn = select_vpn()
        notes = select_notes()
        media = select_media()
        git_tools = select_git_tools()
        servers = select_servers()
        cli_tools = select_cli_tools()
        network_tools = select_network_tools()
        languages = select_languages()
        build_tools = select_build_tools()
        api_clients = select_api_clients()
        shells = select_shells()

        result = {
            "selected_browsers": browsers,
            "selected_editors": editors,
            "selected_terminals": terminals,
            "selected_databases": databases,
            "selected_database_managers": database_managers,
            "selected_devops": devops,
            "selected_tunneling": tunneling,
            "selected_socials": socials,
            "selected_vpn": vpn,
            "selected_notes": notes,
            "selected_media": media,
            "selected_git_tools": git_tools,
            "selected_servers": servers,
            "selected_cli_tools": cli_tools,
            "selected_network_tools": network_tools,
            "selected_languages": languages,
            "selected_build_tools": build_tools,
            "selected_api_clients": api_clients,
            "selected_shells": shells,
            "selected_shell_plugins": select_shell_plugins(shells),
            "selected_login_shell": select_login_shell(shells),
        }
    except KeyboardInterrupt:
        print("\nSelection cancelled.", file=sys.stderr)
        sys.exit(130)

    # The menus draw on stdout, so the answers must not go there too.
    with open(sys.argv[1], "w", encoding="utf-8") as handle:
        json.dump(result, handle)


if __name__ == "__main__":
    main()
