from .db_handler import DbHandler
from pprint import pprint
import datetime


class QuestionHandler(DbHandler):
    def __init__(self):
        super().__init__()
    
    def insert_question(self, user_id, title, body):
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
            query = "SELECT FROM questions WHERE qn_id={}"
            self.cursor.execute(query.format(qn_id))
            row = self.cursor.fetchone()
            self.conn.close()
            return row
        except (Exception) as error:
            pprint(error)
            self.conn.close()
            return False
        
    def get_questions(self):
        try:
            query = "SELECT * FROM questions"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            self.conn.close()
            return rows
        except (Exception) as error:
            pprint(error)
            self.conn.rollback()
            self.conn.close()
            return None

    def update_question(self, qn_id):
        try:
            pass
        except (Exception) as error:
            pprint(error)
            self.conn.close()
            return False

    def check_title(self, qn_id):
        try:
            pass
        except (Exception) as error:
            pprint(error)
            self.conn.close()
            return False

    def check_body(self, qn_id):
        try:
            pass
        except (Exception) as error:
            pprint(error)
            self.conn.close()
            return False
