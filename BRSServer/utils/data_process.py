
# 数据模型类===》普通字典
#    user/[user,user,user]    属性清单,

#                  数据源     数据模型类属性    0 obj / 1
def Class_To_Data(data_list, fields, type=0):
    if not type:  # [obj, obj]
        user_list = []  
        for u in data_list:
            if u != None:
                temp = {}
                for f in fields:
                    temp[f] = getattr(u, f)
            user_list.append(temp)

    else:  # obj
        user_list = {}
        if data_list != None:
            for f in fields:
                user_list[f] = getattr(data_list, f)

    return user_list