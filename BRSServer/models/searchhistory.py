from db_config import db_init as db

class SearchHistory(db.Model):
    __tablename__ = 'searchhistory'
    userid = db.Column(db.Integer, primary_key=True)
    keyword = db.Column(db.String(32))
    date = db.Column(db.DateTime, primary_key=True)

    def __repr__(self):
        return '<SearchHistory userid:%s keyword:%s date:%s>' % (self.userid, self.keyword, self.date)

