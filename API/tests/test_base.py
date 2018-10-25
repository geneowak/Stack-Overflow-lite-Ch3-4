import unittest
from API.app import app
from API.config import app_config
from API.resources.question import QuestionList
from API.models.question import Question
from API.models.answer import Answer
from API.database.db_handler import DbHandler

from .helpers import *


class BaseCase(unittest.TestCase):
    
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

    def tearDown(self):
        ''' this method clears all the data that was used for the test '''
        with self.client:
            ''' create all tables before first request '''
            dbHandle = DbHandler()
            dbHandle.drop_all_tables()
            dbHandle.close_conn()
