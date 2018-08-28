from .db_handler import DbHandler
from pprint import pprint
import datetime


class AnswerHandler(DbHandler):
    def __init__(self):
        super().__init__()

    def insert_answer(self, user_id, qn_id, body):
        pass

    def update_answer(self, ans_id):
        pass

    def get_answer_by_qn_id(self, qn_id):
        pass
        