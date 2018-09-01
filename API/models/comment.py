from API.models.question import Question
from API.models.answer import Answer
class Comment:

    comments = []

    def __init__(self, _id, body, parent, parent_id):
        self.id = _id
        self.body = body
        self.parent = parent # NUM 'question', 'comment'
        self.parent_id = parent_id

    def json(self):
        return {
            "id": self.id,
            "body": self.body,
            "parent": self.parent,
            "parent_id": self.parent_id
        }

    @classmethod
    def add_comment(cls, comment):
        ''' this method first checks if a parent exists and if it does, it adds an comment to it
        True is returned for success and False when it fails to add the comment '''
        if comment.parent.lower() == 'question':
            print(comment.json())
            if Question.get_question_by_id(comment.parent_id):
                comm = {
                    "id": comment.id,
                    "body": comment.body,
                    "parent": comment.parent,
                    "parent_id": comment.parent_id
                }
                cls.comments.append(comm)
                return True
            return False
        elif comment.parent.lower() == 'answer':
            if Answer.get_answer_by_id(comment.parent_id):
                comm = {
                    "id": comment.id,
                    "body": comment.body,
                    "parent": comment.parent,
                    "parent_id": comment.parent_id
                }
                cls.comments.append(comm)
                try:
                    Answer.add_comment(comment.parent_id, comm)
                except:
                    return False
                return True
            return False
        return False
            
    @classmethod
    def get_comments(cls):
        return cls.comments

    @classmethod
    def get_comments_by_parent_id(cls,parent, parent_id):
        return list(filter(lambda comm: comm['parent'] == parent and comm['parent_id'] == parent_id, cls.comments))

    @classmethod
    def get_no_of_comments(cls):
        return len(cls.comments)

    @classmethod
    def check_for_repeated_comment(cls, body, parent, parent_id):
        ''' check if an comment has already been given '''
        for comm in cls.comments:
            if comm['parent'].lower() == parent.lower():
                if str(comm['parent_id']) == str(parent_id):
                    if comm['body'].lower() == body.lower():
                        return True
        return False
