from flask_restx.inputs import email
from app import app , db
from flask import request , make_response , jsonify
from werkzeug.security import check_password_hash
from flask_restx import Resource
from app.models.user import User
from .routes import Login_Management_namespace
import jwt
import datetime


@Login_Management_namespace.route('')
class UserLogin(Resource):

    def get(self):
        auth = request.authorization

        if not auth or not auth.username or not auth.password:
            return make_response('Could not Verfiy' , 401 , {'WWW-Authenticate' :'Basic realm="Login Required"'})
        
        user = User.query.filter_by(email = auth.username).first()

        if not user:
            return make_response('Could not Verfiy' , 401 , {'WWW-Authenticate' :'Basic realm="Login Required"'})
            
        if check_password_hash(user.password , auth.password):
            token = jwt.encode({'email' : user.email , 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)} , app.config['SECRET_KEY'])
            
            User.query.filter_by(email=auth.username).update({'token' : token.decode('UTF-8')})
            db.session.commit()

            return jsonify({'token' : token.decode('UTF-8')})
        
        return make_response('Could not Verfiy' , 401 , {'WWW-Authenticate' :'Basic realm="Login Required"'})
