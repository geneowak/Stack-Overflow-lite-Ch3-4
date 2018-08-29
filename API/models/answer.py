from .question import Question
from API.database.answer_db_hander import AnswerHandler
from pprint import pprint

class Answer:
    ''' this class will handle all the data processing for answers '''
    
    def __init__(self, body, qn_id, user_id, ans_id = None):
        self.ans_id = ans_id
        self.body = body
        self.qn_id = qn_id
        self.user_id = user_id
        self.comments = []

    def json(self):
        return {
            "ans_id": self.ans_id,
            "qn_id": self.qn_id,
            "user_id": self.user_id,
            "answer": self.body,
            "comments": self.comments
        }

    @classmethod
    def add_answer(cls, answer):
        ''' this first checks if a question exists and if it does, it adds an answer to it
        True is returned for success and False when it fails to add the answer '''
        if Question.get_question_by_id(answer.qn_id):
            handle = AnswerHandler()
            pprint(answer.json())
            handle.insert_answer(answer.user_id, answer.qn_id, answer.body)
            return True
        return False

    @classmethod
    def get_answers(cls):
        handle = AnswerHandler()
        answers = handle.get_answers()
        answersList = []
        if answers:
            for answer in answers:
                qn = Answer(answer[0], answer[1], answer[2], answer[3])
                answersList.append(qn)

            return [x.json() for x in answersList]
        # from .answer import Answer
        # for qn in cls.questions:
        #     qn['answers'].extend(Answer.get_answers_by_qn_id(qn['id']))
        return answersList

    @classmethod
    def get_answers_by_qn_id(cls, qn_id):
        handle = AnswerHandler()
        answers = handle.get_answers_by_qn_id(qn_id)
        answersList = []
        if answers:
            for answer in answers:
                ans = Answer(answer[0], answer[1], answer[2], answer[3])
                answersList.append(ans)

            # append comments....

            return [x.json() for x in answersList]
        return answersList

    @classmethod
    def check_ans_body(cls, body, qn_id):
        ''' check if an answer has already been given '''
        handle = AnswerHandler()
        return handle.check_body(body, qn_id)

    @classmethod
    def get_answer_by_id(cls, answerId):
        handle = AnswerHandler()
        answer = handle.get_answers_by_ans_id(answerId)
        print(answer)
        if answer:
            return Answer(answer[0], answer[1], answer[2], answer[3])
        return None

    @classmethod
    def update_answer(cls, ans_id, body):
        print("ans_id:", ans_id, " body:", body)
        handle = AnswerHandler()
        question = handle.update_answer(ans_id, body)
        print(question)
        if question:
            return True
        return False

    @classmethod
    def accept_answer(cls, ans_id, qn_id):
        print("ans_id:", ans_id, " qn_id:", qn_id)
        handle = AnswerHandler()
        question = handle.accept_answer(ans_id, qn_id)
        if question:
            return True
        return False
