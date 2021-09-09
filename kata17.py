def order_weight(strng):
    _list = strng.split(' ')
    _weight = []

    for i in _list:
        temp = 0
        for j in range(len(i)):
            temp+=int(i[j])
        _weight.append({'w':i, 's':temp})
    newlist = sorted(_weight, key=lambda k: k['s']) 

    
    _str = ""
    for i in newlist:
        _str += i['w'] + " "

    return _str[0:-1]



print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))