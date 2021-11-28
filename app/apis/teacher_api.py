from urllib import parse
from app import db
from flask_restx import Resource , fields , reqparse 
from flask import jsonify , request

from app.models.teacher import Teacher
from .routes import Teacher_Management_namespace

teacher_model = Teacher_Management_namespace.model('teacher_model' , {'id' : fields.String , 'teacher_name' : fields.String , 'teacher_email' : fields.String , 'teacher_phone' : fields.String})

# parser = reqparse.RequestParser()
# parser.add_argument('teacher_name' , type = str)
# parser.add_argument('teacher_email' , type = str)
# parser.add_argument('teacher_phone' , type = int)


@Teacher_Management_namespace.route('/teacher')
class TeachersResource(Resource):


    @Teacher_Management_namespace.marshal_list_with(teacher_model)
    def get(self):
        teacher_list = Teacher.query.all()

        return teacher_list
    

    @Teacher_Management_namespace.expect(teacher_model)
    @Teacher_Management_namespace.marshal_with(teacher_model)
    def post(self):

        args = request.json
        new_teacher = Teacher(args['teacher_name'] , args['teacher_email'] , args['teacher_phone'])
        db.session.add(new_teacher)
        db.session.commit()
        
        return new_teacher
    

@Teacher_Management_namespace.route('/teacher/<int:id>')
class TeacherResource(Resource):

    @Teacher_Management_namespace.marshal_list_with(teacher_model)
    def get(self , id ):
        teacher_obj = Teacher.query.filter_by(id = id ).first()
        return teacher_obj 
        # jsonify({'teacher_name' : teacher_obj.teacher_name , 'teacher_email' : teacher_obj.teacher_email , 'teacher_phone' : teacher_obj.teacher_phone})


    @Teacher_Management_namespace.expect(teacher_model)
    @Teacher_Management_namespace.marshal_with(teacher_model)
    def put (self , id ):
        args = request.json
        Teacher.query.filter_by(id = id).update({'teacher_name' : args['teacher_name'] , 'teacher_email' : args['teacher_email'] , 'teacher_phone' : args['teacher_phone']})
        db.session.commit()

        teacher = Teacher.query.filter_by(id = id).first()

        return teacher
    

    def delete(self , id):
        Teacher.query.filter_by(id = id).delete()
        db.session.commit()
        
        return jsonify({"message" : "Teacher Deleted"})

