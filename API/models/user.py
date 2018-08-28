


class UserModel:
    ''' user_id, username, password, create_date, last_login '''
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def add_user(self):
        query = "INSERT INTO users VALUES({},{},{},{},{})".format('NULL',)
        return False

    @classmethod
    def get_user_by_username(cls):
        pass
    
    @classmethod
    def get_user_by_id(cls):
        pass
