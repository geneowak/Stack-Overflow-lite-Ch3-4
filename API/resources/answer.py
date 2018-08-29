from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from API.models.answer import Answer
from API.models.question import Question
from .utilities import clean_input


class Answers(Resource):


    @jwt_required
    def post(self, questionId):
        ''' method to add an answer '''
        try:
            # check if the submitted questionId is in the expected format
            questionId = float(questionId)
        except:
            return { "message": "The question id should be a float"}, 400
        
        # check if the question exists
        if not Question.get_question_by_id(questionId):
            return {"message": "Sorry, that question doesn't exist"}, 400

        parser = reqparse.RequestParser()
        parser.add_argument(
            'body',
            type=str,
            required=True,
            help="The body field can't be empty"
        )

        data = parser.parse_args()
        ''' validate data sent '''
        if not clean_input(data['body']):
            return {'message': 'The body should be a string'}, 400
        
        ''' validate that the question hasn't been asked before '''
        if Answer.check_ans_body(data['body'], questionId):
            return {'message': 'Sorry, that answer has already been given'}, 400

        user_id = get_jwt_identity()
        answer = Answer(data['body'], questionId, user_id)
        try:
            if Answer.add_answer(answer) == True:
                return {'message': 'Your answer was successfully added'}, 201
        except:
            return {'message': 'There was a problem adding the answer'}, 500

        return {'message': 'There was a problem adding the answer'}, 500


class AnswerList(Resource):
    
    def get(self):
        ''' method get all the available answers '''
        return {'answers': Answer.get_answers()}
