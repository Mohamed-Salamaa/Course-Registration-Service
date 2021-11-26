from operator import mod
from app import db
from flask_restx import Resource, fields , reqparse , Namespace
from flask import  Blueprint,jsonify , request
from .routes import Course_Management_namespace
from app.models.registration import Registration  
from .student_api import student_model
from .course_api import course_model 


model = Course_Management_namespace.model('courseStudent_model', {'student_id': fields.Integer, 'student' : fields.Nested(student_model) , 'course_id': fields.Integer , 'course' : fields.Nested(course_model)})
model1 = Course_Management_namespace.model('Coursestudent_model' , {'student_id' : fields.Integer , 'course_id' : fields.Integer})

parser = reqparse.RequestParser()
parser.add_argument('student_id' , type =int)
parser.add_argument('course_id' , type=int)


@Course_Management_namespace.route('/registration')
class CoursesstudentsResource(Resource):

    # Get All Courses from DB
    @Course_Management_namespace.marshal_list_with(model)
    def get(self):
        coursestudents_list = Registration.query.all()
        print(coursestudents_list)
        return coursestudents_list

    # Post a Course To DB
    @Course_Management_namespace.expect(model1)
    @Course_Management_namespace.marshal_with(model)
    def post(self):

        args = request.json
        new_coursestudent = Registration(args['student_id'] , args['course_id'])

        # print(new_coursestudent)
        db.session.add(new_coursestudent)
        db.session.commit()

        return new_coursestudent