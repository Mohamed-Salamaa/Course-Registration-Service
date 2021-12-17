from werkzeug import security
from app import db
from flask import request 
from flask_restx import Resource , fields
from werkzeug.security import generate_password_hash
from app.models.user import User
from .routes import User_Management_namespace
from .decorators import token_required

user_model = User_Management_namespace.model('user_model', 
{'id' : fields.String ,
'name' : fields.String ,
'email' :fields.String ,
'password' : fields.String,
'admin' : fields.Boolean})

@User_Management_namespace.route('')
@User_Management_namespace.doc(security='apikey')   
class UsersResource(Resource):

    
    @User_Management_namespace.marshal_list_with(user_model)
    @token_required
    def get(self):
        user_list = User.query.all()
        print(user_list)
        return user_list

    @User_Management_namespace.expect(user_model)
    @User_Management_namespace.marshal_with(user_model)
    @token_required
    def post(self):
        args = request.json
        hashed_password = generate_password_hash(args['password'] , method='sha256')
        new_user = User(args['name'] , args['email'] , hashed_password ,args['admin'])
        db.session.add(new_user)
        db.session.commit()
        return new_user

@User_Management_namespace.route('/<int:id>')
@User_Management_namespace.doc(security='apikey')   
class UserResource(Resource):

    @User_Management_namespace.marshal_list_with(user_model)
    @token_required
    def get(self , id):
        user_obj = User.query.filter_by(id = id).first()
        return user_obj
    
    @User_Management_namespace.expect(user_model)
    @User_Management_namespace.marshal_with(user_model)
    @token_required
    def put(self ,id):
        args = request.json
        hashed_password = generate_password_hash(args['password'] , method='sha256')
        User.query.filter_by(id=id).update({'name': args['name'] , 'email':args['email'] , 'passwor' : hashed_password  , 'admin' :args['admin']})
        db.session.commit()
        user = User.query.filter_by(id=id).first()
        return user
    
    def delete(self , id):
        User.query.filter_by(id=id).delete()
        db.session.commit()

        return ({"message: ": 'User Deleted'})
