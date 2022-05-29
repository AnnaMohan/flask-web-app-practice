
import json
from flask import Blueprint, flash, jsonify,render_template, request
from flask_login import  login_required , current_user 
from .models import Note
from . import db

views = Blueprint('views', __name__)  

@views.route('/',methods = ['GET','POST'])
@login_required # @login_required this decorator says a user must be logged into to view the homepage
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Length of the note is too small',category='error')
        else:
            # creating a new object named new_note to the Note class
            new_note = Note(data = note,user_id = current_user.id)
            #adding the new_note into the database
            db.session.add(new_note)
            # updating the database
            db.session.commit()
            flash('Note added sucessfully',category='success')
        # passing user=current_user to pass the info to the home.html
    return render_template("home.html", user=current_user)

@views.route('/delete-note',methods=['POST'])
def delete_note():
    note  = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})