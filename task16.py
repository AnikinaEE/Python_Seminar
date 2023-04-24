# Задача №16
# Требуется вычислить, сколько раз встречается
# некоторое число Х в массиве А[1...N].
# Пользователь в первой строке вводит натуральное
# число N - количество элементов массива.
# В последующих строках записаны N целых чисел
# массива А, последняя строка содержит число Х

# 5
# 1 2 3 4 5
# 3
# -> 1

num = int(input('Введите количество элементов массива: '))

# Заполним и выведем полученный список
list = [int(input()) for i in range(num)]
print(*list)

count = 0
number_x = int(input('Введите искомое число Х: '))
for i in range(num):
    if list[i] == number_x:
        count += 1
print(f'Число {number_x} встречается в массиве {count} раз(а)')