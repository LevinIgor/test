from typing import Counter


def score(dice):
    _score = 0

    if dice.count(1) == 3: _score+=1000
    if dice.count(6) == 3: _score+=600
    if dice.count(5) == 3: _score+=500
    if dice.count(4) == 3: _score+=400
    if dice.count(3) == 3: _score+=300
    if dice.count(3) == 4: _score+=300
    if dice.count(3) == 4: _score+=300
    if dice.count(2) == 3: _score+=200
    if dice.count(1) == 1: _score+=100
    if dice.count(1) == 2: _score+=200
    if dice.count(1) == 4: _score+=1100
    if dice.count(1) == 5: _score+=1200
    if dice.count(5) == 1: _score+=50
    if dice.count(5) == 2: _score+=100
    if dice.count(5) == 4: _score+=550
    if dice.count(5) == 5: _score+=600

    return _score


print(score([3,3, 2, 3,3]))


#  Three 1's => 1000 points
#  Three 6's =>  600 points
#  Three 5's =>  500 points
#  Three 4's =>  400 points
#  Three 3's =>  300 points
#  Three 2's =>  200 points
#  One   1   =>  100 points
#  One   5   =>   50 point
