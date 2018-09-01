from .db_handler import DbHandler
from pprint import pprint
import datetime


class AnswerHandler(DbHandler):
    ''' ans_id, body, qn_id, user_id, preferred, create_date '''
    
    def __init__(self):
        super().__init__()

    def insert_answer(self, user_id, qn_id, body):
        try:
            query = "INSERT INTO answers (body, qn_id, user_id, create_date) VALUES(%s,%s,%s,%s)"
            self.cursor.execute(
                query, (body, qn_id, user_id, datetime.datetime.now()))
            # close connection
            super().close_conn()
            return True
        except (Exception) as error:
            pprint(error)
            self.conn.rollback()
            super().close_conn()
            return False

    def update_answer(self, ans_id, body):
        try:
            print("ans_id:", ans_id, " body:", body)
            query = "UPDATE answers SET body=%s WHERE ans_id=%s"
            self.cursor.execute(query, (body, ans_id))
            super().close_conn()
            print('answer updated....',ans_id)
            return True
        except (Exception) as error:
            pprint(error)
            self.conn.rollback()
            super().close_conn()
            return False

    def accept_answer(self, ans_id, qn_id):
        try:
            print("ans_id:",ans_id," qn_id:",qn_id)
            # first unselect what was accepted before
            query = "SELECT ans_id FROM answers WHERE qn_id=%s AND preferred=%s"
            self.cursor.execute(query, (qn_id,'true'))
            row = self.cursor.fetchone()
            if row:
                query = "UPDATE answers SET preferred=%s WHERE ans_id=%s"
                self.cursor.execute(query, ('false', row[0]))

            query = "UPDATE answers SET preferred=%s WHERE ans_id=%s"
            self.cursor.execute(query, ('true', ans_id))
            super().close_conn()
            return True
        except (Exception) as error:
            pprint(error)
            self.conn.rollback()
            super().close_conn()
            return False

    def get_answers_by_qn_id(self, qn_id):
        try:
            query = "SELECT body, qn_id, user_id, ans_id FROM answers WHERE qn_id=%s"
            self.cursor.execute(query, (qn_id,))
            rows = self.cursor.fetchall()
            super().close_conn()
            return rows
        except (Exception) as error:
            pprint(error)
            super().close_conn()
            return False

    def get_answer_by_qn_id(self, ans_id, qn_id):
        try:
            query = "SELECT body, qn_id, user_id, ans_id FROM answers WHERE qn_id=%s and ans_id=%s"
            self.cursor.execute(query, (qn_id, ans_id))
            rows = self.cursor.fetchone()
            super().close_conn()
            return rows
        except (Exception) as error:
            pprint(error)
            super().close_conn()
            return False
            
    def get_answers_by_ans_id(self, ans_id):
        try:
            query = "SELECT body, qn_id, user_id, ans_id FROM answers WHERE ans_id=%s"
            self.cursor.execute(query, (ans_id,))
            row = self.cursor.fetchone()
            super().close_conn()
            return row
        except (Exception) as error:
            pprint(error)
            super().close_conn()
            return False
            
    def get_answers_by_ans_user_id(self, user_id):
        try:
            query = "SELECT body, qn_id, user_id, ans_id FROM answers WHERE user_id=%s"
            self.cursor.execute(query, (user_id,))
            rows = self.cursor.fetchall()
            super().close_conn()
            return rows
        except (Exception) as error:
            pprint(error)
            super().close_conn()
            return False

    def get_answers(self):
        try:
            query = "SELECT body, qn_id, user_id, ans_id FROM answers"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            super().close_conn()
            return rows
        except (Exception) as error:
            pprint(error)
            super().close_conn()
            return None
        
    def check_body(self, body, qn_id):
        try:
            query = "SELECT body, qn_id, user_id, ans_id FROM answers WHERE body=%s AND qn_id=%s"
            self.cursor.execute(query, (body, qn_id))
            row = self.cursor.fetchone()
            super().close_conn()
            return row
        except (Exception) as error:
            pprint(error)
            super().close_conn()
            return False
