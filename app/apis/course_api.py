from app import  db
from flask_restx import Resource, fields , reqparse 
from flask import jsonify , request

from app.models.Course import Course
from .routes import Course_Management_namespace

teacher_model = Course_Management_namespace.model('teacher_model' ,{'id' : fields.Integer , 'teacher_name' : fields.String})
course_model = Course_Management_namespace.model('course_model', {'id' : fields.Integer ,'title': fields.String, 'price': fields.Integer, 'teacher_id' : fields.Integer , 'teacher' : fields.Nested(teacher_model)})

parser = reqparse.RequestParser()
parser.add_argument('title' , type =str)
parser.add_argument('price' , type=int)
parser.add_argument('teacher' , type = str)

@Course_Management_namespace.route('/course')
class CoursesResource(Resource):

    # Get All Courses from DB
    @Course_Management_namespace.marshal_list_with(course_model)
    def get(self):
        course_list = Course.query.all()

        # print(course_list)
        return course_list

    # Post a Course To DB
    @Course_Management_namespace.expect(course_model)
    @Course_Management_namespace.marshal_with(course_model)
    def post(self):

        args = request.json
        new_course = Course(args['title'] , args['price'] , args['teacher_id'])
        db.session.add(new_course)
        db.session.commit()

        # return jsonify({"message" : "Course Added"})
        return new_course


@Course_Management_namespace.route('/course/<int:id>')
class CourseResource(Resource):

    # Get Course by ID 
    def get(self , id ):
        course_obj = Course.query.filter_by(id = id).first()
        return jsonify({'title' : course_obj.title , 'price' : course_obj.price})

    # To Update on a Course
    @Course_Management_namespace.expect(course_model)
    def put (self , id):
        args = parser.parse_args()
        Course.query.filter_by(id = id).update({'title' : args['title'] , 'price' : args['price'] , 'teahcer_id' :args['teacher_id']})
        db.session.commit()

        return jsonify({"message" : "Course Updated"})

    # To Delete a Course
    def delete (self , id):        
        Course.query.filter_by(id = id ).delete()
        db.session.commit()

        return jsonify({"message" : "Course Deleted"})
