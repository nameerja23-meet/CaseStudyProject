from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config={
    "apiKey": "AIzaSyCSGTfHg1EzMQootZldniM4bVzl2q5bAqE",
    "authDomain": "casestudyproje.firebaseapp.com",
    "projectId": "casestudyproje",
    "storageBucket": "casestudyproje.appspot.com",
    "messagingSenderId": "475964335933",
    "appId": "1:475964335933:web:a0eb145ccebac19be80754",
    "measurementId": "G-MPPTM5CX0T",
    "databaseURL" : "https://casestudyproje-default-rtdb.europe-west1.firebasedatabase.app/"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'fsoifj23423@#$sdfj#%#$)@48*(*)spwv@#$@#@2849238dfskjfw'

@app.route('/')
def index():
    return render_template('index.html')