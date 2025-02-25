# Код для поиска списка с максимальной и минимальной длиной.

# Пример использования кода
# Ввод:
# [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# Вывод:
# Список с максимальной длиной:
# (3, [13, 15, 17])
#
# Список с минимальной длиной:
# (1, [0])


def find_max_and_min_list(lst: list):
    max_result = (max_len := max(len(x) for x in lst),) + tuple(filter(lambda y: len(y) == max_len, lst), )
    min_result = (min_len := min(len(x) for x in lst),) + tuple(filter(lambda y: len(y) == min_len, lst), )
    return f'Список с максимальной длиной:\n{max_result}\n\nСписок с минимальной длиной:\n{min_result}'
