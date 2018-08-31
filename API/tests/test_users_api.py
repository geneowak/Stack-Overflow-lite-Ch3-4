import unittest
from API.app import app
from API.config import app_config

from API.database.db_handler import DbHandler

from .helpers import *

import json


class TestUserApi(unittest.TestCase):
    
    def setUp(self):
        ''' this method sets up the client and the test data we'll be using in the tests '''
        app.config.from_object(app_config['testing'])
        self.client = app.test_client()
        with self.client as client:
            ''' create all tables before first request '''
            dbHandle = DbHandler()
            dbHandle.create_tables()
            dbHandle.close_conn()
            add_test_user(client)
            self.token = get_auth_token(client) 

    def test_signup(self):
        """ this method tests that a question can be added to the platform """
        with self.client as client:
            # add a questions
            request = sign_up(client, **correct_user2)
            response = json.loads(request.data.decode())
            self.assertIn("User created successfully", response['message'])
            self.assertEqual(request.status_code, 201)

    def test_signup_existing_user(self):
        """ this method tests that a question can be added to the platform """
        with self.client as client:
            # add a questions
            request = sign_up(client, **correct_user)
            response = json.loads(request.data.decode())
            self.assertIn("User geneowak already exists", response['message'])
            self.assertEqual(request.status_code, 400)

    def test_login(self):
        """ this method tests that a question can be added to the platform """
        with self.client as client:
            # add a questions
            request = login(client, **correct_user)
            response = json.loads(request.data.decode())
            self.assertIn("Login successful", response['message'])
            self.assertEqual(request.status_code, 200)

    def tearDown(self):
        ''' this method clears all the data that was used for the test '''
        with self.client:
            ''' create all tables before first request '''
            # dbHandle = DbHandler()
            # dbHandle.drop_all_tables()
            # dbHandle.close_conn()
