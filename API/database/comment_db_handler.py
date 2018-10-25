from .db_handler import DbHandler
from pprint import pprint
import datetime
from .database_ini import table_names


class CommentsHandler(DbHandler):
    '''
    This method handles all the database functions of the comment model
    '''

    # question comment table cols: id, comment, qn_id, user_id, create_date
    # answer comment table cols: id, comment, ans_id, user_id, create_date
    def __init__(self):
        super().__init__()
        self.qn_table_name = table_names["question_comments"]
        self.ans_table_name = table_names["answer_comments"]

    def insert_qn_comment(self, user_id, qn_id, comment):
        ''' adds a question comment to the database '''
        try:
            query = "INSERT INTO " + self.qn_table_name + " (comment, qn_id, user_id, create_date) VALUES(%s,%s,%s,%s)"
            self.cursor.execute(
                query, (comment, qn_id, user_id, datetime.datetime.now()))
            # close connection
            super().close_conn()
            return True
        except (Exception) as error:
            pprint("and error occured", error)
            self.conn.rollback()
            super().close_conn()
            return False

    def update_qn_comment(self, comment, qn_id):
        ''' updates a question comment in the database '''
        try:
            query = "UPDATE "+self.ans_table_name + " SET comment=%s WHERE qn_id=%s"
            self.cursor.execute(query, (comment, qn_id))
            # close connection
            super().close_conn()
            return True
        except (Exception) as error:
            pprint("and error occured", error)
            self.conn.rollback()
            super().close_conn()
            return False

    def get_qn_comment_by_qn_id(self, qn_id):
        ''' returns the specified question comment from the database '''
        try:
            query = "SELECT comment, id, user_id, qn_id FROM "+self.ans_table_name+" WHERE qn_id=%s"
            self.cursor.execute(query, (qn_id,))
            rows = self.cursor.fetchall()
            super().close_conn()
            return rows
        except (Exception) as error:
            pprint("and error occured", error)
            self.conn.rollback()
            super().close_conn()
            return False

    def delete_qn_comment_by_qn_id(self, comment_id):
        ''' deletes the specified question comment from the database '''
        try:
            query = "DELETE FROM "+self.qn_table_name+" WHERE id=%s"
            self.cursor.execute(query, (comment_id,))
            # close connection
            super().close_conn()
            return True
        except (Exception) as error:
            pprint("and error occured", error)
            self.conn.rollback()
            super().close_conn()
            return False

    def check_repeated_qn_comment(self, comment):
        ''' checks if the specified question comment already exists in the database '''
        try:
            query = "SELECT comment, id, user_id, qn_id FROM " + \
                self.qn_table_name+" WHERE comment=%s"
            self.cursor.execute(query, (comment,))
            row = self.cursor.fetchone()
            super().close_conn()
            return row
        except (Exception) as error:
            pprint("and error occured", error)
            super().close_conn()
            return False

    def insert_ans_comment(self, user_id, ans_id, comment):
        ''' adds an answer comment to the database '''
        try:
            query = "INSERT INTO "+self.ans_table_name + \
                " (comment, ans_id, user_id, create_date) VALUES(%s,%s,%s,%s)"
            self.cursor.execute(
                query, (comment, ans_id, user_id, datetime.datetime.now()))
            # close connection
            super().close_conn()
            return True
        except (Exception) as error:
            pprint("and error occured", error)
            self.conn.rollback()
            super().close_conn()
            return False

    def update_ans_comment(self, user_id, ans_id, comment):
        ''' updates an answer comment in the database '''
        try:
            query = "UPDATE "+self.ans_table_name + " SET comment=%s WHERE ans_id=%s"
            self.cursor.execute(query, (comment, ans_id))
            # close connection
            super().close_conn()
            return True
        except (Exception) as error:
            pprint("and error occured", error)
            self.conn.rollback()
            super().close_conn()
            return False

    def get_ans_comment_by_ans_id(self, user_id, ans_id, comment):
        ''' returns the specified answer comment from the database '''
        try:
            query = "SELECT comment, id, user_id, ans_id FROM "+self.ans_table_name+" WHERE ans_id=%s"
            self.cursor.execute(query, (ans_id,))
            rows = self.cursor.fetchall()
            super().close_conn()
            return rows
        except (Exception) as error:
            pprint("and error occured", error)
            self.conn.rollback()
            super().close_conn()
            return False

    def delete_ans_comment_by_ans_id(self, comment_id):
        ''' deletes the specified answer comment from the database '''
        try:
            query = "DELETE FROM "+self.ans_table_name+" WHERE id=%s"
            self.cursor.execute(query, (comment_id,))
            # close connection
            super().close_conn()
            return True
        except (Exception) as error:
            pprint("and error occured", error)
            self.conn.rollback()
            super().close_conn()
            return False

    def check_repeated_ans_comment(self, comment):
        ''' checks if the specified answer comment already exists in the database '''
        try:
            query = "SELECT comment, id, user_id, ans_id FROM " + \
                self.ans_table_name+" WHERE comment=%s"
            self.cursor.execute(query, (comment,))
            row = self.cursor.fetchone()
            super().close_conn()
            return row
        except (Exception) as error:
            pprint("and error occured", error)
            super().close_conn()
            return False

    
        
