from os import path
from venv import create
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialising the Databse
db = SQLAlchemy()
# Naming the database 
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ANY RANDOM STRING YOU WANT'
    # f'sqlite:///{DB_NAME}' --> this is the place where our database is stored.
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # connecting the flask app to the database
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

   # import .models  as models #  import .models throws an error becuase you can't say .models.User if you want to use something so 
    # we need to do it as import .models as models in this case there is no need to use period while refrencing something 
    # from models # even this is not working here
    # lets do it as
    from .models import User,Note

    create_database(app)

    return app

# creating the database
def create_database(app):
    # condition check if already exists nothing happens if not it will create a database
    if not path.exists('website/' + DB_NAME):
        # this app has SQLALCHEMY_DATABASE_URI where to create the database
        db.create_all(app=app)
        print("Created Databse !!")

