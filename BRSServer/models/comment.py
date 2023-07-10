from db_config import db_init as db

class Comments(db.Model):
    __tablename__ = 'comment'
    userid = db.Column(db.Integer, nullable=False, primary_key=True)
    bookid = db.Column(db.Integer, nullable=False, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, primary_key=True)
    comment = db.Column(db.String(255))

    def __repr__(self):
        return '<Comment bookid:%s userid:%s date:%s comment:%s>' % (self.bookid, self.userid, self.date, self.comment)

