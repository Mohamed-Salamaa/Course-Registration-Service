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

import os, secrets

# Secrets and DB config from env vars (with safe defaults)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', secrets.token_urlsafe(32))

db_user = os.getenv('DB_USER', '')
db_pass = os.getenv('DB_PASSWORD', '')
db_host = os.getenv('DB_HOST', 'localhost')
db_port = os.getenv('DB_PORT', '5432')
db_name = os.getenv('DB_NAME', 'Course-Registration-Service')

if os.getenv('DATABASE_URL'):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
else:
    # Build URI only if user/pass provided; otherwise rely on peer/local auth
    credentials = f"{db_user}:{db_pass}@" if db_user and db_pass else ""
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{credentials}{db_host}:{db_port}/{db_name}"

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
