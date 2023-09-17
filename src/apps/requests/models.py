from src.extensions.db import db

class Requests(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    
    name = db.Column(db.String(20))
    
    mount = db.Column(db.Integer())
    reason = db.Column(db.Text())

    discount = db.Column(db.String(20))
    deadlines = db.Column(db.Integer())
    location = db.Column(db.String(20))
    state = db.Column(db.String(20))
    