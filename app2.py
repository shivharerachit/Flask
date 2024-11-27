###Building URL Dynamically
###Variable Rules and URL Building

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to the Flask App!'

@app.route('/success/<int:score>')
def success(score):
    return "The student has passed with a score of " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The student has failed with a score of "+ str(score)

@app.route('/results/<int:marks>')
def results(marks):
    if marks < 50:
        result='fail'
    else: 
        result='success'
    return redirect(url_for(result,score=marks))

if __name__=='__main__':
    app.run(debug=True) ###Debug true will help to see the changes in the browser without restarting the server