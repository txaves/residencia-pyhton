import time
from json import dumps, loads

from services.database import MyDatabase

class PostModel:
    database_service: MyDatabase = None
    def __init__(self, user_name, content, id=None) -> None:
        if id:
            self.id = id
        else:
            self.id = round(time.time() * 1000)
        self.user_name = user_name
        self.content = content

    @classmethod
    def find_post(cls, post_id):
        found_post = None
        result = cls.database_service.find_post(post_id)
        print(result)
        if result:
            found_post = PostModel(result[1], result[2], result[0])
        return found_post
    @classmethod
    def add_post(cls, post):
        cls.database_service.create_post(post)
    
    @classmethod
    def list_to_dict(cls):
        result = cls.database_service.list_posts()
        post_list = []
        for post in result:
            post_list.append(PostModel(post[1], post[2], post[0]))
        return loads(dumps(post_list, default=PostModel.to_dict))

    @classmethod
    def remove_post(cls, post):
        cls.database_service.delete_post(post)

    @classmethod
    def edit_post(cls, post):
        cls.database_service.edit_post(post)

    def to_dict(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "text": self.content,
        }

    