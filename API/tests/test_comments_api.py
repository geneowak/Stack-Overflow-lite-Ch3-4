import unittest
from API.app import app
from API.config import app_config
from API.resources.question import QuestionList
from API.models.question import Question
from API.models.answer import Answer
from API.models.comment import Comment

from API.database.db_handler import DbHandler

from .helpers import *

import json

class TestCommentApi(unittest.TestCase):
    
    def setUp(self):
        ''' this method sets up the client and the test data we'll be using in the tests '''
        app.config.from_object(app_config['testing'])
        self.client = app.test_client()
        with self.client as client:
            ''' create all tables before first request '''
            dbHandle = DbHandler()
            dbHandle.drop_all_tables()
            dbHandle.create_tables()
            dbHandle.close_conn()
            add_test_user(client)

    # def test_add_question_comment(self):
    #     ''' method to test adding of a comment to a question '''
    #     with self.client as client:
    #         # add a question
    #         request = client.post(add_question_url, data=test_question)
    #         self.assertEqual(request.status_code, 201)
    #         # add comment
    #         request = client.post(
    #             add_question_comment_url, data=test_question_comment
    #         )
    #         self.assertEqual(request.status_code, 201)
    #         response = json.loads(request.data.decode())
    #         self.assertIn("Your comment was successfully added", response['message'])

    # def test_add_answer_comment(self):
    #     ''' method to test adding of a comment to an answer '''
    #     with self.client as client:
    #         # add a question
    #         request = client.post(add_question_url, data=test_question)
    #         self.assertEqual(request.status_code, 201)
    #         # add an answer
    #         request = client.post(add_answer_url, data=test_answer)
    #         self.assertEqual(request.status_code, 201)
    #         # add comment
    #         request = client.post(
    #             add_answer_comment_url, data=test_answer_comment
    #         )
    #         self.assertEqual(request.status_code, 201)
    #         response = json.loads(request.data.decode())
    #         self.assertIn("Your comment was successfully added", response['message'])

    # def test_repeated_question_comment(self):
    #     ''' method to test if a comment has already been added '''
    #     with self.client as client:
    #         # add a question
    #         request = client.post(add_question_url, data=test_question)
    #         self.assertEqual(request.status_code, 201)
    #         # add comment
    #         request = client.post(
    #             add_question_comment_url, data=test_question_comment
    #         )
    #         self.assertEqual(request.status_code, 201)
    #         # add the same comment
    #         request = client.post(
    #             add_question_comment_url, data=test_question_comment
    #         )
    #         self.assertEqual(request.status_code, 400)
    #         response = json.loads(request.data.decode())
    #         self.assertIn(
    #             "Sorry, that comment has already been given", response['message']
    #         )

    # def test_repeated_answer_comment(self):
    #     ''' method to test if a comment can be added to an answer '''
    #     with self.client as client:
    #         # add a question
    #         request = client.post(add_question_url, data=test_question)
    #         self.assertEqual(request.status_code, 201)
    #         # add an answer
    #         request = client.post(add_answer_url, data=test_answer)
    #         self.assertEqual(request.status_code, 201)
    #         # add comment
    #         request = client.post(
    #             add_answer_comment_url, data=test_answer_comment
    #         )
    #         self.assertEqual(request.status_code, 201)
    #         # add the same comment
    #         request = client.post(
    #             add_answer_comment_url, data=test_answer_comment
    #         )
    #         self.assertEqual(request.status_code, 400)
    #         response = json.loads(request.data.decode())
    #         self.assertIn(
    #             "Sorry, that comment has already been given", response['message']
    #         )

    # def test_blank_question_comment(self):
    #     ''' method to test if the comment being added to a question is a string '''
    #     with self.client as client:
    #         # add a question
    #         request = client.post(add_question_url, data=test_question)
    #         self.assertEqual(request.status_code, 201)
    #         # add blank comment
    #         request = client.post(
    #             add_question_comment_url, data={'body': "   "}
    #         )
    #         self.assertEqual(request.status_code, 400)
    #         response = json.loads(request.data.decode())
    #         self.assertIn("The body should be a string", response['message'])
    #         # add comment with only numbers
    #         request = client.post(
    #             add_question_comment_url, data={'body': "73736482"}
    #         )
    #         self.assertEqual(request.status_code, 400)
    #         response = json.loads(request.data.decode())
    #         self.assertIn("The body should be a string", response['message'])

    # def test_blank_answer_comment(self):
    #     ''' method to test if the comment being added to a comment is a string '''
    #     with self.client as client:
    #         # add a question
    #         request = client.post(add_question_url, data=test_question)
    #         self.assertEqual(request.status_code, 201)
    #         # add an answer
    #         request = client.post(add_answer_url, data=test_answer)
    #         self.assertEqual(request.status_code, 201)
    #         # add blank comment
    #         request = client.post(
    #             add_answer_comment_url, data={'body': "   "}
    #         )
    #         self.assertEqual(request.status_code, 400)
    #         response = json.loads(request.data.decode())
    #         self.assertIn("The body should be a string", response['message'])
    #         # add comment with only numbers
    #         request = client.post(
    #             add_answer_comment_url, data={'body': "73736482"}
    #         )
    #         self.assertEqual(request.status_code, 400)
    #         response = json.loads(request.data.decode())
    #         self.assertIn("The body should be a string", response['message'])

    # def test_get_comments(self):
    #     with self.client as client:
    #         # add a question
    #         request = client.post(add_question_url, data=test_question)
    #         self.assertEqual(request.status_code, 201)
    #         # add comment
    #         request = client.post(
    #             add_question_comment_url, data=test_question_comment
    #         )
    #         self.assertEqual(request.status_code, 201)
    #         # add an answer
    #         request = client.post(add_answer_url, data=test_answer)
    #         self.assertEqual(request.status_code, 201)
    #         # add comment
    #         request = client.post(
    #             add_answer_comment_url, data=test_answer_comment
    #         )
    #         self.assertEqual(request.status_code, 201)
    #         # get questions
    #         request = client.get(get_comments_url)
    #         response = json.loads(request.data.decode())
    #         self.assertEqual(2, len(response['comments']))

    def tearDown(self):
        ''' this method clears all the data that was used for the test '''
        with self.client:
            ''' create all tables before first request '''
            # dbHandle = DbHandler()
            # dbHandle.drop_all_tables()
            # dbHandle.close_conn()
