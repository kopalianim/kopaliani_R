from simple_colors import *  # пакет.изменение цвета(pip install simple-colors)


numbers_1  = int(input(green('Введите чиcло:\n')))
numbers_2 = int(input(green('Введите второе чиcло:\n')))
sum = numbers_1 + numbers_2
print(blue('Сложение:\n2 + 2 ='),sum)


while True:
    numbers_1 = int(input(green('Введите число:\n')))
    numbers_2 = int(input(green('Введите число:\n')))
    if numbers_2 == 0:
        print(red('ДЕЛИТЬ НА 0 НЕЛЬЗЯ.'))

    else:
        sum = numbers_1 / numbers_2
        print(blue('Деление:\n2 : 2 ='),sum)
        break


num_1 = int(input(green('Введите число:\n')))
num_2 = int(input(green('Введите второе число:\n')))
decision = num_1 * num_2                              # decision - решение
print(blue('Умножение,заданные Вами чисел:\n? * ? ='),decision)

my_num_1 = int(input(green('Введите число:\n')))      # my_num - переменные,
my_num_2 = int(input(green('Введите 2 число:\n')))
my_num_3 = int(input(green('Введите 3 число:\n')))
result = my_num_1 - my_num_2 - my_num_3
print(blue('Вычитание:\n?-?-?='),result)


while True:
    try:
        sign = int(input(green('Введите число:\n')))
        sign_2 = int(input(green('Введите  2 число:\n')))
        sign_3 = int(input(green('Введите 3 число:\n')))
        res = sign % sign_2 % sign_3
    except (ValueError, ZeroDivisionError):
        print(red('Деление на 0 запрещено, вводите только числа.'))
    else:
        print(blue('Правильно, деление по модулю:'), sign, '%', sign_2, '%', sign_3, '=', res)
        break


while True:
    try:
        num_1 = int(input(green('Введите число:\n')))
        num_2 = int(input(green('Введите второе число:\n')))
        num_3 = int(input(green('Введите третье число:\n')))
        result = num_1 ** num_2 ** num_3
    except (ValueError, ZeroDivisionError):
        print(red("Основание 0, нельзя возводить в ОТРИЦАТЕЛЬНУЮ степень, введите числа"))
    else:
        print(blue('Правильно:\nесли возвести'), num_1, (blue("в степень")), num_2, blue('и'), num_3,
              (blue("получиться")), result)
        break
