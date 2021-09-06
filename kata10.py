def is_isogram(string):
    _repeat = []
    string = string.upper()
    for i in string:
        if i in _repeat:
            return "false"
        else:
            _repeat.append(i)
    return "true"

print(is_isogram("Aba"))