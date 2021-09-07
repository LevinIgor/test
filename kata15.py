def find_missing_letter(chars):
    
    _alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    _input = chars
    _alphabet_list = list(_alphabet)
    
    _start_poss = 0
    for i in range(len(_alphabet_list)):
        if _alphabet[i] == _input[0]:
           _start_poss = i
           break


    iteral = 0
    for i in range(_start_poss,len(_input)+_start_poss):
        if _input[iteral] != _alphabet_list[i]:
            return(_alphabet_list[i])
        else:
            iteral+=1
    return -1
           
    

print(find_missing_letter(['O','Q','R','S']))