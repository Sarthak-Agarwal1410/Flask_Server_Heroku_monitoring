from flask import Flask
import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/time')
def time_now():
    now = datetime.datetime.now()
    return now.time().strftime('%H:%M:%S')

app.run()
