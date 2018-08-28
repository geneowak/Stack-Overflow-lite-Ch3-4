from .db_handler import DbHandler
from pprint import pprint
import datetime


class QuestionHandler(DbHandler):
    def __init__(self, mode=None):
        super().__init__(mode)
    
    def insert_question(self, title, body, user_id):
        try:
            query="INSERT INTO questions VALUES({},{},{},{},{})".format(
                'NULL', title, body, user_id, datetime.datetime.now())
            self.cursor.execute(query)
            # close connection
            self.conn.close()
            return True
        except (Exception) as error:
            pprint(error)
            self.conn.close()
            return False

    def get_question_by_id(self, qn_id):
        try:
            query = "SELECT FROM questions WHERE qn_id={}".format(qn_id)
            self.cursor.execute(query)
            self.conn.close()
        except (Exception) as error:
            pprint(error)
            self.conn.close()
            return False
        
