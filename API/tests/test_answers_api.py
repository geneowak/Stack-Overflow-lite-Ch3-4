import unittest
from API.app import app
from API.config import app_config
from API.resources.question import QuestionList
from API.models.question import Question
from API.models.answer import Answer
from API.database.db_handler import DbHandler

from .helpers import *

import json


class TestAnswerApi(unittest.TestCase):

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
        

    def test_add_answer(self):
        ''' this method tests that an answer can be added to a question '''
        with self.client as client:
            request = add_question(client, self.token, test_question)
            self.assertEqual(request.status_code, 201)
            response = json.loads(request.data.decode())

            request = add_answer(client, self.token, test_answer)
            self.assertEqual(request.status_code, 201)
            response = json.loads(request.data.decode())
            self.assertIn("Your answer was successfully added", response['message'])
        
    def test_update_answer(self):
        ''' this method tests that an answer can be added to a question '''
        with self.client as client:
            request = add_question(client, self.token, test_question)
            self.assertEqual(request.status_code, 201)
            response = json.loads(request.data.decode())

            request = add_answer(client, self.token, test_answer)
            self.assertEqual(request.status_code, 201)

            request = update_answer(client, self.token, update_answer_data)
            self.assertEqual(request.status_code, 201)
            response = json.loads(request.data.decode())
            self.assertIn("Answer was successfully updated", response['message'])

    def test_accept_answer(self):
        ''' this method tests that an answer can be added to a question '''
        with self.client as client:
            request = add_question(client, self.token, test_question)
            self.assertEqual(request.status_code, 201)
            response = json.loads(request.data.decode())

            request = add_answer(client, self.token, test_answer)
            self.assertEqual(request.status_code, 201)

            request = accept_answer(client, self.token, accept_answer_data)
            self.assertEqual(request.status_code, 200)
            response = json.loads(request.data.decode())
            self.assertIn("Answer was successfully accepted", response['message'])

    def test_blank_ans(self):
        ''' this method tests that a submitted answer is a string '''
        with self.client as client:
            request = add_question(client, self.token, test_question)
            self.assertEqual(request.status_code, 201)
            
            request = add_answer(client, self.token, {"body": "2356"})
            self.assertEqual(request.status_code, 400)
            response = json.loads(request.data.decode())
            self.assertIn("The body should be a string", response['message'])
            
            request = add_answer(client, self.token, {"body": " "})
            self.assertEqual(request.status_code, 400)
            response = json.loads(request.data.decode())
            self.assertIn("The body should be a string", response['message'])

    def test_repeated_answer(self):
        ''' this method tests that the same answer isn't given to a question '''
        with self.client as client:
            request = add_question(client, self.token, test_question)
            self.assertEqual(request.status_code, 201)

            request = add_answer(client, self.token, test_answer)
            self.assertEqual(request.status_code, 201)

            request = add_answer(client, self.token, test_answer)
            self.assertEqual(request.status_code, 400)
            response = json.loads(request.data.decode())
            self.assertIn("Sorry, that answer has already been given", response['message'])

    def test_qn_for_answer_exists(self):
        ''' this method tests that an answer can only be added to a question that exists '''
        with self.client as client:
            # add an answer before adding question
            request = add_answer(client, self.token, test_answer)
            self.assertEqual(request.status_code, 400)
            response = json.loads(request.data.decode())
            self.assertIn("Sorry, that question doesn't exist", response['message'])

    def tearDown(self):
        ''' this method clears all the data that was used for the test '''
        with self.client:
            ''' create all tables before first request '''
            dbHandle = DbHandler()
            dbHandle.drop_all_tables()
            dbHandle.close_conn()


