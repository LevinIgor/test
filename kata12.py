def remove_smallest(numbers):
    if len(numbers) == 0: return numbers
    _min = numbers[0]
    _return = []
    for i in range(len(numbers)):
        if _min>numbers[i]:
            _min = numbers[i]
    for i in range(len(numbers)):
        if numbers[i]==_min:
            _min = ""
        else:
            _return.append(numbers[i])
    return _return


print(remove_smallest([0,1,0,1,2,3,4]))