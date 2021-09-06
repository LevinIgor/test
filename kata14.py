def iq_test(numbers):
    _list = numbers.split(' ')
    _event_count=0
    _pos=0

    for i in range(len(_list)):
        if int(_list[i])% 2 ==0:
            _event_count+=1
        else:
            _event_count-=1
    print(_event_count)
    if _event_count>0:
        for i in range(len(_list)):
            if int(_list[i])%2 != 0:
                _pos = i+1
    else:
        for i in range (len(_list)):
            if int(_list[i])%2 ==0:
                _pos=i+1
    return _pos
print(iq_test("0 2 4 6 7 8"))