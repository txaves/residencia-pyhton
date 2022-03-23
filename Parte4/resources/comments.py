from json import dumps, loads
from flask_restful import Resource, reqparse
from model.comment import CommentModel

from model.post import PostModel

class Comment(Resource):
    def get(self, post_id, comment_id=None):
        found_post = PostModel.find_post(post_id)
        if found_post:
            if comment_id:
                found_comment = found_post.find_comment(comment_id)
                if found_comment:
                    return found_comment.to_dict()
                return {"message": "Comment not found"}, 404
            else:
                return found_post.comments_to_dict()
        else:
            return {"message": "Post not found"}, 404
    def post(self, post_id):
        found_post = PostModel.find_post(post_id)
        if found_post:
            body_arguments = reqparse.RequestParser()
            body_arguments.add_argument("user_name")
            body_arguments.add_argument("text")

            params = body_arguments.parse_args()
            new_comment = CommentModel(params["user_name"], params["text"])
            found_post.add_comment(new_comment)
            return new_comment.to_dict()
        else:
            return {"message": "Post not found"}, 404 

    def delete(self, post_id, comment_id):
        found_post = PostModel.find_post(post_id)
        if found_post:
            if comment_id:
                found_comment = found_post.find_comment(comment_id)
                if found_comment:
                    found_post.remove_comment(found_comment)
                    return found_comment.to_dict()
                return {"message": "Comment not found"}, 404
            else:
                return found_post.comments_to_dict()
        else:
            return {"message": "Post not found"}, 404

    def put(self, post_id, comment_id):
        found_post = PostModel.find_post(post_id)
        if found_post:
            if comment_id:
                found_comment = found_post.find_comment(comment_id)
                if found_comment:
                    body_arguments = reqparse.RequestParser()
                    body_arguments.add_argument("text")
                    params = body_arguments.parse_args()
                    found_comment.text = params.text
                    return found_comment.to_dict()
                return {"message": "Comment not found"}, 404
            else:
                return found_post.comments_to_dict()
        else:
            return {"message": "Post not found"}, 404