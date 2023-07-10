from operation.collection import Collection_operation
from utils.data_process import Class_To_Data
from api.book import Book_findBookById
from operation.book import Book_operation

def Collection_addCollection(bookid, userid):
    c_o = Collection_operation()
    data = c_o._addcollection(bookid, userid)
    return data

def Collection_hadCollection(bookid, userid):
    c_o = Collection_operation()
    data = c_o._hadcollection(bookid, userid)
    return data

def Collection_findCollectionByUserid(userid):
    c_o = Collection_operation()
    collection_list = c_o._findcollectionbyuserid(userid)
    # 根据list中的bookid返回book_list
    book_list = []
    for i in collection_list:
        book = Book_findBookById(i.bookid)
        book_list.append(book)
    return book_list

def Collection_searchBookInCollection(userid, keyword):
    c_o = Collection_operation()
    collection_list = c_o._findcollectionbyuserid(userid)
    book_list = []
    for i in collection_list:
        book = Book_findBookById(i.bookid)
        if keyword in book["title"]:
            book_list.append(book)
    return book_list
