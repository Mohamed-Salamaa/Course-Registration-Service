from flask_restx import Namespace


Course_Management_namespace = Namespace('Courses Management', description= 'Courses related Opreations')  

Student_Management_namespace = Namespace ('Students Management' , description= 'Students related Operations')

Teacher_Management_namespace = Namespace ('Teachers Management' , description= 'Teachers related Operations')