# from arepl_dump import dump

    # def sum_of_intervals(intervals):
    #     result = set()
    #     for start, stop in intervals:
    #         for x in range(start, stop):
    #             result.add(x)
                
    #     return len(result)


# def sum_of_intervals(intervals): 
#     s = []
#     for i in intervals:
#         s += list(range(i[0],i[1]))
#     return len(set(s))

def sum_of_intervals(a):
        a = sorted(a)
        r, last = 0, a[0][0]
        for x, y in a:
            if y <= last: continue
            m = max(x, last)
            r += y - m
            last = y
        return r

# def sum_of_intervals(intervals):
#     intervals.sort()
#     res=0
#     x,y=intervals[0]
#     for s,e in intervals:
#         if s<=y: 
#             y=max(y,e)
#         else:
#             res+=y-x
#             x,y=s,e
#     return res+y-x



# def sum_of_intervals(intervals):
#     a=[i for lists in intervals for i in range(int(lists[0]),int(lists[1]))]
#     return len(set(a))

print(sum_of_intervals([(1, 4), (7, 10), (3, 8)]))
print(sum_of_intervals([(1, 4), (3, 5),(4,9), (6,12)]))