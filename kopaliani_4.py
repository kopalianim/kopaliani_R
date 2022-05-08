# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

numbers = int(input('Введите целое, положительное число:\n'))
max_num = numbers % 10
num = numbers

while num > 0:

    digit = num % 10
    if digit > max_num:
         max_num = digit

    if digit == 9:
        break
    num //= 10 # num = num // 10
    print(num)
print(f'Наибольшая цыфра в числе: {num} равно {max_num}')

