from . import db

class UserProfiles(db.Model):
    id = db.Column(db.Integer,autoincrement=True)
    firstname=db.Column(db.String(20))
    lastname=db.Column(db.String(20))
    gender=db.Column(db.String(6))
    age=db.Column(db.Integer)
    bio=db.Column(db.String(200))
    profpic=db.Column(db.String(50))
    username=db.Column(db.String(20), primary_key=True)
    date_created=db.Column(db.Date)
    
    def __init__(self,id,firstname,lastname,username,gender,age,bio,profpic,date_created):
        self.id=id
        self.firstname=firstname
        self.lastname=lastname
        self.username=username
        self.gender=gender
        self.age=age
        self.bio=bio
        self.profpic=profpic
        self.date_created=date_created