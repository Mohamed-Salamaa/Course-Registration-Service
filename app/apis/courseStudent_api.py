from app import db
from flask_restx import Resource, fields , reqparse , Namespace
from flask import  Blueprint,jsonify
from .routes import Course_Management_namespace
from app.models.courseStudent import Courses


student_model = Course_Management_namespace.model('student_model' , {'name' : fields.String })
course_model = Course_Management_namespace.model('course_model' , {'title' : fields.String})
model = Course_Management_namespace.model('courseStudent_model', {'student_id': fields.Integer, 'student' : fields.Nested(student_model) , 'course_id': fields.Integer , 'course' : fields.Nested(course_model)})

parser = reqparse.RequestParser()
parser.add_argument('student_id' , type =int)
parser.add_argument('course_id' , type=int)


@Course_Management_namespace.route('/coursestudent')
class CoursesstudentsResource(Resource):

    # Get All Courses from DB
    @Course_Management_namespace.marshal_list_with(model)
    def get(self):
        coursestudents_list = Courses.query.all()
        print(coursestudents_list)
        return coursestudents_list

    # Post a Course To DB
    @Course_Management_namespace.expect(parser)
    def post(self):

        args = parser.parse_args()
        new_coursestudent = Courses(args['student_id'] , args['course_id'])

        print(new_coursestudent)
        db.session.add(new_coursestudent)
        db.session.commit()

        return jsonify({"message" : "Course Added"})


# @api.route('/coursestudent/<int:id>')
# class CourseStudentResource(Resource):

#     # Get Course by ID 
#     def get(self , id ):
#         coursestudent_obj = CourseStudent.query.filter_by(id = id).first()
#         return jsonify({'student_id' : coursestudent_obj.student_id , 'course_id' : coursestudent_obj.course_id})

#     # To Update on a Course
#     @api.expect(parser)
#     def put (self , id):
#         args = parser.parse_args()
#         CourseStudent.query.filter_by(id = id).update({'student_id' : args['student_id'] , 'course_id' : args['course_id']})
#         db.session.commit()

#         return jsonify({"message" : "Course Updated"})

#     # To Delete a Course
#     def delete (self , id):        
#         CourseStudent.query.filter_by(id = id ).delete()
#         db.session.commit()

#         return jsonify({"message" : "Course Deleted"})
