# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

from random import randint

list_numbers = []
def fill_list(list_numbers: int):
    for i in range(randint(5, 10)):
        list_numbers.append(randint(1,10))
    return list_numbers


def exception(list_numbers: list):
    new_list = []
    list_len = {}.fromkeys(list_numbers, 0)

    for i in list_numbers:
        list_len[i] += 1

    for k in list_len:
        if list_len[k] == 1:
            new_list.append(k)

    return new_list

fill_list(list_numbers)
print(list_numbers)
print(exception(list_numbers))

# fromkeys для меня был неизведан, теперь все понятно
