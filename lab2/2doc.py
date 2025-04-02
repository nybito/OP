def calculate_binary_and_count_ones():
    """
    Вычисляет значение a = 8**2020 + 4**2017 + 26 - 1,
    преобразует его в двоичную строку и считает количество единиц.

    :return: Кортеж (двоичная строка, количество единиц)

    >>> calculate_binary_and_count_ones()
    ('...двоичное представление...', ...количество единиц...)
    """
    
    a = 8**2020 + 4**2017 + 26 - 1
    b = bin(a)[2:]  # Преобразуем в двоичную строку без префикса '0b'
    count_of_ones = b.count("1")  # Считаем количество единиц
    return b, count_of_ones

if __name__ == "__main__":
    import doctest
    doctest.testmod()
