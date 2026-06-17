"""Frontend application entrypoint."""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Multi-Agent Research System'
