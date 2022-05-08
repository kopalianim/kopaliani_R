# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
number = (input('Введите число: \n'))
result_1 = int(number)
result_2 = number + number
result_3 = number + number + number
numbers = int(result_1) + int(result_2) + int(result_3)
print(f'{result_1} + {result_2} + {result_3} = {int(result_1) + int(result_2) + int(result_3)}')
