from models.comment import Comments
from db_config import db_init as db


class Comment_operation():
    def __init__(self):
        self.__fields__ = ['bookid', 'userid', 'date', 'comment']

    def _add(self, bookid, userid, date, comment):
        c = Comments(bookid=bookid, userid=userid, date=date, comment=comment)
        db.session.add(c)
        db.session.commit()
        return {"result": "success", "bookid": bookid, "userid": userid,\
                "date": date, "comment": comment}

    def _findcommentbybookid(self, bookid):
        comment_list = Comments.query.filter_by(bookid=bookid).all()
        return comment_list

    def _findcommentbyuserid(self, userid):
        comment_list = Comments.query.filter_by(userid=userid).all()
        return comment_list

