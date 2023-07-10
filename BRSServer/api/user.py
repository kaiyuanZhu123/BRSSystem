from operation.user import User_operation
from utils.data_process import Class_To_Data


def User_list():
    #
    u_o = User_operation()
    data = u_o._all()
    # data（复杂对象）====> 数据
    data = Class_To_Data(data, u_o.__fields__, 0)
    return data


def User_reg(kwargs):
    u_o = User_operation()
    data = u_o._reg(kwargs)
    return data


def User_login(account, pwd):
    u_o = User_operation()
    user = u_o._login(account, pwd)
    data = Class_To_Data(user, u_o.__fields__, 1)
    return data

def User_getnamebyid(userid):
    u_o = User_operation()
    username = u_o._getnamebyid(userid)
    return username

def User_changename(userid, username):
    u_o = User_operation()
    return u_o._changename(userid=userid, username=username)
