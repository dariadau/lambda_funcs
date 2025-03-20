# Код для поиска чисел в заданной строке только те числа числа,
# значения которых превышает длину списка.

# Пример использования функции
# Ввод:
# sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5
# Вывод:
# 20 23 56

def find_num(s: str):
    max_len = len(max(filter(lambda x: x.isdigit(), s.split())))
    num_chk = sorted(filter(lambda x: int(x) > max_len, s.split()))
    return ' '.join(num_chk)
