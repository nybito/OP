# 1 Задание:
Андрей составляет 6-буквенные коды из букв А, Н, Д, Р, Е, Й. Буква Й может использоваться в коде не более одного раза, при этом она не может стоять на первом месте, на последнем месте и рядом с буквой Е. Все остальные буквы могут встречаться произвольное количество раз или не встречаться совсем. Сколько различных кодов может составить Андрей?
```Python
import itertools
s = "Андрей"
c = 0
for x in itertools.product(s, repeat=6):
    a = "".join(x)
    if a.count("й")<=1 and a[0] != "й" and a[5] != "й" and a.count("ей") == 0 and a.count("йе") == 0:
        print(a)
        c+=1
print(c)  
```
С помощью подсчета проверяем правильность полученных кодов.
Скрин: ![image](https://github.com/user-attachments/assets/c5db46e9-7cbb-466a-8a7a-4154698f2c95)

# 2 Задание:
Сколько единиц содержится в двоичной записи значения выражения.
```Python
a = 8**2020 + 4**2017 + 26 - 1
b = bin(a)[2:]
print(b)
print(b.count("1"))
```
Скрин: ![image](https://github.com/user-attachments/assets/a4e7e483-da22-4185-9c9c-11a743750ac4)

# 3 Задание:
Найти простые числа в числовом отрезке.
```Python
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
```
Во 2 цикле for идем от 2 до корня числа.
Скрин: ![image](https://github.com/user-attachments/assets/711e834c-ce16-4cc0-bde9-af4ca545b7e8)

