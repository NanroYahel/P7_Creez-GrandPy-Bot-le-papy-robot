from flask import Flask, render_template

from datetime import datetime

app = Flask(__name__)

#Config option
app.config.from_object('config')

#Use for display the correct year for the copyright in the footer
@app.context_processor
def inject_now():
    return dict(now=datetime.now())

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

def hello(name):
    return 'Hello ' + name