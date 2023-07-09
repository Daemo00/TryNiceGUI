"""Main file."""


from nicegui import app, ui

from . import home_page, theme
from .pages import with_router, delay_creation


def populate_ui():
    """Insert everything in the UI."""

    @ui.page('/')
    def index_page() -> None:
        """Index."""
        with theme.frame('Homepage'):
            home_page.content()

    delay_creation.create()
    app.include_router(with_router.router)


def run():
    """Run the application."""
    populate_ui()
    ui.run(
        reload=False,
        dark=True,
    )
