from app import app, db
import os, time
from flask import render_template, request, redirect, url_for, flash
from forms import ProfileForm
from models import UserProfiles
from werkzeug.utils import secure_filename

def date():
    return time.strftime("%m %d %Y")

@app.route('/createprof',methods=['POST','GET'])
def createprof():
    
    pform=ProfileForm()
    file_folder = app.config['UPLOAD_FOLDER']
    # date=date()
    if request.method=='POST':
        firstname=pform.firstname.data
        lastname=pform.lastname.data
        age=pform.age.data
        gender=pform.gender.data
        bio=pform.bio.data
        profpic=request.files['profpic']
        print age
        print "Age ABOVE"
        if profpic and allowed_file(profpic.filename):
            picname= secure_filename(profpic.filename)
            profpic.save(os.path.join(file_folder, picname))
            profpic=os.path.join(file_folder, picname)
            # profpic= lo_import(os.path.join(file_folder, picname)
            prof= UserProfiles(firstname,lastname,gender,age,bio,profpic,date())
            print prof.age
            print "Lname: "+lastname
            print age
            print "gender: "+gender
            print "Bio: "+bio
            print "Path: "+profpic
            print "Date: "+date()
            db.session.add(prof)
            db.session.commit()
        
    return render_template('createProf.html',form=pform)
    
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

