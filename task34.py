# Задача №34
# Винни-Пух попросил вас посмотреть, есть ли в егостихах ритм.
# Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е число
# гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько
# слов, то они разделяются дефисами. Фразы отделяются друго от
# друга пробелами. Стихотворение Винни-Пух вбивает в программу
# с клавиатуры. В ответе напишите "Парам пам-пам", если с
# ритмом все в порядке и "Пам парам", если с ритмом все не в
# порядке.

def rhythm(str):
    str = str.split()
    list_1 = []
    for word in str:
        sum_vl = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                sum_vl += 1
        list_1.append(sum_vl)
    return len(list_1) == list_1.count(list_1[0])


str_1 = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
if rhythm(str_1):
    print('Парам пам-пам')
else:
    print('Пам парам')
