#!/usr/bin/env bash
set -euo pipefail

# Always run from the directory containing this script.
cd "$(dirname "$0")"

# Debian and Ubuntu ship python3 without the venv module.
if [ -r /etc/debian_version ] && ! python3 -c 'import venv' >/dev/null 2>&1; then
    echo "Installing the Python venv module."
    sudo apt-get update
    sudo apt-get install -y python3-venv python3-pip
fi

if ! command -v python3 >/dev/null 2>&1; then
    echo "python3 not found." >&2
    case "$(uname -s)" in
        Darwin) echo "Install the Xcode command line tools: xcode-select --install" >&2 ;;
        *)      echo "Install python3 and the python3-venv package." >&2 ;;
    esac
    exit 1
fi

# Create the virtual environment if it doesn't exist.
if [ ! -d .venv ]; then
    python3 -m venv .venv
fi

# Install the Python dependencies for the selection menus.
.venv/bin/python -m pip install -q --upgrade pip
.venv/bin/python -m pip install -q -r scripts/requirements.txt

# Choose which Ansible to run. A system install from brew or apt is preferred
# because it tracks a current release. Otherwise install it in the virtualenv,
# where the version is capped by whatever python3 this machine ships.
if command -v ansible-playbook >/dev/null 2>&1; then
    ansible_playbook=$(command -v ansible-playbook)
    ansible_galaxy=$(command -v ansible-galaxy)
else
    echo "Ansible not found. Installing it in the virtualenv, which takes a while."
    .venv/bin/python -m pip install -q ansible
    ansible_playbook=.venv/bin/ansible-playbook
    ansible_galaxy=.venv/bin/ansible-galaxy
fi

# The "ansible" distribution ships this collection, but "ansible-core" does not.
if ! "$ansible_galaxy" collection list community.general 2>/dev/null \
     | grep -q 'community\.general'; then
    echo "Installing the community.general collection."
    "$ansible_galaxy" collection install community.general
fi

# Collect interactive selections. The menus draw on stdout, so the answers go
# to a file. Capturing them with $( ) would hide the menus from the user.
selection=$(mktemp)
trap 'rm -f "$selection"' EXIT
.venv/bin/python -m scripts.select_apps "$selection"

# Run the Ansible playbook with the selected applications. -K asks for the
# sudo password once, up front. Several tasks need root: the apt installs on
# Debian, and /etc/paths.d/homebrew on macOS.
"$ansible_playbook" ansible/playbook.yml --ask-become-pass --extra-vars "@$selection"
