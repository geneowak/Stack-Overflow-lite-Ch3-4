from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from API.models.question import Question
from .utilities import clean_input, check_description_length, check_title_length

class Questions(Resource):
    
    def get(self, questionId):
        qn = Question.get_question_by_id(questionId)
        if qn:
            return { 'question': qn.json() }, 200
        return { 'message': 'Question not found' }, 404
        
    @jwt_required
    def delete(self, questionId):
        ''' this method deletes a question only if the user is the author '''
        user_id = get_jwt_identity()

        question = Question.get_question_by_id(questionId)
        if question:
            if user_id == question.user_id:
                try:
                    if Question.delete_question(question.qn_id):
                        return {"message":"Question was successfully deleted"}, 200
                    return {"message": "Question was not deleted, Please try again later..."}, 500
                except:
                    return {'message': 'There was a problem adding the question'}, 500
            return {'message': "Sorry you don't have permission to delete this question"}, 401

        return {'message': 'Question not found'}, 404

    @jwt_required
    def put(self, questionId):
        ''' this method deletes a question only if the user is the author '''
        parser = reqparse.RequestParser()
        parser.add_argument(
            'body',
            type=str,
            required=True,
            help="The body field can't be empty"
        )
        data = parser.parse_args()
        
        user_id = get_jwt_identity()

        db_question = Question.get_question_by_id(questionId)
        if db_question:
            if db_question.user_id == user_id:
                ''' validate data sent '''
                if not clean_input(data['body']):
                    return {'message': 'The body should be a string'}, 400

                if not check_description_length(data['body']):
                    return {'message': 'The question description is too short'}, 400

                ''' validate that the question hasn't been asked before '''

                if Question.check_qn_body(data['body']):
                    return {'message': 'Sorry, that question with already exits'}, 400

                try:
                    if Question.update_question(db_question.qn_id, data['body']):
                        return {"message": "Question was successfully updated"}, 200
                        
                    return {"message": "Question was not updated, Please try again later..."}, 500
                except:
                    return {'message': 'There was a problem adding the question'}, 500
            return {'message': "Sorry you don't have permission to update this question"}, 401

        return {'message': 'Question not found'}, 404


class QuestionList(Resource):
    
    def get(self):
        ''' this method gets all the questions on the platform '''
        return {'questions': Question.get_questions()}, 200
        
    @jwt_required
    def post(self):
        ''' this method add a question '''
        parser = reqparse.RequestParser()
        parser.add_argument(
            'title', 
            type=str, 
            required=True,
            help="The title field can't be empty"
        )
        parser.add_argument(
            'body',
            type=str, 
            required=True,
            help="The body field can't be empty"
        )
        data = parser.parse_args()
        ''' validate data sent '''
        if not clean_input(data['title']):
            return {'message': 'The title should be a string'}, 400
        
        if not check_title_length(data['title']):
            return {'message': 'The title should be at least 8 characters'}, 400

        if not clean_input(data['body']):
            return {'message': 'The body should be a string'}, 400
            
        if not check_description_length(data['body']):
            return {'message': 'The question description is too short.'}, 400
            
        ''' validate that the question hasn't been asked before '''
        if Question.check_qn_title(data['title']):
            return {'message': 'Sorry, a question with that title has already been asked'}, 400

        if Question.check_qn_body(data['body']):
            return {'message': 'Sorry, a question with that body has already been asked'}, 400
        
        user_id = get_jwt_identity()
        # print(user_id, "userid")
        question = Question(data['title'], data['body'], user_id)

        try:
            question.add_question(question)
        except:
            return {'message': 'There was a problem adding the question'}, 500

        return {'message': 'Question was successfully created'}, 201
