#!/usr/bin/python3
"""Defines unittests for console.py."""

import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """This class defines a set of unit tests for the HBNBCommand
       console application.
    """
    def setUp(self):
        self.console = HBNBCommand()
        self.mock_stdout = MagicMock()

    def tearDown(self):
        self.console = None

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit_command(self, mock_stdout):
        self.assertTrue(self.console.onecmd("quit"))
        self.assertTrue(mock_stdout.getvalue() == "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_EOF_command(self, mock_stdout):
        self.assertTrue(self.console.onecmd("EOF"))
        self.assertTrue(mock_stdout.getvalue() == "\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline(self, mock_stdout):
        self.console.emptyline()
        self.assertTrue(mock_stdout.getvalue() == "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_BaseModel(self, mock_stdout):
        self.assertFalse(self.console.onecmd("create BaseModel"))
        self.assertTrue(mock_stdout.getvalue() != "")


if __name__ == '__main__':
    unittest.main()
