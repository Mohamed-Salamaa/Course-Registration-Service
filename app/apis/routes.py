from flask_restx import Namespace


Course_Management_namespace = Namespace('CourseManagement', description= 'Courses related Opreations')  

Student_Management_namespace = Namespace ('StudentManagement' , description= 'Students related Operations')