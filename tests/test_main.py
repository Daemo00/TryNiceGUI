import unittest

from nicegui import globals
from TryNiceGUI.main import populate_ui


class TestMain(unittest.TestCase):

    def test_client(self):
        populate_ui()
        client = globals.get_client()

        self.assertEqual(
            client.elements[3].tag,
            'div',
        )
