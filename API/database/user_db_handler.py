from .db_handler import DbHandler
from pprint import pprint
import datetime


class UserHandler(DbHandler):

    ''' user_id, username, password, create_date, last_login '''
    def __init__(self):
        super().__init__()
        
    def insert_user(self, username, password):
        try:
            query = "INSERT INTO users VALUES ({},{},{},{},{})"
            self.cursor.execute(query.format('NULL', username, password, datetime.datetime.now(), 'NULL'))
            self.cursor.close()
            self.conn.close()
            return True
        except (Exception) as error:
            pprint(error)
            self.conn.close()
            return False

    def update_username(self, user_id, username):
        try:
            query = "UPDATE users SET username={} WHERE user_id={}"
            self.cursor.execute(query.format(username,user_id))
            super().close_conn()
            return True
        except (Exception) as error:
            pprint(error)
            super().close_conn()
            return False

    def get_user_by_id(self, user_id):
        try:
            query = "SELECT user_id, username, password FROM users WHERE user_id={}"
            self.cursor.execute(query.format(user_id))
            row = self.cursor.fetchone()
            super().close_conn()
            return row
        except (Exception) as error:
            pprint(error)
            super().close_conn()
            return False

    def get_user_by_username(self, username):
        try:
            query = "SELECT user_id, username, password FROM users WHERE username={}"
            self.cursor.execute(query.format(username))
            row = self.cursor.fetchone()
            super().close_conn()
            return row
        except (Exception) as error:
            pprint(error)
            super().close_conn()
            return False

    def delete_user(self, username):
        try:
            query = "DELETE FROM users WHERE username={}"
            self.cursor.execute(query.format(username))
            row = self.cursor.fetchone()
            super().close_conn()
            return True
        except (Exception) as error:
            pprint(error)
            self.conn.close()
            return False
