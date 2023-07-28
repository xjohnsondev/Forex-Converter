from flask import Flask, request, render_template, session, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
import requests

app = Flask(__name__)

app.config['SECRET_KEY'] = "chickenz"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

URL = 'https://api.exchangerate.host/latest'

currencyList = []


@app.route('/')
def home():
    res = requests.get(URL)
    data = res.json()
    session['data'] = data['rates']

    return render_template('base.html')

@app.route('/convert', methods=['POST'])
def convert():
    if float(request.form['amount']) < 1:
        flash("Not a valid amount", "error")
    else:
        amount = request.form['amount']
        cFrom = session['data'][f"{request.form['from']}"]
        cTo = session['data'][f"{request.form['to']}"]

        session['amount'] = amount
        session['fromCode'] = request.form['from']
        session['toCode'] = request.form['to']

        session['rate'] = round((cTo / cFrom) * float(amount), 2)

        flash(f"{session['amount']} {session['fromCode']} is equal to {session['rate']} {session['toCode']}", 'success')
    


    return redirect('/')
    
    

    


    