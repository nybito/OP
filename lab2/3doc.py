def find_primes_in_range(start, end):
    """
    Находит все простые числа в заданном диапазоне [start, end).

    :param start: Начало диапазона (включительно)
    :param end: Конец диапазона (исключительно)
    :return: Список простых чисел в заданном диапазоне

    >>> find_primes_in_range(245690, 245700)
    [245693]
    >>> find_primes_in_range(245700, 245756)
    [245701, 245711, 245717, 245723, 245729, 245733, 245747]
    """
    
    primes = []
    for x in range(start, end):
        c = 0
        for y in range(2, int(math.sqrt(x)) + 1):  # Оптимизация: проверяем до корня из x
            if x % y == 0:
                c += 1
                break  # Если нашли делитель, выходим из цикла
        if c == 0 and x > 1:  # Учитываем только числа больше 1
            primes.append(x)
    
    return primes

if __name__ == "__main__":
    import doctest
    doctest.testmod()
