from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api

authorization = {'apikey' : {
    'type' : 'apiKey',
    'in' : 'header' ,
    'name' : 'X-API-KEY'
}}

app = Flask(__name__  )
api = Api(app , title='Course System' , authorizations= authorization )

app.config['SECRET_KEY'] ='mysecretkey' # To use encoding with my token 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mohamed:root@localhost:5432/proj_course'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
migrate = Migrate (app ,db)

from app.models import *
from app.apis import *


api.add_namespace(Course_Management_namespace , path= '/course')
api.add_namespace(Student_Management_namespace, path= '/student')
api.add_namespace(Teacher_Management_namespace , path='/teacher')
api.add_namespace(User_Management_namespace , path='/user' )
api.add_namespace(Login_Management_namespace ,path='/login')
