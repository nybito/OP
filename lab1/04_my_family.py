#!/usr/bin/env python3
# -*- coding: utf-8 -*-

my_family = ['Отец', 'Мать', 'Сын', 'Дедушка', 'Бабушка']

# список списков приблизительного роста членов вашей семьи
my_family_height = [
    ['Отец', 190],
    ['Мать', 165],
    ['Сын', 170],
    ['Дедушка', 175],
    ['Бабушка', 160],
]

# Выведите на консоль рост отца в формате
father_height = next(height for name, height in my_family_height if name == 'Отец')
print(f'Рост отца - {father_height} см')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
total_height = sum(height for name, height in my_family_height)
print(f'Общий рост моей семьи - {total_height} см')
