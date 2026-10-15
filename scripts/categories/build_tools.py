"""Compiler and build tool selection."""

from scripts.prompt import choose

CHOICES = [
    {"name": "C and C++ toolchain", "value": "cxx"},
    {"name": "ccache", "value": "ccache"},
    {"name": "CMake", "value": "cmake"},
    {"name": "Fortran", "value": "fortran"},
    {"name": "GDB debugger", "value": "gdb"},
    {"name": "GNU autotools", "value": "autotools"},
    {"name": "Ninja", "value": "ninja"},
    {"name": "pkg-config", "value": "pkgconf"},
]


def select_build_tools():
    """Display a multi-select menu for compilers and build tools."""

    return choose(
        "Which compilers and build tools would you like to install?",
        CHOICES,
    )
