from flask import Flask,render_template
import numpy as np
import pandas as pd


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload')
def upload():
    return render_template('inputpage.html')

if __name__ == "__main__":
    app.run(debug=True)