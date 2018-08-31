from flask import Flask, request, render_template, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager

from API.resources.question import Questions, QuestionList
from API.resources.answer import Answers, AnswerList, UpdateAnswer
from API.resources.comment import CommentList, QuestionComments, AnswerComments
from API.resources.user import RegisterUser, Login

from API.database.db_handler import DbHandler

from API.config import app_config

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = "JDJDISGHKJDGHPOGHIHGKDFNHIHWT723BQE8T7YFIOQER0Q3TYIOVN"
jwt = JWTManager(app)

api = Api(app)

''' 
# end points to develop

GET /questions Fetch all questions
GET /questions/<questionId> | Fetch a specific question | This should come with the all  answers provided so far for the question.
POST /questions Add a question
POST /questions/<questionId>/answers Add an answer

POST /questions/<questionId>/comments Add an add a comment to a question
POST /answers/<answerId>/comments Add an add a comment to an answer


POST /auth/signup | Register a user
POST /auth/login | Login a user
Delete /questions/<questionId> | Delete a question | This endpoint should be available to the author’s author.
PUT /questions/<questionId>/answers/<answerId> | Mark an answer as accepted | available to only the question author.
PUT /questions/<questionId>/answers/<answerId> | update an answer. | available to only the answer author.

 '''

@app.before_first_request
def create_tables():
    ''' create all tables before first request '''
    dbHandle = DbHandler()
    dbHandle.create_tables()
    dbHandle.close_conn()
 
@app.route('/')
def get_def_page():
   return render_template('index.html')

""" custom error handlers """
@app.errorhandler(404)
def page_not_found(error):
    return jsonify({'message': "Page not found. If you entered the URL manually please check your spelling and try again."}), 404
    
@app.errorhandler(403)
def forbidden(error):
    return jsonify({'message':"Sorry you don't have access to that resource. Try logging in."}), 403
    
@app.errorhandler(500)
def server_error(error):
    return jsonify({'message':"Sorry there was an error processing your request. Please review it and try again."}), 500

api.add_resource(Questions, '/api/v1/questions/<string:questionId>')
api.add_resource(QuestionList, '/api/v1/questions')
api.add_resource(AnswerList, '/api/v1/answers')
api.add_resource(Answers, '/api/v1/questions/<string:questionId>/answers')
api.add_resource(CommentList, '/api/v1/comments')
api.add_resource(QuestionComments, '/api/v1/questions/<string:questionId>/comments')
api.add_resource(AnswerComments, '/api/v1/answers/<string:answerId>/comments')

api.add_resource(RegisterUser, '/api/v1/auth/signup')
api.add_resource(Login, '/api/v1/auth/login')
api.add_resource(UpdateAnswer, '/api/v1/questions/<string:questionId>/answers/<string:answerId>')

# if __name__ == "__main__":
#     app.config.from_object(app_config['development'])
#     app.run()
