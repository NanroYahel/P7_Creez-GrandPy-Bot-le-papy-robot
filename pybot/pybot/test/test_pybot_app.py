"""File containing all the unit tests for the application"""

import unittest
import pybot
from pybot import utils
from unittest.mock import MagicMock, patch

from io import BytesIO
import json

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
        self.assertEqual(test_result,"Je allé marché")

    @patch('pybot.utils.request_api')
    def test_get_data_from_google_maps(self, mock_request_api):
        """Test the Google map api request function"""
        mock_result = {"results": [{"geometry": {"location": \
            {"lat": 47.231849, "lng": -1.5584598}}}]}
        mock_request_api.return_value = mock_result
        test_lat, test_long = utils.get_data_from_google_maps("test")
        self.assertEqual(test_lat, 47.231849)
        self.assertEqual(test_long, -1.5584598)

if __name__ == "__main__":
    unittest.main()