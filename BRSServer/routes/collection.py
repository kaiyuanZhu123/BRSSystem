from flask import Blueprint, request

collection = Blueprint('collection', __name__)
from api.collection import *


@collection.route('/addcollection', methods=['GET'])
def addCollection():
    bookid = request.args.get('bookid')
    userid = request.args.get('userid')
    data = Collection_addCollection(bookid, userid)
    return data

@collection.route('/hadcollection', methods=['GET'])
def hadCollection():
    bookid = request.args.get('bookid')
    userid = request.args.get('userid')
    data = Collection_hadCollection(bookid, userid)
    return data

@collection.route('/findcollectionbyuserid', methods=['GET'])
def findCollectionByUserid():
    userid = request.args.get('userid')
    booklist = Collection_findCollectionByUserid(userid)
    return booklist

@collection.route('/searchbookincollection', methods=['GET'])
def searchBookInCollection():
    userid = request.args.get('userid')
    keyword = request.args.get('keyword')
    booklist = Collection_searchBookInCollection(userid, keyword)
    return booklist