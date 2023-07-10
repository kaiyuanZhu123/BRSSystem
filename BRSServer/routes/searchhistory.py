from flask import Blueprint, request

searchhistory = Blueprint('searchhistory', __name__)
from api.searchhistory import *


@searchhistory.route('/add', methods=['GET'])
def addSearchHistory():
    userid = request.args.get('userid')
    date = request.args.get('date')
    keyword = request.args.get('keyword')
    data = SearchHistory_add(userid=userid, date=date, keyword=keyword)
    return data

@searchhistory.route('allbyuserid', methods=['GET'])
def allByUserid():
    userid = request.args.get('userid')
    data = SearchHistory_allByUserid(userid)
    return data

@searchhistory.route('searchhistory', methods=['GET'])
def searchHistory():
    keyword = request.args.get('keyword')
    data = SearchHistory_searchHistory(keyword)
    return data