from operation.searchhistory import SearchHistory_operation
from utils.data_process import Class_To_Data

def SearchHistory_add(userid, keyword, date):
    s_o = SearchHistory_operation()
    data = s_o._add(userid, keyword, date)
    return data

def SearchHistory_allByUserid(userid):
    s_o = SearchHistory_operation()
    data = s_o._allbyuserid(userid)
    data = Class_To_Data(data, s_o.__fields__, 0)
    return data

def SearchHistory_searchHistory(keyword):
    s_o = SearchHistory_operation()
    data = s_o._searchhistory(keyword)
    data = Class_To_Data(data, s_o.__fields__, 0)
    return data
