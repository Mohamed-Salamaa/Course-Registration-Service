from app import db
from flask_restx import Resource, fields , reqparse , Namespace
from app.models.student import Student
from flask import jsonify
from .routes import Student_Management_namespace

model = Student_Management_namespace.model('student_model', {'name': fields.String, 'email': fields.String,})

parser = reqparse.RequestParser()
parser.add_argument('name' , type =str)
parser.add_argument('email' , type=str)


@Student_Management_namespace.route('/student')
class StudentsResource(Resource):

    # Get All Student from DB
    @Student_Management_namespace.marshal_list_with(model)
    def get(self):
        student_list = Student.query.all()

        print(student_list)
        return student_list

    # Post a Student To DB
    @Student_Management_namespace.expect(parser)
    def post(self):

        args = parser.parse_args()
        new_student = Student(args['name'] , args['email'])
        print(new_student)
        db.session.add(new_student)
        db.session.commit()

        return jsonify({"message" : "Student Added"})


@Student_Management_namespace.route('/student/<int:id>')
class StudentResource(Resource):

    # Get Student by ID 
    def get(self , id ):
        student_obj = Student.query.filter_by(id = id).first()
        return jsonify({'name' : student_obj.name , 'email' : student_obj.email , })

    # To Update on a Student
    @Student_Management_namespace.expect(parser)
    def put (self , id):
        args = parser.parse_args()
        Student.query.filter_by(id = id).update({'name' : args['name'] , 'email' : args['email']})
        db.session.commit()

        return jsonify({"message" : "Student Updated"})

    # To Delete a Student
    def delete (self , id):        
        Student.query.filter_by(id = id ).delete()
        db.session.commit()

        return jsonify({"message" : "Student Deleted"})