from API.database.user_db_handler import UserHandler


class UserModel:
    ''' user_id, username, password, create_date, last_login '''
    def __init__(self, username, password, user_id = None):
        self.username = username
        self.password = password
        self.user_id = user_id

    def add_user(self):
        handle = UserHandler()
        if handle.insert_user(self.username, self.password):
            return True
        return False

    @staticmethod
    def get_user_by_username(username):
        handle = UserHandler()
        row = handle.get_user_by_username(username)
        if row:
            return UserModel(row[0], row[1], row[2])
        return None
    
    @staticmethod
    def get_user_by_id(user_id):
        handle = UserHandler()
        row = handle.get_user_by_id(user_id)
        if row:
            return UserModel(row[0], row[1], row[2])
        return None

