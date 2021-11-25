from app import db 

class Student(db.Model):

    id = db.Column (db.Integer , primary_key = True , autoincrement = True)
    name = db.Column (db.String(100) , nullable = False)
    email =  db.Column (db.String(150) , nullable = False)
    #studentcourses = db.relationship('Course' , secondary= courses , backref='stcourses')

    def __init__(self , name , email):
        self.name = name
        self.email = email