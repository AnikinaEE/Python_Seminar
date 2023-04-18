# Задача №21
# Напишите программу для печати всех уникальных
# значений в словаре

# dict = {1: 3, 2: 5}
# # получение значения
# print(dict.values())
# # получение списка значений
# print(list(dict.values()))

list_of_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
                {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
                {"VIII": "S007"}]

# # 1
uniq_el = set()
# for i in list_of_dict:
#     element = list(i.values())[0]
#     print(element)
#     uniq_el.add(element)
# print(uniq_el)

# 2
for i in list_of_dict:
    for key in i:
        element = i[key]
        uniq_el.add(element)
print(uniq_el)

# 3
uniq_el1 = set(list(i.values())[0] for i in list_of_dict)
print(uniq_el1)
