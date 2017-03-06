from app import app, db
import os, time
from flask import render_template, request, redirect, url_for, flash,jsonify
from forms import ProfileForm
from models import UserProfiles
from werkzeug.utils import secure_filename

def date():
    return time.strftime("%m %d %Y")

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/profiles', methods=["GET","POST"])
def profiles():
    userss=[]
    print request.method
    if request.method=="POST":
        users= db.session.query(UserProfiles).all()
        for user in users:
            userss.append(("username:"+user.username, "userid: "+str(user.id)))
        return jsonify(userss)
    users= db.session.query(UserProfiles).all()
    return render_template('profiles.html',users=users)
    
@app.route('/profile/<userid>',methods=["GET"])
def viewprof(userid):
    users= db.session.query(UserProfiles).filter_by(username=userid)
    return render_template('viewprof.html',users=users)

@app.route('/profile',methods=['POST','GET'])
def createprof():
    
    pform=ProfileForm()
    file_folder = app.config['UPLOAD_FOLDER']
    # date=date()
    if request.method=='POST':
        firstname=pform.firstname.data
        lastname=pform.lastname.data
        username=pform.username.data
        age=pform.age.data
        gender=pform.gender.data
        bio=pform.bio.data
        profpic=request.files['profpic']
        if profpic and allowed_file(profpic.filename):
            picname= secure_filename(profpic.filename)
            path="/static/uploads/"+ picname
            profpic.save("./app"+path)
            profpic=path
            prof= UserProfiles(firstname,lastname,username,gender,age,bio,profpic,date())
            db.session.add(prof)
            db.session.commit()
            return redirect (url_for('home'))
    return render_template('createProf.html',form=pform)
    
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

