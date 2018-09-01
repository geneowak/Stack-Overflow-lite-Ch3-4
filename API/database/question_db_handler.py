from .db_handler import DbHandler
from pprint import pprint
import datetime


class QuestionHandler(DbHandler):
    ''' qn_id, title, description, user_id, create_date '''
    def __init__(self):
        super().__init__()
    
    def insert_question(self, user_id, title, description):
        try:
            query="INSERT INTO questions (title, description, user_id, create_date) VALUES(%s,%s,%s,%s)"
            self.cursor.execute(query, (title, description, user_id, datetime.datetime.now()))
            # close connection
            super().close_conn()
            return True
        except (Exception) as error:
            pprint(error)
            self.conn.rollback()
            super().close_conn()
            return False

    def get_question_by_id(self, qn_id):
        try:
            query = "SELECT title, description, user_id, qn_id FROM questions WHERE qn_id=%s"
            self.cursor.execute(query, (qn_id,))
            row = self.cursor.fetchone()
            super().close_conn()
            return row
        except (Exception) as error:
            pprint(error)
            super().close_conn()
            return False

    def delete_question(self, qn_id):
        try:
            query = "DELETE FROM questions WHERE qn_id=%s"
            self.cursor.execute(query, (qn_id,))
            super().close_conn()
            return True
        except (Exception) as error:
            pprint(error)
            super().close_conn()
            return False
        
    def get_questions(self):
        try:
            query = "SELECT title, description, user_id, qn_id FROM questions"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            super().close_conn()
            return rows
        except (Exception) as error:
            pprint(error)
            super().close_conn()
            return None
        
    def get_questions_by_user_id(self, user_id):
        try:
            query = "SELECT title, description, user_id, qn_id FROM questions WHERE user_id=%s"
            self.cursor.execute(query, (user_id,))
            rows = self.cursor.fetchall()
            # print(rows)
            super().close_conn()
            return rows
        except (Exception) as error:
            pprint(error)
            super().close_conn()
            return None

    def update_question(self, qn_id, description):
        try:
            query = "UPDATE questions SET description=%s WHERE qn_id=%s"
            self.cursor.execute(query, (description,qn_id))
            super().close_conn()
            return True
        except (Exception) as error:
            pprint(error)
            self.conn.rollback()
            super().close_conn()
            return False

    def check_title(self, title):
        try:
            query = "SELECT title, description, user_id, qn_id FROM questions WHERE title=%s"
            self.cursor.execute(query, (title,))
            row = self.cursor.fetchone()
            super().close_conn()
            return row
        except (Exception) as error:
            pprint(error)
            super().close_conn()
            return False

    def check_description(self, description):
        try:
            query = "SELECT title, description, user_id, qn_id FROM questions WHERE description=%s"
            self.cursor.execute(query, (description,))
            row = self.cursor.fetchone()
            super().close_conn()
            return row
        except (Exception) as error:
            pprint(error)
            super().close_conn()
            return False
