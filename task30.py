# Задача №30
# Заполните массив элементами арифметической прогрессии.
# Её первый элемент(a1), разность(d) и количество элементов(n)
# нужно ввести с клавиатуры. Формула для получения n-го члена
# прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_a1 = int(input('Введите первый элемент прогрессии: '))
difference_d = int(input('Введите разность: '))
quantity_k = int(input('Введите количество элементов: '))
list = []
for n in range(1, quantity_k + 1):
    list.append(first_a1 + difference_d*(n - 1))
print(list)
