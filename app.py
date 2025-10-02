from flask import Flask,render_template,session
import numpy as np
import pandas as pd


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload')
def upload():
    if request.method == 'POST':
         if 'submit' in request.form:
        file = request.files['csvfile']
        if file and file.filename.endswith('.csv'):
            data = pd.read_csv(file)
            session['data'] = data.to_json()
    elif 'next' in request.form:
        if 'data' in session:
            return redirect(url_for('/clean'))
        else:
            return "No Data Uploaded! Please upload to proceed"
    return render_template('inputpage.html')

@app.route('/clean')
def clean():
    return render_template('cleaning.html')

if __name__ == "__main__":
    app.run(debug=True)