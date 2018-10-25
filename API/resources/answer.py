from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from API.models.answer import Answer
from API.models.question import Question
from .utilities import clean_input, check_answer_length


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
        body = data['body'].strip().lower()
        ''' validate data sent '''
        if not clean_input(body):
            return {'message': 'The body should be a string'}, 400

        if not check_answer_length(body):
            return {'message': 'Answer is too short'}, 400
        
        ''' validate that the question hasn't been asked before '''
        if Answer.check_repeated_ans(body, questionId):
            return {'message': 'Sorry, that answer has already been given'}, 400

        user_id = get_jwt_identity()
        answer = Answer(body, questionId, user_id)
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


class UpdateAnswer(Resource):
    
    @jwt_required
    def put(self, questionId, answerId):
        ''' this method deletes a question only if the user is the author '''
        parser = reqparse.RequestParser()
        parser.add_argument(
            'action',
            type=str,
            required=True,
            help="The action field can't be empty"
        )
        parser.add_argument('body', type=str)
        data = parser.parse_args()
        action = data['action'].strip()
        # print(action)

        if action.lower() != 'update' and action.lower() != 'accept':
            return {'message': 'The action value should be update or accept'}, 400

        user_id = get_jwt_identity()
        db_question = Question.get_question_by_id(questionId)
        if not db_question:
            return {'message': 'Question not found'}, 404
        
        answer = Answer.get_answer_by_qn_id(answerId, questionId)
        if answer:
            print(db_question.json())
            print(answer.json())
            if action.lower() == 'update':
                if answer.user_id == user_id:
                    body = data['body'].lower().strip()
                    if not body:
                        return {'message': 'The body should not be empty'}, 400

                    ''' validate data sent '''
                    if not clean_input(body):
                        return {'message': 'The body should be a string'}, 400

                    if not check_answer_length(body):
                        return {'message': 'Answer is too short'}, 400

                    ''' validate that the answer hasn't been given before '''
                    if Answer.check_repeated_ans(body, questionId):
                        return {'message': 'Sorry, that answer with already exits'}, 400
                    try:
                        if Answer.update_answer(answer.ans_id, body):
                            return {"message": "Answer was successfully updated"}, 201

                        return {"message": "There was a problem updating the answer, Please try again later..."}, 500
                    except:
                        return {'message': 'There was a problem adding the answer'}, 500
                return {'message': "Sorry you don't have permission to update this answer"}, 401
            elif action.lower() == 'accept':
                if db_question.user_id == user_id:
                    try:
                        if Answer.accept_answer(answer.ans_id, db_question.qn_id):
                            return {"message": "Answer was successfully accepted"}, 200

                        return {"message": "There was a problem accepting the answer, Please try again later..."}, 500
                    except:
                        return {'message': 'There was a problem accepting the answer, please try again later...'}, 500
                return {'message': "Sorry you don't have permission to accept this answer"}, 401

        return {'message': 'Answer not found'}, 404
