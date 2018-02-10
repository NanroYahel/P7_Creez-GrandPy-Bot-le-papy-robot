from flask import Flask, render_template

app = Flask(__name__)

#Config option
app.config.from_object('config')


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

def hello(name):
    return 'Hello ' + name