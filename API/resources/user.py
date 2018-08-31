from flask_restful import Resource, reqparse
from API.models.user import UserModel
from API.models.question import Question
from API.models.answer import Answer
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from .utilities import validate_email, validate_password, validate_username, username_requirements, password_requirements


class RegisterUser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', 
        type=str, required=True, help="Username field can't be left blank"
    )
    parser.add_argument('password',
        type=str, required=True, help="Password field can't be left blank"
    )
    
    def post(self):

        RegisterUser.parser.add_argument('email',
            type=str, required=True, help="Email field can't be left blank"
        )
        data = RegisterUser.parser.parse_args()
        username = data['username'].strip().lower()
        password = data['password'].strip().lower()
        email = data['email'].strip().lower()
        
        if not username:
            return {"message": "username must not be blank"}, 400

        if not password:
            return {"message": "password must not be blank"}, 400

        if not email:
            return {"message": "email must not be blank"}, 400

        if not validate_username(username):
            return {"message": "username doesn't meet requirements: {}".format(username_requirements)}, 400

        if not validate_email(email):
            return {"message": "email is invalid."}, 400

        if not validate_password(password):
            return {"message": "password doesn't meet requirements: {}".format(password_requirements)}, 400

        if UserModel.get_user_by_username(username):
            return {
                "message": "User '{}' already exists".format(username)
            }, 400

        if UserModel.get_user_by_email(email):
            return {
                "message": "Sorry, email '{}' already exists".format(email)
            }, 400
        
        user = UserModel(username, password, email=email)
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
        username = data['username'].strip().lower()
        password = data['password'].strip().lower()

        if not username:
            return {"message": "username must not be blank"}, 400

        if not password:
            return {"message": "password must not be blank"}, 400

        user = UserModel.get_user_by_username(username)

        if not user:
            return {"message": "Wrong username or password"}, 401
            
        if user.password == password:
            access_token = create_access_token(user.user_id)
            return {
                'access_token': access_token,
                'message': "Login successful"
            }, 200
        else:
            return {"message": "Wrong username or password"}, 401


class UserQuestions(Resource):
    """ this method handles user questions """
    @jwt_required
    def get(self):
        """ this method gets questions asked by the user """
        return {"questions": Question.get_questions_by_user_id(get_jwt_identity())}
        
class UserAnswers(Resource):
    
    @jwt_required
    def get(self):
        """ this method gets questions asked by the user """
        return {"answers": Answer.get_answers_by_user_id(get_jwt_identity())}
        
