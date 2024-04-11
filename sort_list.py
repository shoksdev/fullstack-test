def sort_list_by_len(list_for_sort):
    """Сортировка списка по возрастанию и убыванию длины слов внутри"""

    sort_by_len = sorted(list_for_sort, key=len)
    sort_by_len_revers = sorted(list_for_sort, key=len, reverse=True)

    return sort_by_len, sort_by_len_revers


def create_list(num):
    """Генерация списка из консоли"""

    new_list = []
    for i in range(num):
        str_for_list = input('Введите слово для списка: ')
        new_list.append(str_for_list)

    return new_list


list_len = int(input('Введите длину списка: '))
if list_len <= 0:
    print('Длина списка должна быть больше 0')
else:
    input_list = create_list(list_len)
    sorted_list_by_len, sorted_list_by_len_reverse = sort_list_by_len(input_list)

    print(f'Отсортированный список по возрастанию: {sorted_list_by_len}')
    print(f'Отсортированный список по убыванию: {sorted_list_by_len_reverse}')
