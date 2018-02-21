from flask import Flask, render_template, request

from datetime import datetime

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
	if request.method == "POST":
		usr_question = request.form['question']
		text = make_text(usr_question)
		return render_template('test.html', question=text)

	return render_template('index.html')





