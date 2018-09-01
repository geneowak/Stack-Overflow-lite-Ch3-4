from .db_handler import DbHandler
from pprint import pprint
import datetime
from .database_ini import table_names


class CommentHandler(DbHandler):
    ''' 
    This method handles all the database functions of the answer model
    '''
    # table cols
    def __init__(self):
        super().__init__()
        self.qn_table_name = table_names["question_comments"]
        self.ans_table_name = table_names["answer_comments"]

    def insert_qn_comment(self, user_id, qn_id, comment):
        ''' adds a question comment to the database '''
        try:
            query = "INSERT INTO "+self.qn_table_name+" (comment, qn_id, user_id, create_date) VALUES(%s,%s,%s,%s)"
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
        ''' adds an answer comment to the database '''
        pass

    def update_qn_comment(self):
        ''' updates a question comment in the database '''
        pass

    def update_ans_comment(self):
        ''' updates an answer comment in the database '''
        pass

    def get_qn_comment_by_qn_id(self):
        ''' returns the specified question comment from the database '''
        pass

    def get_ans_comment_by_ans_id(self):
        ''' returns the specified answer comment from the database '''
        pass

    def delete_qn_comment_by_qn_id(self):
        ''' deletes the specified question comment from the database '''
        pass

    def delete_ans_comment_by_ans_id(self):
        ''' deletes the specified answer comment from the database '''
        pass

    def check_repeated_ans_comment(self):
        ''' checks if the specified answer comment already exists in the database '''
        pass

    def check_repeated_qn_comment(self):
        ''' checks if the specified question comment already exists in the database '''
        pass

    
        
