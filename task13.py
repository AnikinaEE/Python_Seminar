# Задача №13
# Уставшие от необычно теплой зимы жители решили узнать,
# действительно ли это самая длинная оттепель за всю
# историю наблюдений за погодой. Они обратились к
# синоптикам, а те, в свою очередь, занялись исследованиями
# статистики за прошлые годы. Их интересует, сколько
# дней длилась самая длинная оттепель. Оттепелью они
# называют период, в который среднесуточная температура
# ежедневно превышала 0 градусов Цельсия.
# Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N - общее количество
# рассматриваемых дней (1 <= N <= 100). В следующих строках
# располагается N целых чисел. Каждое число - среднесуточная
# температура в соответствующий день. Температуры -
# целые числа, лежат в диапазоне от -50 до 50

# Использование рандомно генерируемых чисел
# заданного интервала (по условию задачи от -50 до 50)
from random import randint

# period = int(input('Введите число дней рассматриваемого периода: '))

# # Проверка на правильность ввода с вызовом ошибки
# if period > 100 or period < 1:
#     raise "Введите число от 1 до 100"

# Второй вариант проверки на правильность ввода
# цикл будет повторяться, пока не будет введено
# число согласно условию
while True:
    period = int(input('Введите число дней рассматриваемого периода: '))
    if not (period > 100 or period < 1):
        break

count = max_count = 0
for i in range(period):
    # temperature = int(input('Введите среднесут значение температуры: '))
    temperature = randint(-50, 50)
    print(f'Температура: {temperature}')
    if temperature > 0:
        count += 1
    if i == period - 1 or temperature <= 0:
        if count > max_count:
            max_count = count
        count = 0
print(f'Максимальная оттепль {max_count} дн.')
