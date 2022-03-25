from flask import Flask, abort, jsonify, request
from model.post import PostModel
app = Flask(__name__)

@app.route("/post", methods=["GET"])
def getAll():
    return jsonify({"posts":PostModel.list_to_dict()})

@app.route("/post", methods=["POST"])
def createPost():
    body_data = request.get_json()
    new_post = PostModel(body_data["user_name"], body_data["text"])
    PostModel.add_post(new_post)
    return jsonify(new_post.to_dict())

@app.route("/post/<int:id>", methods=["GET"])
def getPost(id):
    found_post = PostModel.find_post(id)
    if found_post:
        return jsonify(found_post.to_dict())
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)