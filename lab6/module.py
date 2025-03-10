import math

def Shar(r):
    V = (4/3)* math.pi * r**3
    P = 4 * math.pi * r**2
    return [V,P]

def Para(a,b,h):
    V = a * b * h
    P = 2 * (a * b + a * h + b * h)
    return [V,P]

def Tetra(a):
    V = (round(math.sqrt(2)/12,2))* a **3
    P = round(math.sqrt(3),2)* a **2
    return [V,P]


