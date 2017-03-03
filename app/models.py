from . import db

class UserProfile(db.Model):
     id = db.Column(db.Integer, primary_key=True)