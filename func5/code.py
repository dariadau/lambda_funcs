# Код для поиска всех анаграмм заданной строки в списке строк.

# Пример использования функции
# Ввод:
# ['bcda', 'abce', 'cbda', 'cbea', 'adcb'] (Исходный список)
# abcd (Заданная строка)

# Вывод:
# ['bcda', 'cbda', 'adcb'] (Аннограммы для строки abcd)

def find_anagrams(a: list, s: str):
    

    for ltr in s:
        result = list(filter(lambda x: ltr in x, a))

    return result
# расписать и вывести на экран (как сократить)
