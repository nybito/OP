import math
z = 1
for x in range(245690,245756):
    c = 0
    for y in range(2,math.isqrt(x)):
        if x%y == 0:
            c+=1
    z+=1
    if c == 0:
        print(z, x)
       
