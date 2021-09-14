
def sum_of_intervals(intervals):
    a=[i for lists in intervals for i in range(int(lists[0]),int(lists[1]))]
    return len(set(a))

print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))
# print(sum_of_intervals([(1, 4), (3, 5),(4,9), (6,12)]))