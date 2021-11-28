from werkzeug.wrappers import response
from app import  db
from flask_restx import Resource, fields , reqparse 
from flask import jsonify , request

from app.models.Course import Course
from .routes import Course_Management_namespace
from .teacher_api import teacher_model

course_model = Course_Management_namespace.model('course_model', {'id' : fields.String ,'title': fields.String, 'price': fields.String, 'teacher_id' : fields.String , 'teacher' : fields.Nested(teacher_model)})

@Course_Management_namespace.route('/course')
class CoursesResource(Resource):

    # Get All Courses from DB
    @Course_Management_namespace.marshal_list_with(course_model)
    def get(self):
        course_list = Course.query.all()
        return course_list

    # Post a Course To DB
    @Course_Management_namespace.expect(course_model)
    @Course_Management_namespace.marshal_with(course_model)
    def post(self):

        args = request.json
        new_course = Course(args['title'] , args['price'] , args['teacher_id'])
        db.session.add(new_course)
        db.session.commit()
        return new_course


@Course_Management_namespace.route('/course/<int:id>')
class CourseResource(Resource):

    # Get Course by ID 
    @Course_Management_namespace.marshal_list_with(course_model)
    def get(self , id ):
        course_obj = Course.query.filter_by(id = id).first()
        return course_obj 

    # To Update on a Course
    @Course_Management_namespace.expect(course_model)
    @Course_Management_namespace.marshal_with(course_model)
    def put (self , id):

        args = request.json
        Course.query.filter_by(id = id).update({'title' : args['title'] , 'price' : args['price'] , 'teacher_id' :args['teacher_id']})
        db.session.commit()
        course = Course.query.filter_by(id = id).first()
        return course

    # To Delete a Course
    def delete (self , id):        
        Course.query.filter_by(id = id ).delete()
        db.session.commit()

        return jsonify({"message" : "Course Deleted"})
