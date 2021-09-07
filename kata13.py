def move_zeros(array):
    _array = []
    _count = 0
    for i in range(len(array)):
        if array[i] !=0:
            _array.append(array[i])
        else:
            _count+=1
    for i in range(_count):
        _array.append(0)

    return _array

print(move_zeros([0,32,32,4,5,2,3,4,0,5,4,3,2,1,2,3,4]))