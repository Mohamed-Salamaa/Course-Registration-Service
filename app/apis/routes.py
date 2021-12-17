from flask_restx import Namespace


Course_Management_namespace = Namespace('Courses', description= 'Courses related Opreations')  

Student_Management_namespace = Namespace ('Students' , description= 'Students related Operations')

Teacher_Management_namespace = Namespace ('Teachers' , description= 'Teachers related Operations')

User_Management_namespace = Namespace ('Users' , description= 'Teachers related Operations')

Login_Management_namespace = Namespace ('Login' , description= 'Login Operations')
