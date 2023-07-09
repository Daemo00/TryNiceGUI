"""Home Page."""

from nicegui import ui


def content() -> None:
    """Home Page Content."""
    ui.label('Hello NiceGUI!').classes('text-h4 font-bold text-grey-8')
