from flask import Flask, request
import json
from routes.user import user
from routes.book import book
# app = Flask(__name__)
from db_config import app


# 跨域  pip install flask_cors
from flask_cors import CORS
CORS(app)


# user模块
app.register_blueprint(user, url_prefix="/user")
# Book模块
app.register_blueprint(book, url_prefix="/book")


@app.route('/')
def ping():
    return "ok"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)
