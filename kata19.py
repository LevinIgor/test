def dirReduc(arr):

    for i in range(len(arr)):
        if arr[i] == "NORTH":
            for j in range(i+1,len(arr)-1):
                if arr[j] == "SOUTH":
                    arr[i] = ""
                    arr[j] = ""
                    break
        if arr[i] == "SOUTH":
            for j in range(i+1,len(arr)-1):
                if arr[j] == "NORTH":
                    arr[i] = ""
                    arr[j] = ""
                    break
        if arr[i] == "WEST":
            for j in range(i+1,len(arr)-1):
                if arr[j] == "EAST":
                    arr[i] = ""
                    arr[j] = ""
                    break
        if arr[i] == "EAST":
            for j in range(i+1,len(arr)-1):
                if arr[j] == "WEST":
                    arr[i] = ""
                    arr[j] = ""
                    break
        
        _return = []
        for i in arr:
            if i !="":
                _return.append(i)

    return  _return

print (dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]))