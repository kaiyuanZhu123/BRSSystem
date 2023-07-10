from operation.comment import Comment_operation
from utils.data_process import Class_To_Data
from api.user import User_getnamebyid
from api.book import Book_findBookById

def Comment_add(bookid, userid, date, comment):
    c_o = Comment_operation()
    data = c_o._add(bookid, userid, date, comment)
    return data

def Comment_findCommentByBookid(bookid):
    c_o = Comment_operation()
    comment_list = c_o._findcommentbybookid(bookid)
    data = Class_To_Data(comment_list, c_o.__fields__, 0)
    for i in data:
        userid = i['userid']
        username = User_getnamebyid(userid=userid)
        i['username'] = username
    return data

def Comment_findCommentByUserid(userid):
    c_o = Comment_operation()
    comment_list = c_o._findcommentbyuserid(userid)
    data = Class_To_Data(comment_list, c_o.__fields__, 0)
    for i in data:
        userid = i['userid']
        username = User_getnamebyid(userid=userid)
        i['username'] = username
        bookid = i['bookid']
        book = Book_findBookById(id=bookid)
        i['bookname']  = book['title']
        i['img'] = book['img']
    return data

def Comment_searchComment(userid, keyword):
    c_o = Comment_operation()
    comment_list = c_o._findcommentbyuserid(userid)
    result_list = []
    data = Class_To_Data(comment_list, c_o.__fields__, 0)
    for i in data:
        bookid = i['bookid']
        book = Book_findBookById(id=bookid)
        i['bookname'] = book['title']
        if (keyword in i['bookname']) or (keyword in i['comment']):
            userid = i['userid']
            username = User_getnamebyid(userid=userid)
            i['username'] = username
            i['img'] = book['img']
            result_list.append(i)
    return result_list