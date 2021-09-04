def filter_list(l):
    returnList = []
    for i in l:
        if isinstance(i,int):
            returnList.append(i)
           
    return returnList


print(filter_list([1,2,'aasf','1','123',123]))
