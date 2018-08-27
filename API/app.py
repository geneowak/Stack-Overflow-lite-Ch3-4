from flask import Flask, request, render_template
from flask_restful import Api

from API.resources.question import Questions, QuestionList
from API.resources.answer import Answers, AnswerList
from API.resources.comment import CommentList, QuestionComments, AnswerComments
from API.models.question import Question

app = Flask(__name__)

api = Api(app)

''' 
# end points to develop

GET /questions Fetch all questions
GET /questions/<questionId> Fetch a specific question
POST /questions Add a question
POST /questions/<questionId>/answers Add an answer

POST /questions/<questionId>/comments Add an add a comment to a question
POST /answers/<answerId>/comments Add an add a comment to an answer

 '''
@app.before_first_request
def load_data():
    #  first load all the questions with their repective answers
    Question.load_all_qns()


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

