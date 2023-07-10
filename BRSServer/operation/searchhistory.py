from models.searchhistory import SearchHistory
from db_config import db_init as db


class SearchHistory_operation():
    def __init__(self):
        self.__fields__ = ['userid', 'keyword', 'date']

    def _add(self, userid, keyword, date):
        s = SearchHistory(userid=userid, keyword=keyword, date=date)
        db.session.add(s)
        db.session.commit()
        return {'result': 'success', 'userid': userid, 'keyword': keyword, 'date': date}

    def _allbyuserid(self, userid):
        data = SearchHistory.query.filter_by(userid=userid).all()
        return data

    def _searchhistory(self, keyword):
        data = SearchHistory.query.filter(SearchHistory.keyword.like('%' + keyword + '%')).all()
        return data

