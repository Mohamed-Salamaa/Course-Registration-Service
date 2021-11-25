from app import db 


class Courses(db.Model):
    id = db.Column(db.Integer , primary_key = True , autoincrement = True)

    student_id = db.Column(db.Integer , db.ForeignKey('student.id'))
    student = db.relationship("Student", lazy='select')

    course_id = db.Column(db.Integer , db.ForeignKey('course.id'))
    course = db.relationship("Course", lazy='select')

    def __init__(self , student_id , course_id):
        self.student_id = student_id
        self.course_id = course_id
        
# courses = db.Table('courses',
# db.Column('student_id' , db.Integer , db.ForeignKey('student.id') , primary_key = True),
# db.Column('course_id' , db.Integer , db.ForeignKey('course.id'), primary_key = True)
# )
        


