import string

def is_pangram(s):
    _list = []
    _numbers = ['0','1','2','3','4','5','6','7','8','9']
    _alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(s)):
        if s[i] not in _list and s[i] not in _numbers and s[i] !=' ' and s[i] != '!' and s[i] !=',' and s[i] !='.':
            _list.append(s[i].lower())
    
    _result = list(set(_list) ^ set(_alphabet_list))

    if len(_result) == 0:
        return True
    else:
        return False
    
    
print(is_pangram("ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ"))

