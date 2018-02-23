"""File containing all the unit tests for the application"""

import unittest
import pybot
from pybot import utils
from unittest.mock import MagicMock
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
        assert test_result == "Je allé marché"

    def test_get_data_from_google_maps(self):
        """Test the Google map api request function"""
        mock_result = {"results": [{"geometry": {"location": {"lat": 47.23184999999999, "lng": -1.5584598}}}]}
        # result = json.dumps(mock_result)
        # result_2 = json.loads(result)
        # print(type(mock_result))
        # print(mock_result)
        # print(type(result))
        # print(result)
        # print(type(result_2))
        # print(result_2)
        # mock_result = utils.req.Response()
        mock_result = utils.req.Response()
        # mock_result.text = {"results": [{"geometry": {"location": {"lat": 47.23184999999999, "lng": -1.5584598}}}]}
        utils.req.get = MagicMock(return_value=mock_result)
        test_lat, test_long = utils.get_data_from_google_maps("test")
        assert test_lat == 47.23184999999999
        assert test_long == -1.5584598

if __name__ == "__main__":
    unittest.main()