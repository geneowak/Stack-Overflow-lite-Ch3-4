import os
import unittest
from API.app import app
from API.config import app_config
from API.resources.question import QuestionList
from API.models.question import Question
from API.models.answer import Answer

from API.database.db_handler import DbHandler

from .helpers import *

import json

class TestQuestionApi(unittest.TestCase):
    # setup method
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
            self.token = get_auth_token(client)

    def test_get_questions(self):
        """ this method can test that the api can get all the questions that have been added to the platform """
        with self.client as client:
            # add a questions
            request = add_question(client, self.token, test_question)
            self.assertEqual(request.status_code, 201)
            request = add_question(client, self.token, {"title": "some title", "body": "Lorem ipsum dolor sit amet"})
            self.assertEqual(request.status_code, 201)
            # try getting the data submitted
            request = get_questions(client)
            self.assertEqual(request.status_code, 200)
            response = json.loads(request.data.decode())
            self.assertEqual(2, len(response['questions']))

    def test_add_question(self):
        """ this method tests that a question can be added to the platform """
        with self.client as client:
            # add a questions
            request = add_question(client, self.token, test_question)
            response = json.loads(request.data.decode())
            self.assertIn("Question was successfully created", response['message'])
            self.assertEqual(request.status_code, 201)

    def test_delete_question(self):
        """ this method tests that a question can be added to the platform """
        with self.client as client:
            # add a questions
            request = add_question(client, self.token, test_question)
            self.assertEqual(request.status_code, 201)
            request = delete_question(client, self.token)
            self.assertEqual(request.status_code, 200)
            response = json.loads(request.data.decode())
            self.assertIn("Question was successfully deleted", response['message'])

    def test_get_question(self):
        """ this method tests that the api can get a question that have been submitted """
        with self.client as client:
            # add a questions
            request = add_question(client, self.token, test_question)
            self.assertEqual(request.status_code, 201)
            # try getting the data submitted
            request = get_question(client)
            self.assertEqual(request.status_code, 200)
            self.assertIn("stop over bleeding artery", str(request.data))

    def test_for_correct_qn_title(self):
        ''' this method tests to ensure that the title of the question is a string '''
        with self.client as client:
            # check with empty title
            request = add_question(client, self.token, { "title": " ", "body": "Lorem ipsum dolor sit amet"})
            self.assertEqual(request.status_code, 400)
            response = json.loads(request.data.decode())
            self.assertIn("The title should be a string", response['message'])
            # check with numerical title
            request = add_question(client, self.token, {"title": "21948", "body": "Lorem ipsum dolor sit amet"})
            self.assertEqual(request.status_code, 400)
            response = json.loads(request.data.decode())
            self.assertIn("The title should be a string", response['message'])

    def test_for_repeated_qn(self):
        ''' this method tests to ensure that a question isn't asked more than once '''
        with self.client as client:
            # post a question
            request = add_question(client, self.token, {'title':'title1 of question1', 'body':'body1 with of question1 of test'})
            self.assertEqual(request.status_code, 201)
            # check with repeated question title
            request = add_question(client, self.token, {'title':'title1 of question1', 'body':'body1 with of question1 of test'})
            self.assertEqual(request.status_code, 400)
            response = json.loads(request.data.decode())
            self.assertIn("Sorry, a question with that title has already been asked", response['message'])
            # check with repeated question body
            request = add_question(client, self.token, {'title':'title2 of question1333', 'body':'body1 with of question1 of test'})
            self.assertEqual(request.status_code, 400)
            response = json.loads(request.data.decode())
            self.assertIn("Sorry, a question with that body has already been asked", response['message'])

    def test_for_correct_qn_body(self):
        ''' this method tests if for if app rejects non string bodies for the question '''
        with self.client as client:
            # check with empty body
            request = add_question(client, self.token, { "title": "tiltle of a question", "body": " "})
            self.assertEqual(request.status_code, 400)
            response = json.loads(request.data.decode())
            self.assertIn("The body should be a string", response['message'])
            # check with numbers only
            request = add_question(client, self.token, { "title": "tiltle of a questions", "body": "2374 47456 28837473282827"})
            self.assertEqual(request.status_code, 400)
            response = json.loads(request.data.decode())
            self.assertIn("The body should be a string", response['message'])

    def test_title_length(self):
        ''' this method checks if the title length is as expected '''
        with self.client as client:
            # add a questions
            request = add_question(client, self.token, { "title": "title", "body": "some super long body some question"})
            response = json.loads(request.data.decode())
            self.assertIn("The title should be at least 8 characters", response['message'])
            self.assertEqual(request.status_code, 400)

    def test_body_length(self):
        ''' this method checks if the body length is as expected '''
        with self.client as client:
            # add a questions
            request = add_question(client, self.token, { "title": "some good title", "body": "short body "})
            response = json.loads(request.data.decode())
            self.assertIn("The question description is too short.", response['message'])
            self.assertEqual(request.status_code, 400)

    def tearDown(self):
        ''' this method clears all the data that was used for the test '''
        with self.client:
            ''' create all tables before first request '''
            dbHandle = DbHandler()
            dbHandle.drop_all_tables()
            dbHandle.close_conn()

