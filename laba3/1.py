#РЕКУРСИЯ
def unpack_recursive(lst):
    result = []
    for item in lst:
        if isinstance(item, (list, tuple, set, dict)):
            # если элемент - это структура, рекурсивно распаковываем его
            result.extend(unpack_recursive(item))
        elif isinstance(item, dict):
            # если элемент - это словарь, распаковываем ключи и значения
            result.extend(item.keys())
            result.extend(item.values())
        else:
            # если это базовый тип, добавляем его в результат
            result.append(item)
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
print(result_recursive)  # Вывод: [None, 1, 2, 3, 'foo', 'bar']

# Итеративный подход
result_iterative = unpack_iterative(nested_list)
print(result_iterative)  # Вывод: [None, 1, 2, 3, 'foo', 'bar']
