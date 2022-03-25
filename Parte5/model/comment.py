import time

class CommentModel:
    def __init__(self, user_name, text) -> None:
        self.id = round(time.time() * 1000)
        self.user_name = user_name
        self.text = text

    def to_dict(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "text": self.text
        }