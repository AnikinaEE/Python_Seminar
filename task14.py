# Задача №14
# Необходимо вывести все целые степени двойки (т.е. числа вида
# 2 в степени k), не превосходящие числа N.

number = int(input('Введите натуральное число N: '))
degree = 0
list = []
res = 2**degree
while res < number:
    list.append(res)
    degree += 1
    res = 2**degree
print(*list)
