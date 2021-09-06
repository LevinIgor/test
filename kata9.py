def odd_or_even(arr):
    summ = 0
    for i in arr:
        summ +=i
    if summ%2>0:
        return "odd"
    else:
        return "even"
  


print(odd_or_even([0]))