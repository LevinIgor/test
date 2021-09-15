def pig_it(text):
    _list = text.split(' ')
    _revers = []

    for i in _list:
        if i in ['!']:
            _revers.append(i)
        else:
            _revers.append((i[1:]+i[0]) + "ay")
     
    return ' '.join(_revers)

print(pig_it("Hello world !"))