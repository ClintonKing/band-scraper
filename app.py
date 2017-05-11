import sys
from scrape_album import *
from flask import Flask, make_response, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()