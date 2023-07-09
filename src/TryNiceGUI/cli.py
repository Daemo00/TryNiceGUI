"""CLI entry points."""
import argparse

from .main import add_one


def parse_args(args=None):
    """Parse arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'number',
        type=float,
    )
    return parser.parse_args(args=args)


def main(args=None):
    """Entry point for the application script."""
    args = parse_args(args=args)
    number = args.number
    return add_one(number)
