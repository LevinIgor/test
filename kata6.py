def repeat_str(repeat, string):
    _str = ""
    for i in range(repeat):
        _str+=string
    return _str
print(repeat_str(4,"a"))