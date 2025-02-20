# Условие:
Функция для распаковки списка, содержащего другие объекты (int, str, list, tuple, dict, set) произвольной вложенности.

# Описание проделанной работы:
```Python
#РЕКУРСИЯ
def unpack_recursive(lst):
    result = [] // Создается список result, в который будут добавляться значения, во время обработки.
    if isinstance(lst, (list, tuple, set)): // Проверка, переданое в функию являетя списоком, кортежем или множеством?
        for item in lst:
            result.extend(unpack_recursive(item)) // Если да, то с помощью метода extend, все находящееся внутри запихивается в result. Находящееся внутри, также отправляет в функцию.
    elif isinstance(lst, dict): // Если переданное вляет словарем, то в result добавляется значения ключей и значений.
        for key, value in lst.items():
            result.append(key)
            result.append(value) 
    else: // Если переданное не является всем выше перечисленным, значит это базовый тип и его можно спокойно добавлять в result.
        result.append(lst)
    return result // Возвращение ответа.
    
# Не рекурсия
def unpack_iterative(lst):
    result = []
    stack = lst.copy()  // Создание копии переданного в функцию
    while stack:
        item = stack.pop()  // С помощью метода pop() беру последнее значение.
        if isinstance(item, (list, tuple, set)):// Проверка, переданое в функию являетя списоком, кортежем или множеством?
            stack.extend(item)// Если да, то с помощью метода extend, все находящееся внутри запихивается в result.
        elif isinstance(item, dict):// Если переданное вляет словарем, то в result добавляется значения ключей и значений.
            stack.extend(item.keys())
            stack.extend(item.values())
        else:// Если переданное не является всем выше перечисленным, значит это базовый тип и его можно спокойно добавлять в result.
            result.append(item)
    return result[::-1]  // Возвращение ответа.(в обратном порядке, так как мы использовали метод pop())

nested_list = [None, [1, ({2, 3},[1,2,3], {'foo': 'bar'})]] // Что мы передаем в функцию

# Рекурсивный подход
result_recursive = unpack_recursive(nested_list)
print(result_recursive)

# Итеративный подход
result_iterative = unpack_iterative(nested_list)
print(result_iterative)

#РЕКУРСИЯ
def func_recursion(i):
    if i == 2: // По условию, мы знаем значения при i = 1 и i = 2.
        return -1.5
    if i == 1:
        return 0.3
    return (func_recursion(i-1) * func_recursion(i-2) * ((i - 1)**2/(i+1)**3))// Расчет при помощью рекурсии.
print(func_recursion(100)) 
#ИТЕРАТИВНЫЙ
def func_iter(i):
    if i == 1:
        return 0.3
    if i == 2:
        return -1.5 // По условию мы знаем значения при i = 1 и i = 2.
    w = [0] * (i+1) // Создаем список, для запоминания всез полученых значений.
    w[1] = 0.3
    w[2] = -1.5
    for n in range(3,i+1): // Цикл, в котором мы будем считать все значения от 3 и до заданого.
        w[n] = (w[n-1] * w[n-2] * ((n-1)**2/(n+1)**3))
    return(w[i]) // Возвращаем расчет для переданого в функцию i.
print(func_iter(10))
```

# Скриншот результатов: 
![изображение](https://github.com/user-attachments/assets/238f0aa4-0a1a-4513-89e0-879b09805c2e)


# Используемые материалы:

1. [Списки (list). Функции и методы списков](https://pythonworld.ru/tipy-dannyx-v-python/spiski-list-funkcii-i-metody-spiskov.html)
2. [Списки, кортежи и словари](https://metanit.com/python/tutorial/3.1.php)
3. [Как работает рекурсия](https://vertex-academy.com/tutorials/ru/git-osnovy-dlya-nachinayuschih/)
