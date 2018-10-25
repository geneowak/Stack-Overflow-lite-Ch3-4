import os
import unittest
from API.app import app
from API.config import app_config
from API.resources.question import QuestionList
from API.models.question import Question
from API.models.answer import Answer
import json

class BaseCase(unittest.TestCase):
    # setup method
    def setUp(self):
        ''' this method sets up the client and the test data we'll be using in the tests '''
        app.config.from_object(app_config['testing'])
        self.client = app.test_client()
        self.add_question_url = '/api/v1/questions'
        self.get_questions_url = '/api/v1/questions'
        self.get_question_url = '/api/v1/questions/1'
        self.add_answer_url = '/api/v1/questions/1/answers'
        self.get_answers_url = '/api/v1/answers'
        self.test_question = {
            "title": "How do I become the best programmer in the universe?",
            "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        }
        self.test_answer = {
            "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        }

    def test_get_questions(self):
        """ this method can test that the api can get all the questions that have been added to the platform """
        with self.client as client:
            # add a questions
            request = client.post(self.add_question_url, data=self.test_question)
            self.assertEqual(request.status_code, 201)
            request = client.post(self.add_question_url, data={ "title": "some title", "body": "Lorem ipsum dolor sit amet"})
            self.assertEqual(request.status_code, 201)
            # try getting the data submitted
            request = client.get(self.get_questions_url)
            self.assertEqual(request.status_code, 200)
            response = json.loads(request.data.decode())
            self.assertEqual(2, len(response['questions']))

    def test_add_question(self):
        """ this method tests that a question can be added to the platform """
        with self.client as client:
            # add a questions
            request = client.post(self.add_question_url, data=self.test_question)
            response = json.loads(request.data.decode())
            self.assertIn("Question was successfully created", response['message'])
            self.assertEqual(request.status_code, 201)

    def test_get_question(self):
        """ this method tests that the api can get a question that have been submitted """
        with self.client as client:
            # add a questions
            request = client.post(self.add_question_url, data=self.test_question)
            self.assertEqual(request.status_code, 201)
            # try getting the data submitted
            request = client.get(self.get_question_url)
            self.assertEqual(request.status_code, 200)
            self.assertIn("How do I become the best programmer in the universe?", str(request.data))

    def test_for_correct_qn_title(self):
        ''' this method tests to ensure that the title of the question is a string '''
        with self.client as client:
            # check with empty title
            request = client.post(self.add_question_url, data={ "title": " ", "body": "Lorem ipsum dolor sit amet"})
            self.assertEqual(request.status_code, 400)
            response = json.loads(request.data.decode())
            self.assertIn("The title should be a string", response['message'])
            # check with numerical title
            request = client.post(self.add_question_url, data={ "title": "21948", "body": "Lorem ipsum dolor sit amet"})
            self.assertEqual(request.status_code, 400)
            response = json.loads(request.data.decode())
            self.assertIn("The title should be a string", response['message'])

    def test_for_repeated_qn(self):
        ''' this method tests to ensure that a question isn't asked more than once '''
        with self.client as client:
            # post a question
            request = client.post(self.add_question_url, data={'title':'title1 of question1', 'body':'body1 with of question1 of test'})
            self.assertEqual(request.status_code, 201)
            # check with repeated question title
            request = client.post(self.add_question_url, data={'title':'title1 of question1', 'body':'body1 with of question1 of test'})
            self.assertEqual(request.status_code, 400)
            response = json.loads(request.data.decode())
            self.assertIn("Sorry, a question with that title has already been asked", response['message'])
            # check with repeated question body
            request = client.post(self.add_question_url, data={'title':'title2 of question1', 'body':'body1 with of question1 of test'})
            self.assertEqual(request.status_code, 400)
            response = json.loads(request.data.decode())
            self.assertIn("Sorry, a question with that body has already been asked", response['message'])

    def test_for_correct_qn_body(self):
        ''' this method tests if for if app rejects non string bodies for the question '''
        with self.client as client:
            # check with empty body
            request = client.post(self.add_question_url, data={ "title": "tiltle of a question", "body": " "})
            self.assertEqual(request.status_code, 400)
            response = json.loads(request.data.decode())
            self.assertIn("The body should be a string", response['message'])
            # check with numbers only
            request = client.post(self.add_question_url, data={ "title": "tiltle of a questions", "body": "2374 47456 28837473282827"})
            self.assertEqual(request.status_code, 400)
            response = json.loads(request.data.decode())
            self.assertIn("The body should be a string", response['message'])

    def test_title_length(self):
        ''' this method checks if the title length is as expected '''
        with self.client as client:
            # add a questions
            request = client.post(self.add_question_url, data={ "title": "title", "body": "some super long body some question"})
            response = json.loads(request.data.decode())
            self.assertIn("The title should be at least 8 characters", response['message'])
            self.assertEqual(request.status_code, 400)

    def test_body_length(self):
        ''' this method checks if the body length is as expected '''
        with self.client as client:
            # add a questions
            request = client.post(self.add_question_url, data={ "title": "some good title", "body": "short body "})
            response = json.loads(request.data.decode())
            self.assertIn("The body should be atleast 15 characters", response['message'])
            self.assertEqual(request.status_code, 400)

    def tearDown(self):
        ''' this method clears all the data that was used for the test '''
        Question.questions.clear()
        Answer.answers.clear()

