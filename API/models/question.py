
class Question:

    questions = []

    def __init__(self, _id, title, body):
        self.id = _id
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
        question = {
            'id': data.id,  # using timestamps as ids
            "title": data.title,
            "body": data.body,
            "answers": [],
            "comments": []
        }
        print(question)
        cls.questions.append(question)
        return None

    ''' return True if answer is added, False otherwise '''
    @classmethod
    def add_answer (cls, questionId, answer):
        question = cls.get_question_by_id(questionId)

        if question:
            question['answers'].append(answer)
            return True
        return False

    @classmethod
    def add_comment (cls, questionId, comment):
        question = cls.get_question_by_id(questionId)

        if question:
            question['comments'].append(comment)
            return True
        return False

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

    # get all the questions with their answers on loading the application
    @classmethod
    def load_all_qns(cls):
        from .answer import Answer
        for qn in cls.questions:
            qn['answers'].extend(Answer.get_answers_by_qn_id(qn['id']))

    @classmethod
    def get_questions(cls):
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
        
