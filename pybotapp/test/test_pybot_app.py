import os
import pytest
import pybotapp
import tempfile
import flask
from flask import Flask
from flask_testing import TestCase

from .. import views as script



class MyTest(TestCase):

	def create_app(self):
		app = Flask(__name__)
		app.config["TESTING"] = True
		return app

	def Pybotapp_test():
		with script.app.test_request_context('/'):
			assert flask.request.path == '/'