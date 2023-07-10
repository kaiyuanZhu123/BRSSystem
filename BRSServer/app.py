from flask import Flask, request
import json
from routes.user import user
from routes.book import book
from routes.collection import collection
from routes.comment import comment
from routes.searchhistory import searchhistory
# app = Flask(__name__)
from db_config import app


# 跨域  pip install flask_cors
from flask_cors import CORS
CORS(app)


# user模块
app.register_blueprint(user, url_prefix="/user")
# Book模块
app.register_blueprint(book, url_prefix="/book")
# collection模块
app.register_blueprint(collection, url_prefix="/collection")
# comment模块
app.register_blueprint(comment, url_prefix="/comment")
# searchhistory模块
app.register_blueprint(searchhistory, url_prefix="/searchhistory")


@app.route('/')
def ping():
    return "ok"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
