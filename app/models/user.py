from enum import unique
from app import db

class User(db.Model):
    id = db.Column (db.Integer , primary_key = True , autoincrement = True)
    public_id = db.Column(db.String(50),unique=True)
    name = db.Column (db.String(100) , nullable = False)
    email =  db.Column (db.String(150) , nullable = False)
    password = db.Column(db.String(100) , nullable = False)
    admin = db.Column(db.Boolean)
    token = db.Column(db.String(400) ,nullable = True)

    def __init__(self , name , email , password , admin ):
        self.name = name
        self.email = email
        self.password = password
        self.admin = admin
        
