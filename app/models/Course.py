from app import db 


class Course(db.Model):

    id = db.Column (db.Integer , primary_key = True , autoincrement = True)
    title = db.Column (db.String(100) , nullable = False)
    price =  db.Column (db.String(150) , nullable = False)


    def __init__(self , title , price):
        self.title = title
        self.price = price
