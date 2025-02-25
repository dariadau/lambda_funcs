# Код для поиска чисел в заданной строке. Затем отобразите в отсортированном виде только те числа числа,
# значения которых превышает длину списка. Используйте lambda функцию.

# Пример использования функции
# Ввод:
# sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5
# Вывод:
# 20 23 56

def find_num(s: str):
    max_len = len(max(s.split()))
    num_chk = sorted(filter(lambda x: x.isdigit() and int(x) > max_len, s.split()))
    return ' '.join(num_chk)
