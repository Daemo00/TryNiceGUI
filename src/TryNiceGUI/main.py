"""Main file."""

from nicegui import ui


def run():
    """Run the application."""
    ui.label('Hello NiceGUI!')
    ui.run(
        reload=False,
        dark=True,
    )
