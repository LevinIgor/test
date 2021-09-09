# 
    # _sum_intervals = 0
    # _list2 = copy.copy(intervals)
    
    # for i in range(len(intervals)):
    #     for j  in range(i+1,len(intervals)):
    #         if intervals[i][1] > intervals[j][0] and intervals[i][0] < intervals[j][1]:
    #            _list2.append((intervals[i][0],intervals[j][1]))
    #            _list2.pop(j)
    #            _list2.pop(i)
    # for i in _list2:
    #     _sum_intervals+=i[1]-i[0]
    # return _sum_intervals
 

def sum_of_intervals(intervals):
    a=[i for lists in intervals for i in range(int(lists[0]),int(lists[1]))]
    return len(set(a))

print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))
# print(sum_of_intervals([(1, 4), (3, 5),(4,9), (6,12)]))