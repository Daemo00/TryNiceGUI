"""Menu for all the pages."""
from nicegui import ui


def menu() -> None:
    """Create Menu."""
    ui.link('Home', '/').classes(replace='text-white')
    ui.link('A', '/a').classes(replace='text-white')
    ui.link('B', '/b').classes(replace='text-white')
    ui.link('C', '/c').classes(replace='text-white')
