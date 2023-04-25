# Задача №35
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым.
# (Простое число - это число, которое имеет 2 делителя:
# 1 и n-само число)

def divider(n, div=2):
    if div == n//2 + 1:
        return True
    if n % div == 0:
        return False
    return divider(n, div+1)


num = int(input())
print(divider(num))
