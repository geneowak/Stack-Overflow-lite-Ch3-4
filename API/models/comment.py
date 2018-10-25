from API.models.question import Question
from API.models.answer import Answer
from API.database.comment_db_handler import CommentsHandler
from pprint import pprint


class Comment:

    comments = []
    # question comment table cols: id, comment, qn_id, user_id, create_date
    # answer comment table cols: id, comment, ans_id, user_id, create_date
    def __init__(self, user_id, comment, parent, parent_id):
        self.user_id = user_id
        self.comment = comment
        self.parent = parent # NUM 'question', 'comment'
        self.parent_id = parent_id

    def json(self):
        return {
            "user_id": self.user_id,
            "comment": self.comment,
            "parent": self.parent,
            "parent_id": self.parent_id
        }

    def add_comment(self):
        ''' this method first checks if a parent exists and if it does, it adds an comment to it
        True is returned for success and False when it fails to add the comment '''
        pprint("adding comment...")
        pprint(self.json())
        if self.parent.lower() == 'question':
            # print(self.json())
            if Question.get_question_by_id(self.parent_id):
                try:
                    handler = CommentsHandler()
                    handler.insert_qn_comment(self.user_id, self.parent_id, self.comment)
                except:
                    return False
                return True
            return False
        elif self.parent.lower() == 'answer':
            if Answer.get_answer_by_ans_id(self.parent_id):
                try:
                    handler = CommentsHandler()
                    handler.insert_ans_comment(self.user_id, self.parent_id, self.comment)
                except:
                    return False
                return True
            return False
        return False
            
    @classmethod
    def get_comments(cls):
        handle = CommentsHandler()
        qn_comments = handle.get_qn_comments()
        handle = CommentsHandler()
        ans_comments = handle.get_ans_comments()
        pprint(ans_comments)
        commentsList = {
            "question_comments":[],
            "answer_comments":[]
        }
        # question comment table cols: id, comment, qn_id, user_id, create_date
        # answer comment table cols: id, comment, ans_id, user_id, create_date
        # user_id, comment, parent, parent_id
        if qn_comments:
            for comment in qn_comments:
                qn = Comment(comment["user_id"], comment["comment"], "question", comment["qn_id"])
                commentsList["question_comments"].append(qn.json())
        if ans_comments:
            for comment in ans_comments:
                qn = Comment(comment["user_id"], comment["comment"], "answer", comment["ans_id"])
                commentsList["answer_comments"].append(qn.json())

            return commentsList
        # from .answer import Answer
        # for qn in cls.questions:
        #     qn['comments'].extend(Answer.get_comments_by_qn_id(qn['id']))
        return commentsList

    @classmethod
    def get_comments_by_parent_id(cls,parent, parent_id):
        return list(filter(lambda comm: comm['parent'] == parent and comm['parent_id'] == parent_id, cls.comments))

    def check_for_repeated_comment(self):
        ''' check if an comment has already been given '''
        for comm in cls.comments:
            if comm['parent'].lower() == parent.lower():
                if str(comm['parent_id']) == str(parent_id):
                    if comm['comment'].lower() == comment.lower():
                        return True
        return False
