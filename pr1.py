import random

_p = [0.80,0.75,0.85,0.90,0.95]
_r = []
_yes = 0





for k in range(1000):
    _r = []
    for i in range(len(_p)):
      _r.append((random.randrange(0,100))/100) 

    if((_r[0]>_p[0]) | (_r[1] > _p[1])) & (_r[2]>0) & ((_r[3]>_p[3]) & (_r[4]>_p[4])):
       _yes+=1


print("------- " + str(_yes/1000))


# Pa = 1 - (1-p1)*(1-p2)
# Pb = p3
# Pc = 1 - (1-p4)*(1-p5)

# print(Pa*Pb*Pc)