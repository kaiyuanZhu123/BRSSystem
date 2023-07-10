from flask import Blueprint, request

user = Blueprint('user', __name__)
import json
from api.user import *


@user.route('/list', methods=['GET'])
def list():
    # api的业务逻辑方法
    data = User_list()
    return data


@user.route('/login', methods=['GET'])
def login():
    account = request.args['account']
    pwd = request.args['password']

    data = User_login(account, pwd)
    if len(data) == 0:
        data.update({"result": "false"})
    else:
        data.update({"result": "true"})
    return data


@user.route('/register', methods=['POST'])
def reg():
    data = json.loads(request.data)
    data = User_reg({
        "name": data['params']['username'],
        "password": data['params']['password']
    })
    return data

@user.route('/changename', methods=['GET'])
def changename():
    userid = request.args.get('userid')
    username = request.args.get('username')
    return User_changename(userid=userid, username=username)
