from .db_handler import DbHandler
from pprint import pprint
import datetime


class CommentHandler(DbHandler):
    ''' 
    This method handles all the database functions of the answer model
    '''
    # table cols
    def __init__(self):
        super().__init__()

    def insert_qn_comment(self, user_id, qn_id, comment):
        try:
            query = "INSERT INTO answers (comment, qn_id, user_id, create_date) VALUES(%s,%s,%s,%s)"
            self.cursor.execute(
                query, (comment, qn_id, user_id, datetime.datetime.now()))
            # close connection
            super().close_conn()
            return True
        except (Exception) as error:
            pprint(error)
            self.conn.rollback()
            super().close_conn()
            return False

    def insert_ans_comment(self):
        pass

    def update_qn_comment(self):
        pass

    def update_ans_comment(self):
        pass

    def get_qn_comment_by_qn_id(self):
        pass

    def get_ans_comment_by_ans_id(self):
        pass

    def check_repeated_ans_comment(self):
        pass

    def check_repeated_qn_comment(self):
        pass

    
        
