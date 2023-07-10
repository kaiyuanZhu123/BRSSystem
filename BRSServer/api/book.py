from operation.book import Book_operation
from utils.data_process import Class_To_Data


def Book_addBook():
    b_o = Book_operation()
    data = b_o._addbook()
    return data

def Book_addceshi():
    b_o = Book_operation()
    data = b_o._addceshi()
    return data

def Book_newBookList():
    b_o = Book_operation()
    data = b_o._newBookList()
    data = Class_To_Data(data, b_o.__fields__, 0)
    return data

def Book_mostPopular():
    b_o = Book_operation()
    data = b_o._mostPopular()
    data = Class_To_Data(data, b_o.__fields__, 0)
    return data

def Book_guessUserLike():
    b_o = Book_operation()
    data = b_o._guessUserLike()
    data = Class_To_Data(data, b_o.__fields__, 0)
    return data

def Book_searchBook(keyword):
    b_o = Book_operation()
    data = b_o._searchBook(keyword)
    data = Class_To_Data(data, b_o.__fields__, 0)
    return data

def Book_similarBook():
    b_o = Book_operation()
    data = b_o._similarBook()
    data = Class_To_Data(data, b_o.__fields__, 0)
    return data

def Book_findBookById(id):
    b_o = Book_operation()
    data = b_o._findBookById(id)
    data = Class_To_Data(data, b_o.__fields__, 1)
    return data