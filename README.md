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

# 4 ЗАДАНИЕ 
Выведите на консоль с помощью индексации строки, последовательно:
первый фильм
последний
второй 
второй с конца
## Решение: 
Используя срезы получаем следующее:
```Python
my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
print(my_favorite_movies[:10])  # 'Терминатор' Первый фильм
print(my_favorite_movies[-15:]) # 'Назад в будущее' Последний Фильм
print(my_favorite_movies[12:25])   # 'Пятый элемент' Второй Фильм
print(my_favorite_movies[-22:-17]) # 'Чужие' Второй с конца
```
## Скриншот: ![image](https://github.com/user-attachments/assets/3c766a73-fe67-483d-9bdb-4d1c38b52f89)

# 5 ЗАДАНИЕ 
Выведите на консоль рост отца в формате. Выведите на консоль общий рост вашей семьи как сумму ростов всех членов.
## Решение: 
Используя работу со списками получаем следующее:
```Python
my_family_height = [
    ['Отец', 190],
    ['Мать', 165],
    ['Сын', 170],
    ['Дедушка', 175],
    ['Бабушка', 160],
]
father_height = next(height for name, height in my_family_height if name == 'Отец')
print(f'Рост отца - {father_height} см')
total_height = sum(height for name, height in my_family_height)
print(f'Общий рост моей семьи - {total_height} см')
```
## Скриншот: ![image](https://github.com/user-attachments/assets/89a84fe0-66cc-4d5e-919d-57b2c4793ca4)

# 6 ЗАДАНИЕ 
Удаление, добавление, изменение списков.
## Решение: 
Используя методы списков получаем следующее:
```Python
zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
zoo.insert(1, 'bear')
print(zoo)
birds = ['rooster', 'ostrich', 'lark']
zoo.extend(birds)
print(zoo)
zoo.remove('elephant')
print(zoo)
lion_index = zoo.index('lion') + 1 
lark_index = zoo.index('lark') + 1 
print(f'Лев сидит в клетке {lion_index}, жаворонок сидит в клетке {lark_index}.')
```
## Скриншот: ![image](https://github.com/user-attachments/assets/06b168c5-dc8c-47f3-bfda-b37d9050edac)

# 7 ЗАДАНИЕ 
Посчитать продолжительность треков, до 2 знаков после запятой.
## Решение: 
Используя методы списков получаем следующее:
```Python
violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]
time_halo = next(song[1] for song in violator_songs_list if song[0] == 'Halo')
time_enjoy = next(song[1] for song in violator_songs_list if song[0] == 'Enjoy the Silence')
time_clean = next(song[1] for song in violator_songs_list if song[0] == 'Clean')
total_time_list = round(time_halo + time_enjoy + time_clean, 2)
print(f'Три песни звучат {total_time_list} минут')
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}
time_sweetest = violator_songs_dict['Sweetest Perfection']
time_policy = violator_songs_dict['Policy of Truth']
time_blue = violator_songs_dict['Blue Dress']
total_time_dict = round(time_sweetest + time_policy + time_blue, 2)
print(f'А другие три песни звучат {total_time_dict} минут')
```
## Скриншот: ![image](https://github.com/user-attachments/assets/ee55c3e0-82d8-408e-96f8-66067e87f119)

# 8 ЗАДАНИЕ 
Расшифровать сообщение
## Решение: 
Используя срезы и работу со списками получаем следующее:
```Python
secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
]
first_word = secret_message[0][3]  
second_word = secret_message[1][9:13]  
third_word = secret_message[2][5:15:2]  
fourth_word = secret_message[3][7:13][::-1]  
fifth_word = secret_message[4][16:21][::-1]  

decoded_message = f"{first_word} {second_word} {third_word} {fourth_word} {fifth_word}"
print(decoded_message)
```
## Скриншот:![image](https://github.com/user-attachments/assets/9b91482f-c0e4-45db-8633-c5417d9b73f2)

# 9 ЗАДАНИЕ 
Расставить знаки +, -, * и скобки в выражении 1 ? 2 ? 3 ? 4 ? 5, так чтобы получилось 25.
## Решение: 
Методом тыка получаем следующее выражение:
```Python
result = ((1 + 2)* 3 - 4) * 5
print(result)
```
## Скриншот: ![image](https://github.com/user-attachments/assets/d2256e78-00b9-47b5-9b3c-077c336e7455)





