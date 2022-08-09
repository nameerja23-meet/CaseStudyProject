from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config={
	"apiKey": "AIzaSyCSGTfHg1EzMQootZldniM4bVzl2q5bAqE",
	"authDomain": "casestudyproje.firebaseapp.com",
	"databaseURL": "https://casestudyproje-default-rtdb.europe-west1.firebasedatabase.app",
	"projectId": "casestudyproje",
	"storageBucket": "casestudyproje.appspot.com",
	"messagingSenderId": "475964335933",
	"appId": "1:475964335933:web:a0eb145ccebac19be80754",
	"measurementId": "G-MPPTM5CX0T"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'fsoifj23423@#$sdfj#%#$)@48*(*)spwv@#$@#@2849238dfskjfw'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/donate')
def information():
    return render_template('information.html')

 

@app.route('/form', methods =['GET', 'POST'])
def donate():
	error=''
	if request.method == 'POST':
		try:
			email = request.form['email']
			fName = request.form['fname']
			lName = request.form['lname']
			bDay = request.form['bDay']
			sex = request.form['sex']
			phone = request.form['phone']
			bloodType = request.form['bloodType']
			donatedBefore = request.form['donatedBefore']
			city = request.form['city']
			lastReaction = request.form['lastReaction']
			user = {'email': email, 'fullName': fName, 'lastName': lName, 'birthday': bDay, 'sex': sex, 'bloodType':bloodType, 'donatedBefore': donatedBefore, 'city': city, 'phone':phone, 'lastReaction':lastReaction}
			db.child('Donors').push(user)
			error ='success'
		except:
			return render_template('form.html')
	return render_template('form.html')
	
if __name__ == '__main__':
	app.run(debug =True)