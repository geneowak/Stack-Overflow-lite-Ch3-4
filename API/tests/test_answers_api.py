import unittest
from API.app import app
from API.config import app_config
from API.resources.question import QuestionList
from API.models.question import Question
from API.models.answer import Answer
import json


class BaseCase(unittest.TestCase):

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

    def test_add_answer(self):
        ''' this method tests that an answer can be added to a question '''
        with self.client as client:
            # add a question
            request = client.post(self.add_question_url, data=self.test_question)
            self.assertEqual(request.status_code, 201)
            response = json.loads(request.data.decode())
            self.assertIn("Question was successfully created",
                          response['message'])
            request = client.post(
                self.add_answer_url, data=self.test_answer
            )
            self.assertEqual(request.status_code, 201)
            response = json.loads(request.data.decode())
            self.assertIn("Your answer was successfully added",
                          response['message'])

    def test_blank_ans(self):
        ''' this method tests that a submitted answer is a string '''
        with self.client as client:
            request = client.post(self.add_question_url, data=self.test_question)
            self.assertEqual(request.status_code, 201)
            response = json.loads(request.data.decode())
            self.assertIn("Question was successfully created",
                          response['message'])
            # check with numerical body
            request = client.post(
                self.add_answer_url, data={"body": "2356"}
            )
            self.assertEqual(request.status_code, 400)
            response = json.loads(request.data.decode())
            self.assertIn("The body should be a string", response['message'])
            # check with blank body
            request = client.post(
                self.add_answer_url, data={"body": " "}
            )
            self.assertEqual(request.status_code, 400)
            response = json.loads(request.data.decode())
            self.assertIn("The body should be a string", response['message'])

    def test_repeated_answer(self):
        ''' this method tests that the same answer isn't given to a question '''
        with self.client as client:
            request = client.post(self.add_question_url, data=self.test_question)
            self.assertEqual(request.status_code, 201)
            response = json.loads(request.data.decode())
            self.assertIn("Question was successfully created",
                          response['message'])
            request = client.post(
                self.add_answer_url, data=self.test_answer
            )
            self.assertEqual(request.status_code, 201)
            request = client.post(
                self.add_answer_url, data=self.test_answer
            )
            self.assertEqual(request.status_code, 400)
            response = json.loads(request.data.decode())
            self.assertIn(
                "Sorry, that answer has already been given", response['message'])

    def test_qn_for_answer_exists(self):
        ''' this method tests that an answer can only be added to a question that exists '''
        with self.client as client:
            # add an answer before adding question
            request = client.post(
                self.add_answer_url, data=self.test_answer
            )
            self.assertEqual(request.status_code, 400)
            response = json.loads(request.data.decode())
            self.assertIn("Sorry, that question doesn't exist",
                          response['message'])

    def tearDown(self):
        ''' this method clears all the data that was used for the test '''
        Question.questions.clear()
        Answer.answers.clear()
