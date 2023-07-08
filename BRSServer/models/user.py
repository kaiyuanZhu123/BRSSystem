from db_config import db_init as db


# 定义user模型类
class Users(db.Model):
    __tablename__ = 'user'
    userid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    account = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return '<User id:%s name:%s account:%s>' % (self.userid, self.name, self.account)
