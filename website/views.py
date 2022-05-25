from flask import Blueprint,render_template
from flask_login import  login_required , current_user 

views = Blueprint('views', __name__)  

@views.route('/')
@login_required # @login_required this decorator says a user must be logged into to view the homepage
def home():
    return render_template("home.html")