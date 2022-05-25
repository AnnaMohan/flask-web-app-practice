from distutils.log import error
from hashlib import sha256
from xmlrpc.client import boolean
from flask import Blueprint, flash, request, render_template, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from website import views
from . import db
from website.models import User
from flask_login import login_user, logout_user, login_required , current_user 

auth = Blueprint('auth', __name__)  

@auth.route('/login', methods= ['GET','POST'])
def login():
    #return "<h1>Login</h1>"
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # check the databse whelther a user with the email given is present or not
        # by using the query.filter_by(use_attribute_you_want_to_check_With)  .first()
        # .first means the first result 
        # we need to get one result becoz all the emails in the databse need to be unique
        user = User.query.filter_by(email=email).first()
        if user:
            # here we are taking the password associated with the user's email and passing to check_password_hash
            # function and by saying user.password and password which we got from user 
            # the user given password is hashed by this function and the previously hashed password
            # whihc is made while signing up will be matched if matched print successfull
            if check_password_hash(user.password, password):
                flash('Logged in successfully',category='sucess')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.',category='error')
        else:
            flash('Email does not exits',category='error')
    return render_template("login.html", text = 'Testing the value,varible passing using Jinja template', boolean = True)

@auth.route('/logout')
@login_required # using this @login_required decorator,just to make sure logging out the logged in user # even with out this it works
def logout():
    logout_user() # this function call simply logs out the user
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods= ['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists',category='error')
        elif len(email) < 4:
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
            login_user(user, remember=True)
            flash("Account Created!!",category='Success')
           
            # after susccessfully creating the uesr we need to redirect the user to homepage 
            return redirect(url_for('views.home')) # use can also directly say '/' but in future if  you change the route then you need to 
            #change it here as well so reocmmended way is to call the homepage function in this way.
    

    return render_template("sign_up.html")