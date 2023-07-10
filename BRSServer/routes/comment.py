from flask import Blueprint, request

comment = Blueprint('comment', __name__)
from api.comment import *


@comment.route('/add', methods=['GET'])
def addCollection():
    bookid = request.args.get('bookid')
    userid = request.args.get('userid')
    date = request.args.get('date')
    comment = request.args.get('comment')
    data = Comment_add(bookid, userid, date, comment)
    return data

@comment.route('/findcommentbybookid', methods=['GET'])
def findCommentByBookid():
    bookid = request.args.get('bookid')
    data = Comment_findCommentByBookid(bookid)
    return data

@comment.route('/findcommentbyuserid', methods=['GET'])
def findCommentByUserid():
    userid = request.args.get('userid')
    data = Comment_findCommentByUserid(userid)
    return data

@comment.route('/searchcomment', methods=['GET'])
def searchComment():
    userid = request.args.get('userid')
    keyword = request.args.get('keyword')
    data = Comment_searchComment(userid=userid, keyword=keyword)
    return data