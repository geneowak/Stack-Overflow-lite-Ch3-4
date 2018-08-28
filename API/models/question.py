import datetime
from API.database.question_db_handler import QuestionHandler

class Question:
    ''' cols in tb: qn_id, title, body, user_id, create_date '''
    questions = []
    def __init__(self, title, body, user_id):
        self.user_id = user_id
        self.title = title
        self.body = body
        self.answers = []
        self.comments = []

    def json(self):
        return {
            "user_id": self.user_id,
            "title": self.title,
            "body": self.body,
            "answers": self.answers,
            "comments": self.comments
        }

    def add_question(self, data):
        result = QuestionHandler()
        return result.insert_question(self.user_id, self.title, self.body)

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
        
