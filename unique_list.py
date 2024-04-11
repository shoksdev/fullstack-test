def get_unique_list(not_unique_list):
    """Получение списка уникальных чисел"""

    return list(set(not_unique_list))


def create_list(num):
    """Создание списка из чисел из консоли"""

    new_list = []
    for i in range(num):
        num_for_list = int(input('Введите целое число для списка: '))
        new_list.append(num_for_list)

    return new_list


list_len = int(input('Введите длину списка: '))
if list_len <= 0:
    print('Длина списка должна быть больше 0')
else:
    input_list = create_list(list_len)
    result = get_unique_list(input_list)
    print(f'Список уникальных чисел: {result}')
