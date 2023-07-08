import datetime
from db_config import db_init as db


# 定义Book模型类
class Books(db.Model):
    __tablename__ = 'book'
    bookid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(32), nullable=False)  # 书名
    author = db.Column(db.String(32))
    catalog = db.Column(db.String(32), nullable=False)  # 分类
    publisher = db.Column(db.String(32))
    tags = db.Column(db.String(64))  # 标签
    img = db.Column(db.String(128))  # 图书封面
    reading = db.Column(db.String(32), default=0)  # 阅读人数
    online = db.Column(db.String(1024))  # 网购地址
    bytime = db.Column(db.DateTime, default=datetime.datetime)

    def __repr__(self):
        return '<Book bookid:%s title:%s>' % (self.bookid, self.title)

