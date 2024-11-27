###Building URL Dynamically
###Variable Rules and URL Building
from constants import secret_key, json_file
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
flow = InstalledAppFlow.from_client_secrets_file(
    'json_file.json', ['https://www.googleapis.com/auth/drive.metadata.readonly'])

creds = flow.run_local_server(port=0)

from googleapiclient.discovery import build
service = build('drive', 'v3', credentials=creds)

###Jinja2 Templating Engine
'''
{%...%} for Statements
{{...}} for Expressions to print to the template output
{#...#} for Comments not included in the template output
'''
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

# @app.route('/success/<int:score>')
# def success(score):
#     res=""
#     if score >= 50:
#         res=' PASSED '
#     else:
#         res=' FAILED '
    
#     exp={' Score ':score,' Result ':res}
#     return render_template('result.html',result=exp)

# @app.route('/submit',methods=['POST','GET'])
# def submit():
#     total_score=0
#     if request.method=='POST':
#         science=float(request.form['science'])
#         maths=float(request.form['maths'])
#         c=float(request.form['c'])
#         data_science=float(request.form['datascience'])
#         total_score=(science+maths+c+data_science)/4
    
#     return redirect(url_for("success",score=total_score))



@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method=='GET':
        
    return 'hello'



if __name__=='__main__':
    app.run(debug=True) ###Debug true will help to see the changes in the browser without restarting the server