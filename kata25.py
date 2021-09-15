def filter_list(l):
  _return = []

  for i in l:
      if type(i) is type(0):
          _return.append(i)
   
  return _return

print(filter_list([1,2,'aasf','1','123',123]))