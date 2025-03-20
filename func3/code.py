# Код суммирует длину имен из заданного списка после удаления тех, которые
# начинаются со строчной буквы

# Пример использования функции
# Ввод:
# ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']
# Вывод:
# 16

def show_letter_sum(lst: [str]):
    # lst = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']
    letter_sum = sum(len(el) for el in (filter(lambda x: x[0].isupper(), lst)))
    return letter_sum
