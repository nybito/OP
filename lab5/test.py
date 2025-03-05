import pytest
from prime_utils import is_prime, generate_primes, sum_primes

def test_is_prime():
    # Проверка на простые числа
    assert is_prime(2) == True  # 2 - простое число
    assert is_prime(3) == True  # 3 - простое число
    assert is_prime(4) == False  # 4 - не простое
    assert is_prime(5) == True  # 5 - простое
    assert is_prime(16) == False  # 16 - не простое
    assert is_prime(17) == True  # 17 - простое
    assert is_prime(1) == False  # 1 - не простое
    assert is_prime(0) == False  # 0 - не простое
    assert is_prime(-5) == False  # Отрицательные числа не считаются простыми

def test_generate_primes():
    # Тестирование генерации простых чисел
    assert generate_primes(10) == [2, 3, 5, 7]  # Простые числа до 10
    assert generate_primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]  # Простые числа до 20
    assert generate_primes(2) == []  # Ни одно простое число до 2
    assert generate_primes(1) == []  # Ни одно простое число до 1
    assert generate_primes(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]  # Примеры для 50

def test_sum_primes():
    # Тестирование суммы простых чисел
    assert sum_primes(10) == 17  # Сумма простых чисел до 10 (2 + 3 + 5 + 7)
    assert sum_primes(20) == 77  # Сумма простых чисел до 20
    assert sum_primes(1) == 0  # Сумма простых чисел до 1 должна быть 0
    assert sum_primes(2) == 0  # Сумма простых чисел до 2 должна быть 0
    assert sum_primes(50) == 328  # Сумма простых чисел до 50
