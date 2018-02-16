import os
import pytest
import pybotapp 
import tempfile
import flask

from .. import views as script

def test_hello():
    assert script.hello('Ronan') == 'Hello Ronan'

def Pybotapp_test():
	with script.app.test_request_context('/'):
		assert flask.request.path == '/'