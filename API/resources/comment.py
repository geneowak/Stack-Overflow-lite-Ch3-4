from flask import jsonify
from flask_restful import Resource, reqparse
from API.models.answer import Answer
from API.models.question import Question
from API.models.comment import Comment
from .utilities import clean_input, check_comment_length
from flask_jwt_extended import jwt_required, get_jwt_identity
from pprint import pprint

''' 
End point to develop

POST /questions/<questionId>/comments Add a comment to a question
POST /answers/<answerId>/comments Add a comment to an answer
 '''


# load the answers from Model....
comments = Comment.get_comments()


class QuestionComments(Resource):
    
    @jwt_required
    def post(self, questionId):
        ''' method to add a comment to a question '''

        try:
            # check if the submitted questionId is in the expected format
            questionId = float(questionId)
        except:
            return {"message": "The question id should be a float"}, 400

        # check if the question exists
        if not Question.get_question_by_id(questionId):
            return {"message": "Sorry, that question doesn't exist"}, 400

        parser = reqparse.RequestParser()
        parser.add_argument(
            'comment',
            type=str,
            required=True,
            help="The comment field can't be empty"
        )

        data = parser.parse_args()
        ''' validate data sent '''
        if not clean_input(data['comment']):
            return {'message': 'The comment should be a string'}, 400

        ''' validate that the comment has been given before '''
        # if Comment.check_for_repeated_comment(data['comment'], 'question', questionId):
        #     return {'message': 'Sorry, that comment has already been given'}, 400
        # # setting ids
        # comm_id = Comment.get_no_of_comments() + 1

        user_id = get_jwt_identity()
        # user_id, comment, parent, parent_id
        comment = Comment(user_id,  data['comment'], 'question', questionId)
        try:
            pprint("adding question comment...")
            pprint(comment.json())
            if comment.add_comment():
                return {'message': 'Your comment was successfully added'}, 201
        except:
            return {'message': 'There was a problem adding the comment'}, 500

        return {'message': "There was a problem adding the comment to the question..."}, 500

class AnswerComments(Resource):

    @jwt_required
    def post(self, answerId):
        ''' method to add a comment to a question '''
        try:
            # check if the submitted questionId is in the expected format
            answerId = float(answerId)
        except:
            return {"message": "The answer id should be a float"}, 400

        # check if the answer exists
        if not Answer.get_answer_by_ans_id(answerId):
            return {"message": "Sorry, that answer doesn't exist"}, 400

        parser = reqparse.RequestParser()
        parser.add_argument(
            'comment',
            type=str,
            required=True,
            help="The comment field can't be empty"
        )

        data = parser.parse_args()
        ''' validate data sent '''
        if not clean_input(data['comment']):
            return {'message': 'The comment should be a string'}, 400

        # ''' validate that the comment has been given before'''
        # if Comment.check_for_repeated_comment(data['comment'], 'answer', answerId):
        #     return {'message': 'Sorry, that comment has already been given'}, 400
        # # setting ids
        # comm_id = Comment.get_no_of_comments() + 1

        user_id = get_jwt_identity()

        comment = Comment(user_id,  data['comment'], 'answer', answerId)
        try:
            pprint("adding answer comment...")
            pprint(comment.json())
            if comment.add_comment():
                return {'message': 'Your comment was successfully added'}, 201
        except:
            return {'message': 'There was a problem adding the comment'}, 500

        return {'message': 'There was a problem adding the comment to the answer'}, 500


class CommentList(Resource):

    def get(self):
        ''' method get all the available answers '''
        return {'comments': Comment.get_comments()}
