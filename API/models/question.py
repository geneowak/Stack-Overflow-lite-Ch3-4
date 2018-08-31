import datetime
from API.database.question_db_handler import QuestionHandler
from API.database.user_db_handler import UserHandler

class Question:
    ''' cols in tb: qn_id, title, body, user_id, create_date '''
    questions = []
    def __init__(self, title, body, user_id, qn_id = None):
        self.user_id = user_id
        self.title = title
        self.body = body
        self.qn_id = qn_id
        self.answers = []
        self.comments = []

    def json(self):
        handle = UserHandler()
        user = handle.get_user_by_id(self.user_id)
        return {
            "qn_id": self.qn_id,
            "username": user['username'],
            "question": self.title,
            "description": self.body,
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
        handle = QuestionHandler()
        question = handle.get_question_by_id(questionId)
        if question:
            qn = Question(question[0], question[1], question[2], question[3])
            from .answer import Answer
            qn.answers.extend(Answer.get_answers_by_qn_id(qn.qn_id))
            return qn
        return None

    @classmethod
    def get_questions(cls):
        handle = QuestionHandler()
        questions = handle.get_questions()
        questionsList = []
        if questions:
            for question in questions:
                qn = Question(question['title'], question['body'],question['user_id'],question['qn_id'])
                questionsList.append(qn)

            return [ x.json() for x in questionsList] 
        # from .answer import Answer
        # for qn in cls.questions:
        #     qn['answers'].extend(Answer.get_answers_by_qn_id(qn['id']))
        return questionsList

    @classmethod
    def check_qn_title(cls, title):
        ''' check if a question has been asked before '''
        handle = QuestionHandler()
        return handle.check_title(title)

    @classmethod
    def check_qn_body(cls, body):
        ''' check if a question has been asked before '''
        handle = QuestionHandler()
        return handle.check_body(body)
        
    @classmethod
    def delete_question(cls, qn_id):
        try:
            # check if question id is in required format
            questionId = float(qn_id)
        except:
            return None
        handle = QuestionHandler()
        question = handle.delete_question(questionId)
        if question:
            return True 
        return False

    @classmethod
    def update_question(cls, qn_id, body):
        try:
            # check if question id is in required format
            qn_id = float(qn_id)
        except:
            return None
        handle = QuestionHandler()
        question = handle.update_question(qn_id, body)
        if question:
            return True 
        return False

