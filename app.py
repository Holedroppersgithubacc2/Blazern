import psycopg2
from dotenv import load_dotenv
import os
import sys
from flask import Flask, render_template, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)


@app.route('/home')
@app.route('/')
def home():
    return render_template('_about.html')

@app.route('/about')
def about():
    return render_template('_about.html')  # HOME PAGE

@app.route('/features')
def Features():
    return render_template('features.html')  # FEATURES PAGE

@app.route('/timer')
def timer():
    return render_template('timer.html')

@app.route('/brainstorm')
def brainstorm():
    return render_template('brainstorm.html')

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')


@app.errorhandler(404) # IF URL IS NOT VALID

def page_not_found(e):

    return render_template('_404notfound.html'), 404

if __name__ == '__main__':

    app.run(debug=True)









