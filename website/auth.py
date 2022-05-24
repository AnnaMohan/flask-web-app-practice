from distutils.log import error
from hashlib import sha256
from xmlrpc.client import boolean
from flask import Blueprint, flash, request, render_template, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from website import views
from . import db
from website.models import User

auth = Blueprint('auth', __name__)  

@auth.route('/login', methods= ['GET','POST'])
def login():
    #return "<h1>Login</h1>"
    return render_template("login.html", text = 'Testing the value,varible passing using Jinja template', boolean = True)

@auth.route('/logout')
def logout():
    return "<h1>Logout</h1>"

@auth.route('/sign-up', methods= ['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
    
        if len(email) < 4:
            # you can name category as yours wish
            # flash is a functionality provided by flask
            flash("Email should be greater than 3 characters", category="error")
        elif len(first_name) < 2:
            flash("fristName should be greater than 1 character", category="error")
        elif len(password1) < 7:
            flash("Password should be greater than 6 characters", category="error")
        elif password1 != password2:
            flash("Passwords don't match", category=error)
        else:
            # add user to the database
            new_user = User(email= email,first_name = first_name, password = generate_password_hash(password1, method = 'sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("Account Created!!",category='Success')
            # after susccessfully creating the uesr we need to redirect the user to homepage 
            redirect(url_for('views.home')) # use can also directly say '/' but in future if  you change the route then you need to 
            #change it here as well so reocmmended way is to call the homepage function in this way.
    

    return render_template("sign_up.html")