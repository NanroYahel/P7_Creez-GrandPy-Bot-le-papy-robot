"""File containing all the unit tests for the application"""

import unittest
import pybot
from pybot import utils

class TestFlaskApp(unittest.TestCase):
    """Unit test class for """

    def setUp(self):
        pybot.app.testing = True
        self.app = pybot.app.test_client()


    def test_index_by_default_url(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status_code, 200)

    def test_index_by_index_url(self):
        rv = self.app.get('/index')
        self.assertEqual(rv.status_code, 200)


class TestUtils(unittest.TestCase):
    """test all functions in the 'utils.py' file"""

    def test_parser(self):
        """Test the parser function"""
        test_result = utils.parser("Je suis allé au marché")
        assert test_result == "Je allé marché"



if __name__ == "__main__":
    unittest.main()