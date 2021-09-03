def namelist(names):
    returnStr = ""
    if len(names)==0:
        return ""
    if len(names) == 1:
        return names[0]['name']
    if len(names) == 2:
        return names[0]['name'] + " & " + names[1]['name']
    if len(names)>2:
        lastNames = names[len(names)-2]['name'] + " & " + names[len(names)-1]['name']
    names = names[0:len(names)-2]
    for n in names:
        returnStr+=n['name']+", "
    returnStr+=lastNames
    return returnStr


names1 = [{'name':'bob'}]
names2 = [{'name':'dayn'},{'name':'Nix'}]
names3 = [{'name':"Ihor"}, {'name':"Yury"}, {'name':"Denis"}, {'name':"Nikita"},{'name':'Jon'}]
print(namelist(names3))