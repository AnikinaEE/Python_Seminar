# Задача №31
# Последовательностью Фибоначчи называется последовательность
# чисел а0, а1, ..., an, где а0=0, а1=1, ak=ak-1 + ak-2
# (k>1). Требуется найти N-е число Фибоначчи

def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)


num = int(input())
print(fib(num))
