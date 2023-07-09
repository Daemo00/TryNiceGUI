import unittest

from TryNiceGUI.cli import main


class TestCLI(unittest.TestCase):

    def test_cli(self):
        args = str(5)
        self.assertEqual(main(args=args), 6)
