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
