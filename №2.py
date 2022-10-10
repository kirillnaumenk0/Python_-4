# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# in
# 54

# out
# [2, 3, 3, 3]

# in
# 9990

# out
# [2, 3, 3, 3, 5, 37]


def simple_multiplier(num: int):
    new_list = []
    i = 2
    while(num !=1):
        if(num % i==0):
            new_list.append(i)
            num/=i
        else:
            i+=1
    return new_list
    

    

num = int(input('Введите натуральное чило: '))
if(num < 2):
    print('Ошибка')
else:
    print(simple_multiplier(num))