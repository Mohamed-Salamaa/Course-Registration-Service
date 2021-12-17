from flask import request
from functools import wraps
import jwt
from app import app
from app.models import *



def token_required(f):
    @wraps(f)
    def decorated(*args , **kwargs):
        token = None

        if 'X-API-KEY' in request.headers:
            token = request.headers['X-API-KEY']
            print(token)
        if not token:
            return ({'message' : 'token is missing'}) , 401
        
        try:
            data = jwt.decode(token , app.config['SECRET_KEY'])
            current_user = User.query.filter_by(email = data['email']).first()
            
            if not current_user:

                return ({'message' : 'token is not valid'})

        except:
            return ({'message' : 'token is not vaild'}),401
        
        return f(*args , **kwargs)

    return decorated