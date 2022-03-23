import time
from json import dumps, loads

from model.comment import CommentModel

class PostModel:
    _posts_list = list()
    def __init__(self, user_name, text) -> None:
        self.id = round(time.time() * 1000)
        self.user_name = user_name
        self.text = text
        self.comments = list()

    @classmethod
    def find_post(cls, post_id):
        found_post = None
        for post in cls._posts_list:
            if post.id == post_id:
                found_post = post
                break
        return found_post
    @classmethod
    def add_post(cls, post):
        cls._posts_list.append(post)
    
    @classmethod
    def list_to_dict(cls):
        return loads(dumps(cls._posts_list, default=PostModel.to_dict))

    @classmethod
    def remove_post(cls, post):
        cls._posts_list.remove(post)

    def add_comment(self, comment):
        self.comments.append(comment)

    def find_comment(self, comment_id):
        found_comment = None
        for comment in self.comments:
            if comment.id == comment_id:
                found_comment = comment
                break
        return found_comment

    def remove_comment(self, comment):
        self.comments.remove(comment)

    def comments_to_dict(self):
        return loads(dumps(self.comments, default=CommentModel.to_dict))

    def to_dict(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "text": self.text,
            "comments": loads(dumps(self.comments, default=CommentModel.to_dict))
        }

    