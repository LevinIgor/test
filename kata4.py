def high_and_low(numbers):
    numb =[]
    numb = numbers.split(' ')
    _min = 1000000
    _max= -100000
    for i in numb:
        if int(_min)>int(i):
            _min=i
        if int(_max) < int(i):
            _max=i
    return str(str(_max)+" "+ str(_min))


print(high_and_low("1 2 3"))