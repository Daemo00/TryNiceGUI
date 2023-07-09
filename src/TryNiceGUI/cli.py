"""CLI entry points."""
import argparse

from nicegui import ui


def parse_args(args=None):
    """Parse arguments."""
    parser = argparse.ArgumentParser()
    return parser.parse_args(args=args)


def main(args=None):
    """Entry point for the application script."""
    args = parse_args(args=args)


ui.label('Hello NiceGUI!')
ui.run(dark=True)
