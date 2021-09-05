def longest(a1, a2):
    _newString = a1+a2
    _contain = []
    print(range(len(_newString)))
    for i in range(len(_newString)):
        if _newString[i] in _contain:
            continue
        else:
            _contain.append(_newString[i])
    _contain = sorted(_contain)
    _str = ""
    for i in range(len(_contain)):
        _str+=_contain[i]

    return _contain

print(longest("loopingisfunbutdangerous",("lessdangerousthancoding")))