# Задача №6
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались
# за проезд и получали билет с номером.
# Счатливым билетом называется такой билет с шестизначным номером, где
# сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 - счастливый, т.к. 3+8+5 = 9+1+6.
# Необходимо написать программу, которая проверяет счастливость билета.

print("Ведите шестизначный номер билета:")
num = int(input())
sum_left = 0
sum_right = 0

if num < 99999 or num > 1000000:
    print("Вы ввели неверный номер билета! Введите заново")
else:
    for i in range(6):
        if i < 3:
            sum_right = sum_right + num // 10**i % 10
        else:
            sum_left = sum_left + num // 10**i % 10
    if sum_left == sum_right:
        print("Этот билет СЧАСТЛИВЫЙ")
    else:
        print("Увы... Это НЕСЧАСТЛИВЫЙ билет")
