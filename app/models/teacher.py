from app import db

class Teacher(db.Model):
    
    id = db.Column(db.Integer , primary_key = True , autoincrement = True)
    teacher_name = db.Column(db.String(200) , nullable = False)
    teacher_email = db.Column(db.String(200) , nullable = False)
    teacher_phone = db.Column(db.Integer , nullable = False)

    def __init__(self , teacher_name , teacher_email , teacher_phone):
        self.teacher_name = teacher_name
        self.teacher_email = teacher_email
        self.teacher_phone = teacher_phone
