# Задача №25
# Напишите программу, которая принмает на вход строку,
# и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью
# формата _n.

main_str = 'a a a b c a a d c d d'
new_list = main_str.split()
dict = {}
for i in new_list:
    if i in dict:
        dict[i] += 1
        print(f'{i}_{dict[i]}', end=' ')
    else:
        dict[i] = 0
        print(i, end=' ')
