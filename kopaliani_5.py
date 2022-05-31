#5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма. Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее сообщение.

#Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке. Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.


# revenue - выручка
# lesion - убыток
# profitability- рентабельность
# number  - число сотрудников
# profix  - прибыль на одного сотрудника

revenue = int(input("Введите выручку фирмы: \n"))
costs = int(input("Введите издержки фирмы:\n"))
profit = revenue - costs
print("Прибыль фирмы", profit)
lesion = profit > revenue
if profit > 0:
    print(f'Рентабельность: {profit / costs * 100: .2f} %')
    number = int(input("Введите число сотрудников:\n"))
    print(f'Прибыль фирмы на 1 сотрудника: {profit / number: .2f}')
elif profit < lesion:
    print('Фирма в убытке')

