from app import app, db
import os, time,json
from flask import render_template, request, redirect, url_for, flash,jsonify, make_response
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
    xl=[]
    p={}
    i=0
    print request.method
    if request.method=="POST":
        users= db.session.query(UserProfiles).all()
        for user in users:
            p={'username':user.username,'userid':str(user.id)}
            userss.insert(i,p)
            i+=1
        x={'users':jsonify(userss)}
        xl.insert(0,x)
        print x
        # return jsonify(x)
        return jsonify(userss)
    users   = db.session.query(UserProfiles).all()
    for user in users:
        userss.append((user.firstname, user.username))
    return render_template('profiles.html',users=users)
    
@app.route('/profile/<userid>',methods=["GET","POST"])
def viewprof(userid):
    userr={}
    i=0
    if request.method=='POST':
        users= db.session.query(UserProfiles).filter_by(username=userid)
        for user in users:
            p={'userid':str(user.id),'username':user.username, 'image':user.profpic,'gender':user.gender,'age':str(user.age),'profile_created_on':user.date_created}
            # userr.insert(i,p)
            i+=1
        return jsonify(p)
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
            prof= UserProfiles(1,firstname,lastname,username,gender,age,bio,profpic,date())
            db.session.add(prof)
            db.session.commit()
            return redirect (url_for('home'))
    return render_template('createProf.html',form=pform)
    
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

