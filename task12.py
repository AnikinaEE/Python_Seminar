# Задача №12
# Петя и Катя - брат и сестра. Петя - студент, а Катя -
# школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y <=1000),
# а Катя должна их отгадать. Для этого Петя делает две
# подсказки. Он называет сумму этих чисел S и их
# произведение Р.
# Помогите Кате отгадать задуманные Петей числа.

sum = int(input('Введите сумму чисел X и Y: '))
multipl = int(input('Введите произведение чисел X и Y: '))

# Заданные числа определяются решением квадратного уравнения:
# X+Y=sum, X*Y=multipl
# X=sum-Y, Y*(sum-Y)=multipl
# Y**2 - sum*Y + multipl = 0 для решения данного уравнения
# вычисляется дискриминант: diskr = sum**2 - 4*multipl
# Если дискриминат < 0, действительных корней нет,
# если равен 0, то Y = -sum/2
discr = sum ** 2 - 4 * multipl
if discr < 0:
    print('Определить X и Y невозможно')
elif discr == 0:
    num_y = sum/2
    num_x = sum - num_y
    print(f'Число X равно - {num_x}, число Y равно - {num_y}')
else:
    num_y1 = (sum + discr**0.5)/2
    num_y2 = (sum - discr**0.5)/2
    num_x1 = sum - num_y1
    num_x2 = sum - num_y2
    print(f'Числа X и Y равны {num_x1} и {num_y1} или {num_x2} и {num_y2}')