import datetime

from models.book import Books
from db_config import db_init as db


class Book_operation():
    def __init__(self):
        self.__fields__ = ['bookid', 'title', 'author', 'catalog', 'publisher',
                           'tags', 'img', 'reading', 'online', 'bytime']

    def _all(self):
        book_list = Books.query.all()
        return book_list

    def _findbyname(self, title):
        book = Books.query.filter_by(title=title).first()
        return book

    def _addbook(self, kwargs):
        b = Books(**kwargs)
        db.session.add(b)
        db.session.commit()
        return {"result": "success", "bookid": b.bookid}

    def _newBookList(self):
        # 从数据库中查询发行日期最近的9本书
        book_list = Books.query.order_by(Books.bytime.desc()).all()
        return book_list[:9]

    def _mostPopular(self):
        # 从数据库中查询阅读数最高的9本书
        book_list = Books.query.all()
        return book_list[:9]

    def _guessUserLike(self):
        # 使用推荐算法为用户推荐图书，目前简单地返回数据库中前9本书
        book_list = Books.query.all()
        return book_list[:9]

    def _searchBook(self, keyword):
        # 根据关键词在数据库中搜索相关的图书并返回
        book_list = Books.query.filter(Books.title.like('%' + keyword + '%')).all()
        return book_list

    def _similarBook(self):
        # 根据搜索结果推荐相似图书
        book_list = Books.query.all()
        return book_list[:9]

    def _addceshi(self):
        # 用于向数据库添加初始图书数据
        import requests
        from api.api_config import bookApiAddr_bookInfo, bookApiKey
        catalog_id = 5
        pn = 0
        error_code = True
        while error_code:
            re = requests.get(url=bookApiAddr_bookInfo,
                                  params={'key': bookApiKey, 'catalog_id': catalog_id, 'pn': pn, 'rn': 30})  # 带参数的get请求
            re = re.json()
            if re["error_code"] == 0:
                data = re["result"]["data"]
                for book in data:
                    bytime = book["bytime"]
                    bytime = datetime.datetime.strptime(bytime, '%Y年%m月%d日')
                    b = Books(bytime=bytime, catalog=book["catalog"], img=book["img"], online=book["online"],
                                  reading=book["reading"], tags=book["tags"], title=book["title"])
                    oldbook = Books.query.filter_by(title=b.title).first()
                    print(oldbook)
                    if oldbook is None:
                        db.session.add(b)
                db.session.commit()
                pn += 30
            else:
                error_code = False
        return "ok"
