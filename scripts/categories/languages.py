"""Programming language runtime selection."""

from scripts.prompt import choose

CHOICES = [
    {"name": "Clojure (needs Java)", "value": "clojure"},
    {"name": "Crystal", "value": "crystal"},
    {"name": "Dart", "value": "dart"},
    {"name": "Elixir (needs Erlang)", "value": "elixir"},
    {"name": "Erlang/OTP", "value": "erlang"},
    {"name": "Go", "value": "go"},
    {"name": "Groovy (needs Java)", "value": "groovy"},
    {"name": "Java", "value": "java"},
    {"name": "Javascript - Bun", "value": "bun"},
    {"name": "Javascript - Deno", "value": "deno"},
    {"name": "Javascript - Node.js", "value": "node"},
    {"name": "Julia", "value": "julia"},
    {"name": "Kotlin (needs Java)", "value": "kotlin"},
    {"name": "Lua", "value": "lua"},
    {"name": "Perl", "value": "perl"},
    {"name": "Python", "value": "python"},
    {"name": "Ruby", "value": "ruby"},
    {"name": "Rust", "value": "rust"},
    {"name": "Scala (needs Java)", "value": "scala"},
    {"name": "Swift", "value": "swift"},
    {"name": "Zig", "value": "zig"},
    {"name": ".NET", "value": "dotnet"},
]


def select_languages():
    """Display a multi-select menu for language runtimes."""

    return choose(
        "Which language runtimes would you like to install?",
        CHOICES,
    )
