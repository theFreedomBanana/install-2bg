"""Database manager selection."""

from scripts.prompt import choose

CHOICES = [
    {"name": "DBeaver", "value": "dbeaver"},
    {"name": "Beekeeper Studio", "value": "beekeeper"},
    {"name": "pgAdmin", "value": "pgadmin"},
    {"name": "DbVisualizer", "value": "dbvis"},
    {"name": "MongoDB Compass", "value": "compass"},
    {"name": "Redis Insight", "value": "redisinsight"},
]


def select_database_managers():
    """Display a multi-select menu for database managers."""

    return choose("Which database managers would you like to install?", CHOICES)
