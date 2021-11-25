from app import  db
from flask_restx import Resource, fields , reqparse , Namespace
from flask import jsonify

from app.models.Course import Course
from .routes import Course_Management_namespace

model = Course_Management_namespace.model('course_model', {'title': fields.String, 'price': fields.Integer,})

parser = reqparse.RequestParser()
parser.add_argument('title' , type =str)
parser.add_argument('price' , type=int)


@Course_Management_namespace.route('/course')
class CoursesResource(Resource):

    # Get All Courses from DB
    @Course_Management_namespace.marshal_list_with(model)
    def get(self):
        course_list = Course.query.all()

        print(course_list)
        return course_list

    # Post a Course To DB
    @Course_Management_namespace.expect(parser)
    def post(self):

        args = parser.parse_args()
        new_course = Course(args['title'] , args['price'])
        db.session.add(new_course)
        db.session.commit()

        return jsonify({"message" : "Course Added"})


@Course_Management_namespace.route('/course/<int:id>')
class CourseResource(Resource):

    # Get Course by ID 
    def get(self , id ):
        course_obj = Course.query.filter_by(id = id).first()
        return jsonify({'title' : course_obj.title , 'price' : course_obj.price})

    # To Update on a Course
    @Course_Management_namespace.expect(parser)
    def put (self , id):
        args = parser.parse_args()
        Course.query.filter_by(id = id).update({'title' : args['title'] , 'price' : args['price']})
        db.session.commit()

        return jsonify({"message" : "Course Updated"})

    # To Delete a Course
    def delete (self , id):        
        Course.query.filter_by(id = id ).delete()
        db.session.commit()

        return jsonify({"message" : "Course Deleted"})
