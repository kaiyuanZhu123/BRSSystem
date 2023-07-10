from db_config import db_init as db

class Collections(db.Model):
    __tablename__ = 'collection'
    userid = db.Column(db.Integer, primary_key=True)
    bookid = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Collection bookid:%s userid:%s>' % (self.bookid, self.userid)

