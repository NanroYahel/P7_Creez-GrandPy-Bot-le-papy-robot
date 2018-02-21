from flask import Flask, render_template, request

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
	# if request.method == "POST":
	# 	usr_question = request.form['question']
	# 	text = utils.make_text(usr_question)
	# 	return render_template('test.html', question=text)

	if request.method == "POST":
		usr_question = request.form['question']
		search = utils.parser(usr_question)
		result_lat, result_long = utils.get_data_from_google_maps(search)
		return render_template('test.html', result_lat=result_lat, result_long=result_long, \
			google_key=conf.GOOGLE_MAPS_KEY)

	return render_template('index.html')





