import itertools
s = "Андрей"
c = 0
for x in itertools.product(s, repeat=6):
    a = "".join(x)
    if a.count("й")<=1 and a[0] != "й" and a[5] != "й" and a.count("ей") == 0 and a.count("йе") == 0:
        print(a)
        c+=1
print(c)  
