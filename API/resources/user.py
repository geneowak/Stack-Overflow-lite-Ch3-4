from flask_restful import Resource, reqparse
from API.models.user import UserModel


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
