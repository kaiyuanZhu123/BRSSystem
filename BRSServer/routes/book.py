from flask import Blueprint, request

book = Blueprint('book', __name__)
from api.book import *


@book.route('/addbook', methods=['GET'])
def addBook():
    data = Book_addBook()
    return 'ok'


@book.route('/addceshi', methods=['GET'])
def add():
    data = Book_addceshi()
    return data


@book.route('/newbooklist', methods=['GET'])
def newBookList():
    data = Book_newBookList()
    return data


@book.route('/mostPopular', methods=['GET'])
def mostPopular():
    data = Book_mostPopular()
    return data

@book.route('/guessuserlike', methods=['GET'])
def guessUserLike():
    data = Book_guessUserLike()
    return data

@book.route('/searchbook', methods=['GET'])
def searchBook():
    keyword = request.args['keyword']
    data = Book_searchBook(keyword)
    return data

@book.route('/similarbook', methods=['GET'])
def similarBook():
    data = Book_similarBook()
    return data

@book.route('/findbookbyid', methods=['GET'])
def findBookById():
    id = request.args['bookid']
    data = Book_findBookById(id)
    return data