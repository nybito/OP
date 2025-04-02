import itertools

def generate_strings(s):
    """
    Генерирует все возможные строки длиной 6 из символов строки s,
    соблюдая определенные условия.

    Условия:
    - Не более одной буквы 'й'
    - Первая и последняя буквы не могут быть 'й'
    - Не должно быть подстрок 'ей' и 'йе'

    :param s: Исходная строка
    :return: Список строк, соответствующих условиям

    >>> generate_strings("Андрей")
    ['АндреА', 'АндреА', 'АндреА', ...]  # Здесь будет много строк
    """
    
    result = []
    for x in itertools.product(s, repeat=6):
        a = "".join(x)
        if (a.count("й") <= 1 and 
            a[0] != "й" and 
            a[5] != "й" and 
            a.count("ей") == 0 and 
            a.count("йе") == 0):
            result.append(a)
    
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()
