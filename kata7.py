def solution(s):
    _str = ""
    for i in range(len(s)):
        if s[i].isupper():
            _str+=" " + s[i]
        else:
            _str+=s[i]
    return _str       


print(solution("fdfFdd"))