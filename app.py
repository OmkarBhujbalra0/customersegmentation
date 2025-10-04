from flask import Flask,render_template,request,redirect,url_for
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload",methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('csvfile')
        if file:
            if file.filename.endswith('.csv'):
                data = pd.read_csv(file)
                print(f"File uploaded successfully.{data.shape[0]} rows and {data.shape[1]} columns")
                table_string = data.to_html()
                return render_template('inputpage.html',message= f"File uploaded successfully.{data.shape[0]} rows and {data.shape[1]} columns",table_string=table_string)
            else:
                print("Please Upload a Valid CSV File")
                return render_template('inputpage.html',message="Please Upload a Valid CSV File")
    return render_template("inputpage.html")

if __name__ == "__main__":
    app.run(debug=True)

# Use Flash function for message in next part