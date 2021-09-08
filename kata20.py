def solution(s):
    _List = []
    _returnList = list(s)
    i = 0
    
    if len(s)%2>0:
        while i < (len(s)-1):
            _List.append(str(_returnList[i]) + str(_returnList[i+1]))
            i=i+2
        _List.append(str(_returnList[len(_returnList)-1]) + "_")
    else:
        while i < (len(s)):
            print(i)
            _List.append(str(_returnList[i])+str(_returnList[i+1]))
            i=i+2
    
    return _List




print(solution("asasssa"))