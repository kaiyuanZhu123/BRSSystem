from models.collection import Collections
from db_config import db_init as db


class Collection_operation():
    def __init__(self):
        self.__fields__ = ['bookid', 'userid']

    def _addcollection(self, bookid, userid):
        oldCollection = Collections.query.filter_by(bookid=bookid).filter_by(userid=userid).first()
        if oldCollection == None:
            c = Collections(bookid=bookid, userid=userid)
            db.session.add(c)
            db.session.commit()
            return {"result": "success", "bookid": bookid, "userid": userid}
        else:
            db.session.delete(oldCollection)
            db.session.commit()
            return {"result": "cancelcollection", "bookid": bookid, "userid": userid}

    def _hadcollection(self, bookid, userid):
        collection = Collections.query.filter_by(bookid=bookid).filter_by(userid=userid).first()
        if collection == None:
            return {"collection": "no"}
        else:
            return {"collection": "yes"}

    def _findcollectionbyuserid(self, userid):
        collection_list = Collections.query.filter_by(userid=userid).all()
        return collection_list

