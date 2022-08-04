from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config={

}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'fsoifj23423@#$sdfj#%#$)@48*(*)spwv@#$@#@2849238dfskjfw'

@app.route('/')
def index():
    return render_template('index.html')