import copy
def done_or_not(board):

    _exLine = [1,2,3,4,5,6,7,8,9]
    
    for i in range(9):
        _line = copy.copy(board[i])
        _line.sort()
        
        if _line != _exLine:
            return "Try again!"

    for i in range(9):
        _line = []
        for j in range(9):
            _line.append(board[j][i])
        _line.sort()

        if _line != _exLine:
            return "Try again!"

        # 1,1 1,2 1,3     1,4 1,5 1,6

        # 2,1 2,2 2,3     2,4 2,5 2,6

        # 3,1 3,2 3,3     3,4 3,5 3,6
   
    _iterI = -3
    _iterJ = -3
    _list = []
    while _iterI <=5:
        _iterI+=3
        _iterJ+=3
        _list = []
        for i in range(3):
            for j in range(3):
                _list.append(board[i+_iterI][j+_iterJ])
        _list.sort()
        if _list != _exLine:
            return "Try again"


        
    
    return "Finished"

print(done_or_not([      [1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]))