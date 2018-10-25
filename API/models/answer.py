from .question import Question

class Answer:
    ''' this class will handle all the data processing for answers '''
    answers = []
    
    def __init__(self, _id, body, qn_id):
        self.id = _id
        self.body = body
        self.qn_id = qn_id
        self.comments = []

    def json(self):
        return {
            "id": self.id,
            "body": self.body,
            "comments": self.comments
        }

    @classmethod
    def add_answer(cls, answer):
        ''' this first checks if a question exists and if it does, it adds an answer to it
        True is returned for success and False when it fails to add the answer '''
        if Question.get_question_by_id(answer.qn_id):
            ans ={
                "id": answer.id,
                "body": answer.body,
                "qn_id": answer.qn_id,
                "comments": []
            }
            cls.answers.append(ans)
            try:
                Question.add_answer(answer.qn_id, ans)
            except:           
                return False
            return True
        return False

    @classmethod
    def add_comment(cls, answerId, comment):
        answer = cls.get_answer_by_id(answerId)
        if answer:
            answer['comments'].append(comment)
            return True
        return False

    @classmethod
    def get_answers(cls):
        return cls.answers

    @classmethod
    def get_answers_by_qn_id(cls, qn_id):
        return list(filter(lambda ans: ans['qn_id'] == qn_id, cls.answers))
        
    @classmethod
    def get_no_of_ans(cls):
        return len(cls.answers)

    @classmethod
    def check_ans_body(cls, body, qn_id):
        ''' check if an answer has already been given '''
        for ans in cls.answers:
            if str(ans['qn_id']) == str(qn_id):
                if ans['body'].lower() == body.lower():
                    return True
        return False

    @classmethod
    def get_answer_by_id(cls, answerId):
        try:
            # check if answer id is in required format
            answerId = float(answerId)
        except:
            return None
        for ans in cls.answers:
            if float(ans['id']) == answerId:
                return ans
        return None
