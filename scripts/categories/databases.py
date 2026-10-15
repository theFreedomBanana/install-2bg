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


def select_databases():
    """Display a multi-select menu for databases."""

    return choose("Which databases would you like to install?", CHOICES)
