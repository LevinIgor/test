def duplicate_encode(word):
    _duplicate = []
    word = word.upper()
    _return_str=""
    
    for i in range(len(word)):
        temp = word[i]
        for j in range(i+1,len(word)):
            if temp == word[j]:
              _duplicate.append(word[j])
    for i in range(len(word)):
        if(word[i] in _duplicate):
            _return_str+=')'
        else:
            _return_str+='('
    
        
    return _return_str 






print(duplicate_encode("din"))
#()(((()