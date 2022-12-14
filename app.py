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
    return render_template('donation_start.html')

 

@app.route('/confirm/<num>')
def confirm(num):
    return render_template('donation_num.html', num = num)

@app.route('/press')
def press():
    return render_template("Press.html")

@app.route('/join_us')
def join_us():
    return render_template("Join_Us.html")

@app.route('/blog')
def blog():
    return render_template("Blog.html")


@app.route('/form', methods =['GET', 'POST'])
def donate():
    if request.method == 'POST':
        # try:
        email = request.form['email']
        fName = request.form['fname']
        bDay = request.form['bDay']
        sex = request.form['sex']
        phone = request.form['phone']
        bloodType = request.form['bloodType']
        city = request.form['city']
        lastReaction = request.form['lastReaction']
        uni = request.form['uni']
        user = {'email': email, 'fullName': fName, 'birthday': bDay, 'sex': sex, 'bloodType':bloodType, 'city': city, 'phone':phone, 'lastReaction':lastReaction, 'uni' : uni}
        
        i = 1

        if(db.shallow().get().val() != None and 'Donors' in db.shallow().get().val()):
            donors = db.child('Donors').shallow().get().val()
            while (uni+str(i) in donors):
                i+=1

        db.child("Donors").child(uni+str(i)).set(user)
        # except:
        #     return render_template('donation_form.html')
        return redirect(url_for('confirm', num = uni+str(i)))
    return render_template('donation_form.html')
	

@app.route('/adminlogin', methods = ['GET', 'POST'])
def adminLogin():
    if request.method =='POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email,password)
            return redirect(url_for('admin'))
        except:
            error = 'Authentication failed'
            return render_template('adminlogin.html', error =error)
    return render_template('adminlogin.html')

@app.route('/stats', methods = ['GET', 'POST'])
def stats():
    stats = {'TEC':0,'TAU':0,'BGU':0,'HUJ':0,'BIU':0}
    donors = db.child('Donors').shallow().get().val()
    for uni in ['TEC','TAU','BGU','HUJ','BIU']:
        for i in donors:
            if uni in i:
                stats[uni] +=1
    if request.method == "POST":
        name = request.form["name"]
        if name in db.child('Donors').shallow().get().val():
            return render_template('admin.html', stats = stats, donor = db.child('Donors').child(name).get().val())
    return render_template('admin.html', stats = stats)


@app.route('/admin', methods = ['GET', 'POST'])
def admin():
    if 'user' in login_session:
        if login_session['user'] is not None:
            return redirect(url_for('stats'))
        else:
            return redirect(url_for("adminLogin"))
    else:
        return redirect(url_for("adminLogin"))
if __name__ == '__main__':
	app.run(debug =True)