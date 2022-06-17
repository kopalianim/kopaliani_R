#1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


def calculation():              # calculation - расчет
    try:
        workings, bet, bonus = map(float, argv[1:])         # workings  выроботка в часах  bet -ставка  bonus -бонус
        print(f'calculation - {workings * bet + bonus}')
    except ValueError:
        print('Введите 3 числа. Не строки, не пустой ввод')

calculation()


