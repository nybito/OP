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
