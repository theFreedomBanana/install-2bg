# Workstation Configuration

Set up a fresh machine without doing it by hand twice.

Run `./install.sh`, answer 19 questions, and Ansible installs exactly what
you picked — nothing more. Works on macOS, Ubuntu and Debian from the
same selection.

## What it covers

122 tools across 19 categories: browsers, editors, terminals, shells,
databases and their GUI clients, 22 language runtimes via mise, DevOps
and Kubernetes tooling, API clients, VPNs, build tools, and the command
line utilities your dotfiles already assume.

## How it behaves

- **Asks first.** One summary, one confirmation, then it runs.
- **Honest about gaps.** A tool with no build for your platform is
  reported and skipped, not silently ignored.
- **Safe to re-run.** Every task is idempotent; a second run changes
  nothing.
- **Leaves your config alone.** Generated shell settings live in their
  own file, loaded by a single marked line in your rc.