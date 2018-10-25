from .db_handler import DbHandler
from pprint import pprint
import datetime
from .database_ini import table_names


class QuestionHandler(DbHandler):
    ''' 
    This method handles all the database functions of the question model
    '''
    # table_names: qn_id, title, description, user_id, create_date

    def __init__(self):
        super().__init__()
        self.qn_tb_name = table_names["questions"]
    
    def insert_question(self, user_id, title, description):
        ''' adds a question to the database '''
        try:
            query="INSERT INTO "+self.qn_tb_name+" (title, description, user_id, create_date) VALUES(%s,%s,%s,%s)"
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
        ''' gets the specified question form the database '''
        try:
            query = "SELECT title, description, user_id, qn_id FROM "+self.qn_tb_name+" WHERE qn_id=%s"
            self.cursor.execute(query, (qn_id,))
            row = self.cursor.fetchone()
            super().close_conn()
            return row
        except (Exception) as error:
            pprint(error)
            super().close_conn()
            return False

    def delete_question(self, qn_id):
        ''' removes a specific question from the database '''
        try:
            query = "DELETE FROM "+self.qn_tb_name+" WHERE qn_id=%s"
            self.cursor.execute(query, (qn_id,))
            super().close_conn()
            return True
        except (Exception) as error:
            pprint(error)
            super().close_conn()
            return False
        
    def get_questions(self):
        ''' gets all the questions in the database '''
        try:
            query = "SELECT title, description, user_id, qn_id FROM "+self.qn_tb_name+""
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            super().close_conn()
            return rows
        except (Exception) as error:
            pprint(error)
            super().close_conn()
            return None
        
    def get_questions_by_user_id(self, user_id):
        ''' gets all the questions the specified user has ever asked from the database '''
        try:
            query = "SELECT title, description, user_id, qn_id FROM "+self.qn_tb_name+" WHERE user_id=%s"
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
        ''' updates a specific question in the database '''
        try:
            query = "UPDATE "+self.qn_tb_name+" SET description=%s WHERE qn_id=%s"
            self.cursor.execute(query, (description,qn_id))
            super().close_conn()
            return True
        except (Exception) as error:
            pprint(error)
            self.conn.rollback()
            super().close_conn()
            return False

    def check_title(self, title):
        ''' checks if a question with the specified title already exists in the database '''
        try:
            query = "SELECT title, description, user_id, qn_id FROM "+self.qn_tb_name+" WHERE title=%s"
            self.cursor.execute(query, (title,))
            row = self.cursor.fetchone()
            super().close_conn()
            return row
        except (Exception) as error:
            pprint(error)
            super().close_conn()
            return False

    def check_description(self, description):
        ''' checks if a question with the specified description already exists in the database '''
        try:
            query = "SELECT title, description, user_id, qn_id FROM "+self.qn_tb_name+" WHERE description=%s"
            self.cursor.execute(query, (description,))
            row = self.cursor.fetchone()
            super().close_conn()
            return row
        except (Exception) as error:
            pprint(error)
            super().close_conn()
            return False
