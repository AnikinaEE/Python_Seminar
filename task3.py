# Задача №3
# В некоторой школе решили набрать три новых математических класса
# и оборудовать кабинеты для них новыми партами. За каждой партой 
# может сидеть два учащихся. Известно количество учащихся в каждом
# из трех классов. Выведите наименьшее число парт, которое нужно 
# приобрести для них.
# Input: 22 21 22 (ввод чисел не в одну строку)
# Output: 32

first_class = 20
second_class = 21
third_class = 22
print((first_class+1) // 2 +
      (second_class+1) // 2 +
      (third_class+1) // 2)
