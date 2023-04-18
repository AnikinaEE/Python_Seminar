# Задача №23
# Дан массив, сосоящий из целых чисел. Напишите
# программу, которая подсчитает количество элементов
# массива, больших предыдущего (элемента с предыдущим
# номером)

nums = [1, 2, 3, 1, 2]
count = 0
for i in range(1, len(nums)):
    if nums[i-1] < nums[i]:
        count += 1
print(count)

# 2
result = [nums[i] for i in range(1, len(nums))
          if nums[i-1] < nums[i]]
print(len(result))
