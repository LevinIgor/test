def number(bus_stops):
    total = 0

    for i in bus_stops:
        total += i[0]
        total -=i[1]

    return total





print(number([[10,0],[3,5],[5,8]]))