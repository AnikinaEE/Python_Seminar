# Задача №33
# Хакер Василий получил доступ к классному журналу и
# хочет заменить свои минимальные оценки на максимальные.
# Напишите программу, которая заменит все оценки Василия,
# но наоборот: все максимальные - на минимальные.

# [1, 2, 3, 1, 2, 1, 5, 4, 5]
# -> [1, 2, 3, 1, 2, 1, 1, 4, 1]

def marks(a):
    min = a[0]
    max = a[0]
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
        elif a[i] < min:
            min = a[i]
    for j in range(len(a)):
        if a[j] == max:
            a[j] = min
    return a


line_marks = []
num = int(input('Введите количество оценок в журнале: '))
for i in range(num):
    line_marks.append(int(input()))
print(marks(line_marks))
