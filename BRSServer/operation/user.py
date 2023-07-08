from models.user import Users
from db_config import db_init as db


class User_operation():
    def __init__(self):
        self.__fields__ = ['userid', 'name', 'password', 'account']

    def _all(self):
        user_list = Users.query.all()
        return user_list

    def _login(self, account, pwd):
        user = Users.query.filter_by(account=account, password=pwd).first()
        return user

    def _reg(self, kwargs):
        u = Users(**kwargs)
        userlist = self._all()
        if len(userlist) > 0:
            newUserId = userlist[len(userlist) - 1].userid + 1
        else:
            newUserId = 1
        u.account = newUserId
        u.userid = newUserId
        db.session.add(u)
        db.session.commit()
        return {"result": "success", "account": u.account}
