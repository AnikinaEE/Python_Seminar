# Задача №17
# Дан список чисел. Необходимо определить,
# сколько в нем встречается различных чисел.

nums = [1, 2, 3, 4, 1, 2, 3]
# set - пребразует список в множество
# (список уникальных элементов, неповторящихся)
print(len(set(nums)))

# 2
result = []
for i in set(nums):
    if nums.count(i) == 1:
        result.append(i)
print(result, len(result))

# 3
result_1 = [i for i in set(nums) if nums.count(i) == 1]
print(result_1)
