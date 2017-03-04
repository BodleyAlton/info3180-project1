from . import db

class UserProfiles(db.Model):
    id = db.Column(db.Integer,autoincrement=True, primary_key=True)
    firstname=db.Column(db.String(20))
    lastname=db.Column(db.String(20))
    gender=db.Column(db.String(6))
    age=db.Column(db.Integer)
    bio=db.Column(db.String(200))
    profpic=db.Column(db.String(50))
    date_created=db.Column(db.Date)
    
    def __init__(self,firstname,lastname,gender,age,bio,profpic,date_created):
        self.firstname=firstname
        self.lastname=lastname
        self.gender=gender
        self.age=age
        self.bio=bio
        self.profpic=profpic
        self.date_created=date_created