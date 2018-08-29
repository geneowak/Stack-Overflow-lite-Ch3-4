from flask_restful import Resource, reqparse
from API.models.user import UserModel
from flask_jwt_extended import create_access_token


class RegisterUser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', 
        type=str, required=True, help="Username field can't be left blank"
    )
    parser.add_argument('password',
        type=str, required=True, help="Password field can't be left blank"
    )
    
    def post(self):
        data = RegisterUser.parser.parse_args()
        if UserModel.get_user_by_username(data['username']):
            return {
                "message": "User {} already exists".format(data['username'])
            }, 400
        
        user = UserModel(data['username'],data['password'])
        if user.add_user():
            return { "message": "User created successfully"}, 201
        return {"message": "The was a problem registering user"}, 500


class Login(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', 
        type=str, required=True, help="Username field can't be left blank"
    )
    parser.add_argument('password',
        type=str, required=True, help="Password field can't be left blank"
    )

    def post(self):

        data = Login.parser.parse_args()
        user = UserModel.get_user_by_username(data['username'])
        if not user:
            return {
                "message": "Wrong username or password"
            }, 401
        if user.password == data['password']:
            access_token = create_access_token(user.user_id)
            return {'access_token': access_token}, 200
        else:
            return {
                "message": "Wrong username or password"
            }, 401
