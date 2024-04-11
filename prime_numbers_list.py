def is_prime(num):
    """Вычисление число является простым или нет"""

    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def get_prime_numbers_list(minimum, maximum):
    """Создание списка простых чисел"""

    prime_numbers_list = []

    for num in range(minimum, maximum + 1):
        if is_prime(num):
            prime_numbers_list.append(num)

    return prime_numbers_list


range_start = int(input('Введите минимальное число диапазона: '))
range_finish = int(input('Введите максимальное число диапазона: '))
if range_finish > range_start:
    print('Второе число должно быть больше первого!')
else:
    result = get_prime_numbers_list(range_start, range_finish)
    print(f'Список простых чисел в диапазоне от {range_start} до {range_finish}: {result}')
