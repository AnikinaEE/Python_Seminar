# Задача №7
# Дано натуральное число. Требуется определить, является ли год
# високосным. Если год является високосным, то вывести YES,
# иначе вывести NO.
# Напоминание: в соотвествии с григорианским календарем, год
# является високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.
# Input: 2016
# Output: YES

print("Введите год: ")
year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("YES")
else:
    print("NO")
