# Задача №5
# Вагоны в электричке пронумерованы натуральными числами, начиная с 1
# (при этом иногда вагоны нумеруются от "головы" поезда, а иногда - с "хвоста";
# это зависит от того, в какую сторону едет электричка). В каждом вагоне
# написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон номер j.
# Он хочет определить, сколько всего вагонов в электричке.
# Напишите программу, которая определит число вагонов или выведет сообщение,
# что без доп информации это сделать не возможно.
# Input: 3 - 4 (на разных строках)
# Output: 6

print("Введите номер вагона, который обнаружил Витя: ")
vitya_num = int(input())
print("Введите фактический номер вагона электрички: ")
train_num = int(input())

if vitya_num == train_num:
    print("Без доп инфо определить количество вагонов электрички НЕ возможно!")
else:
    print(vitya_num + train_num - 1)
