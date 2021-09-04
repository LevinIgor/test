def descending_order(num):
    return_list = []
    for i in str(num):
        return_list.append(i)
    return_list.sort(reverse=True)
    return ''.join(return_list)


print(descending_order(390909))