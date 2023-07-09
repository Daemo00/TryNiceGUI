"""Common Theme for all the pages."""

from contextlib import contextmanager

from .menu import menu

from nicegui import ui


@contextmanager
def frame(navtitle: str):
    """Share the same styling and behavior across all pages."""
    with ui.header().classes('justify-between text-white'):
        ui.label("Theme Header")
        ui.label(navtitle)
        with ui.row():
            menu()
    with ui.column().classes('absolute-center items-center'):
        yield
