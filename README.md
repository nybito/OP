# OP
# 1 ЗАДАНИЕ 
Вычислить расстояние между 3 городами с помощью данной в задании формуле.
## Решение: 
```Python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}
distances = {}
def calculate_distance(coord1, coord2):
    return ((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2) ** 0.5

for city1, coord1 in sites.items():
    distances[city1] = {}
    for city2, coord2 in sites.items():
        if city1 != city2:  
            distance = calculate_distance(coord1, coord2)
            distances[city1][city2] = distance

print(distances)
```
## Объяснение: 
C помощью отдельной функции вычисляем расстояние между городами так, чтобы не высчитывалось расстояние между одинаковыми городами, после чего это расстояние заносится в список. После всего этого список выводится.
## Скриншот: ![image](https://github.com/user-attachments/assets/0c5f282c-3974-45f0-b754-5c64a320b944)


# 2 ЗАДАНИЕ 
Находиться ли точка в площади окружности.
## Решение: 
Вычисляем площадь круга с помощью данного кода и выводим с тончость до 4 знака после запятой.
```Python
pi = 3.1415926
area = pi * (radius ** 2)
print(round(area, 4))
```

Определяем рассттояние от точки, до начала координат и проверяем, находиться ли точка в радиусе круга.
```Python
distance_1 = (point_1[0] ** 2 + point_1[1] ** 2) ** 0.5
is_inside_1 = distance_1 <= radius
print(is_inside_1)
```
## Скриншот: ![image](https://github.com/user-attachments/assets/4992624c-cfd7-47b4-a013-7b8e05c924b2)

# 3 ЗАДАНИЕ 
Расставить знаки +, -, * и скобки в выражении 1 ? 2 ? 3 ? 4 ? 5, так чтобы получилось 25.
## Решение: 
Методом тыка получаем следующее выражение:
```Python
result = ((1 + 2)* 3 - 4) * 5
print(result)
```
## Скриншот: ![image](https://github.com/user-attachments/assets/d2256e78-00b9-47b5-9b3c-077c336e7455)
