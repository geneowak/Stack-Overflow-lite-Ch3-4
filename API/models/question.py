import datetime
import psycopg2
from API.database.question_db_handler import QuestionHandler
from API.database.database_ini import default_db_config

class Question:
    ''' cols in tb: qn_id, title, body, user_id, create_date '''

    def __init__(self, title, body, user_id):
        self.user_id = user_id
        self.title = title
        self.body = body
        self.answers = []
        self.comments = []

    def json(self):
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "answers": self.answers,
            "comments": self.comments
        }

    @classmethod
    def add_question(cls, data):
        result = QuestionHandler()
        return result.insert_question(self.title, self.body, self.user_id)

    @classmethod
    def get_question_by_id(cls, questionId):
        try:
            # check if question id is in required format
            questionId = float(questionId)
        except:
            return None
        for qn in cls.questions:
            if float(qn['id']) == float(questionId):
                return qn
        return None

    @classmethod
    def get_questions(cls):
        query = 
        from .answer import Answer

        for qn in cls.questions:
            qn['answers'].extend(Answer.get_answers_by_qn_id(qn['id']))
        return cls.questions

    @classmethod
    def get_no_of_qns(cls):
        return len(cls.questions)

    @classmethod
    def check_qn_title(cls, title):
        ''' check if a question has been asked before '''
        for qn in cls.questions:
            if (qn['title']).lower() == title.lower():
                return True
        return False

    @classmethod
    def check_qn_body(cls, body):
        ''' check if a question has been asked before '''
        for qn in cls.questions:
            if (qn['body']).lower() == body.lower():
                return True
        return False
        
