from flask import Flask, request, render_template
from flask_restful import Api

from API.resources.question import Questions, QuestionList
from API.resources.answer import Answers, AnswerList
from API.resources.comment import CommentList, QuestionComments, AnswerComments
from API.resources.user import RegisterUser

app = Flask(__name__)

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
 
@app.route('/')
def get_def_page():
   return render_template('index.html')

api.add_resource(Questions, '/api/v1/questions/<string:questionId>')
api.add_resource(QuestionList, '/api/v1/questions')
api.add_resource(AnswerList, '/api/v1/answers')
api.add_resource(Answers, '/api/v1/questions/<string:questionId>/answers')
api.add_resource(CommentList, '/api/v1/comments')
api.add_resource(QuestionComments, '/api/v1/questions/<string:questionId>/comments')
api.add_resource(AnswerComments, '/api/v1/answers/<string:answerId>/comments')

api.add_resource(RegisterUser, '/api/v1/auth/signup')

