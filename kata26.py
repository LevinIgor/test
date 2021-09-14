from arepl_dump import dump
def top_3_words(text):
    _alp = list(set(text))        
    _alp.remove(' ')
    _count = []
    

    for i in range(len(_alp)):
           _count.append(text.count(_alp[i]))

    for i in range(len(_alp)):
        
    return  _alp  

    




print(top_3_words("a a a  b  c c  d d d d  e e e e e"))