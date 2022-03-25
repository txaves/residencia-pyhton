from flask import Flask
from flask_restful import Api
from model.post import PostModel
from resources.posts import Post
from services.database import MyDatabase

app = Flask(__name__)
api = Api(app)
database = MyDatabase()

PostModel.database_service = database
api.add_resource(Post, "/post/<int:id>" , "/post")

if __name__ == '__main__':
    app.run(debug=True)