from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api
from werkzeug.datastructures import Authorization


app = Flask(__name__)

# authorizations = {
#     'apikey': {
#         'type': 'apiKey',
#         'in': 'header',
#         'name': 'X-API-KEY'
#     }
# }

api = Api(app )


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mohamed:root@localhost:5432/proj_course'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
migrate = Migrate (app ,db)

from app.models import *
from app.apis import *

api.add_namespace(Course_Management_namespace , path= '/course')
api.add_namespace(Student_Management_namespace, path= '/Student') 
