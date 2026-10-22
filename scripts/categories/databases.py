"""Database selection."""

from scripts.prompt import choose

CHOICES = [
    {"name": "CouchDB", "value": "couchdb"},
    {"name": "MariaDB", "value": "mariadb"},
    {"name": "MongoDB", "value": "mongodb"},
    {"name": "MySQL", "value": "mysql"},
    {"name": "PostgreSQL", "value": "postgresql"},
    {"name": "Redis", "value": "redis"},
    {"name": "SQlite", "value": "sqlite"},
]


# MariaDB is a drop-in replacement for MySQL. Both provide
# mysqld and port 3306, so apt and Homebrew each refuse to install the second
# one.
CONFLICTING_PAIR = ("mysql", "mariadb")

CONFLICT_NOTE = "Note: MySQL and MariaDB conflict, so pick at most one of the two."

CONFLICT_MESSAGE = (
    "MySQL and MariaDB cannot be installed side by side. Deselect one of the two."
)


def _no_conflict(selection):
    """Return False when the selection holds both MySQL and MariaDB."""

    return not set(CONFLICTING_PAIR).issubset(selection)


def select_databases():
    """Display a multi-select menu for databases."""

    return choose(
        "Which databases would you like to install?",
        CHOICES,
        note=CONFLICT_NOTE,
        validate=_no_conflict,
        invalid_message=CONFLICT_MESSAGE,
    )
