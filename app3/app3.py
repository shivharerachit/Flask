###Building URL Dynamically
###Variable Rules and URL Building

from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score >= 50:
        res='PASSED'
    else:
        res='FAILED'
    return render_template('result.html',result=res,marks=score)

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4
    
    return redirect(url_for("success",score=total_score))

if __name__=='__main__':
    app.run(debug=True) ###Debug true will help to see the changes in the browser without restarting the server