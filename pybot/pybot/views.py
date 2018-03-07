from flask import Flask, render_template, request, jsonify

from datetime import datetime

import pybot.utils as utils

import config as conf

app = Flask(__name__)

#Config option
app.config.from_object('config')

#Use for display the correct year for the copyright in the footer
@app.context_processor
def inject_now():
    return dict(now=datetime.now())

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	return render_template('index.html', google_key=conf.GOOGLE_MAPS_KEY)


@app.route('/wiki_api')
def wiki_api():
	keywords = request.args.get('keywords', 'test')
	keywords = utils.parser(keywords)
	result = utils.get_data_from_wiki(keywords)
	return jsonify(result)

@app.route('/google_api')
def google_api():
	keywords = request.args.get('keywords', 'test')
	keywords = utils.parser(keywords)
	try:
		result_lat, result_long, address = utils.get_data_from_google_maps(keywords)
		return jsonify(result_lat, result_long, address)
	except TypeError:
		return jsonify('NORETURN')
