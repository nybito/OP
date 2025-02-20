#РЕКУРСИЯ
def unpack_recursive(lst):
    result = []
    if isinstance(lst, (list, tuple, set)):
        for item in lst:
            result.extend(unpack_recursive(item))  # Рекурсивно обрабатываем вложенные элементы
    elif isinstance(lst, dict):
        for key, value in lst.items():
            result.append(key)  # Добавляем ключи
            result.append(value)  # Добавляем значения
    else:
        result.append(lst)  # Добавляем одиночный элемент
    return result
    
# Не рекурсия
def unpack_iterative(lst):
    result = []
    stack = lst.copy()  # создаем копию списка для обработки
    while stack:
        item = stack.pop()  # берём последний элемент из стека
        if isinstance(item, (list, tuple, set)):
            # если это структура, добавляем её элементы в стек
            stack.extend(item)
        elif isinstance(item, dict):
            # если это словарь, добавляем ключи и значения
            stack.extend(item.keys())
            stack.extend(item.values())
        else:
            # если это базовый тип, добавляем его в результат
            result.append(item)
    return result[::-1]  # возвращаем результат в правильном порядке

nested_list = [None, [1, ({2, 3}, {'foo': 'bar'})]]

# Рекурсивный подход
result_recursive = unpack_recursive(nested_list)
print(result_recursive)

# Итеративный подход
result_iterative = unpack_iterative(nested_list)
print(result_iterative)

def func_recursion(i):
    if i == 2:
        return -1.5
    if i == 1:
        return 0.3
    return (func_recursion(i-1) * func_recursion(i-2) * ((i - 1)**2/(i+1)**3))
print(func_recursion(100))

def func_iter(i):
    if i == 1:
        return 0.3
    if i == 2:
        return -1.5
    w = [0] * (i+1)
    w[1] = 0.3
    w[2] = -1.5
    for n in range(3,i+1):
        w[n] = (w[n-1] * w[n-2] * ((n-1)**2/(n+1)**3))
    return(w[i])
print(func_iter(10))
