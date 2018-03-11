from flask import Flask, render_template, request, jsonify

from datetime import datetime

import pybot.utils as utils

import pybot.config as conf

app = Flask(__name__)

# #Config option
# app.config.from_object('config')

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
	keywords = request.args.get('keywords', '')
	keywords = utils.parser(keywords)
	address = request.args.get('address','')
	address = utils.parser_for_wiki(address)
	# Try the address as keywords in first place
	try:
		result = utils.get_data_from_wiki(address)
		return jsonify(result)
	# If there is no return, try only the name of the road
	except KeyError:
		try:
			address = utils.parser_for_name_of_road(address)
			result = utils.get_data_from_wiki(address)
			return jsonify(result)
		#If there is still no result try the same keywords that in the google api
		except KeyError: 
			try:
				result = utils.get_data_from_wiki(keywords)
				return jsonify(result)
			except KeyError:
				return jsonify("Euh... Non là je n'ai rien d'intéressant à ce sujet ! ")
		except ValueError: #Include json.decoder.JSONDecodeError
			try:
				result = utils.get_data_from_wiki(keywords)
				return jsonify(result)
			except KeyError:
				return jsonify("Euh... Non là je n'ai rien d'intéressant à ce sujet ! ")


@app.route('/google_api')
def google_api():
	keywords = request.args.get('keywords', '')
	keywords = utils.parser(keywords)
	try:
		result_lat, result_long, address = utils.get_data_from_google_maps(keywords)
		return jsonify(result_lat, result_long, address)
	except TypeError:
		return jsonify('NORETURN')

