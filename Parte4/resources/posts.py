from json import dumps, loads
from flask_restful import Resource, reqparse
from model.post import PostModel

class Post(Resource):
    def get(self, id=None):
        if id:
            found_post = PostModel.find_post(id)
            if found_post:
                return found_post.to_dict()
            return {"message": "Post not found"}, 404
        else:
            return PostModel.list_to_dict()

    def post(self):
        body_arguments = reqparse.RequestParser()
        body_arguments.add_argument("user_name")
        body_arguments.add_argument("text")

        params = body_arguments.parse_args()
        new_post = PostModel(params["user_name"], params["text"])
        PostModel.add_post(new_post)
        return new_post.to_dict()
        
        
    def delete(self, id):
        found_post = PostModel.find_post(id)
        if found_post:
            PostModel.remove_post(found_post)
            return found_post.to_dict()
        return {"message": "Post not found"}, 404

    def put(self, id):
        found_post = PostModel.find_post(id)
        if found_post:
            body_arguments = reqparse.RequestParser()
            body_arguments.add_argument("text")
            params = body_arguments.parse_args()
            found_post.text = params.text
            return found_post.to_dict()
        return {"message": "Post not found"}, 404