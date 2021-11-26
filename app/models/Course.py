from app import db 


class Course(db.Model):

    id = db.Column (db.Integer , primary_key = True , autoincrement = True)
    title = db.Column (db.String(100) , nullable = False)
    price =  db.Column (db.String(150) , nullable = False)
    teacher_id = db.Column(db.Integer , db.ForeignKey('teacher.id') , nullable = False)

    teacher = db.relationship('Teacher', backref='course')

    def __init__(self , title , price , teacher_id):
        self.title = title
        self.price = price
        self.teacher_id = teacher_id
