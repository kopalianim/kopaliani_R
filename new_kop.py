from simple_colors import *

attempts = 5     # кол-во попыток
while True:
    fr_1 = int(input(green('Введите число:')))      # fr_1 какой-то пользователь
    if fr_1 % 2 == 0:
        print(cyan('%d чётное число.' % fr_1))
    else:
        fr_1 % 2 != 0
        print(red("не чётное число."))
    attempts -= 1
    if attempts > 0:
        print('Left', attempts)
    else:
        print(red('Exit. Попытки закончились.'))
    break
#__________________________
user = int(input(green('Введите число:')))
while user > 0:
    if user % 2 == 0:
        print(f'Чётное число - {user}')
    else:
        print(f'Не чётное число - {user}')
    break
#__________________________
users_numbers = input(green('Введите число:'))
users_num = len(users_numbers)
integ = []
i = 0
while i < users_num:
    users_num_integ = ''
    num = users_numbers[i]
    while '0' <= num <= '9':
        users_num_integ += num
        i += 1
        if i < users_num:
            num = users_numbers[i]
        else:
            break
    i += 1
    if users_num_integ != '':
        integ.append(int(users_num_integ))
print('Только числа -', integ)

#____________________
list_1 = [-21, -20, -19, -18, -17, 15, 16, 17, 18, 19, 20, 21]
list_1.remove(20)
list_1.insert(41, 200)
print(list_1)
#______________________

list_1 = [5, 8, 9, 10, "", 11, 12, "stroka ", 14, 15, 16, "", 19, 20, 21]
my_list = list(filter(None, list_1))
print(my_list)
#____________________-

list_1 = [5, 8, 9, 10, 11, 12, 14, 15, 16, 19, 20, 21]
for i in list_1:
   print('квадрат числа-', i, '=', i ** 2)

#_______________________-

list_1 = [5, 8, 9, 10, 11, 12, 14, 15, 16, 19, 20, 21]
def removeValue(sampleList, val):
    return [value for value in sampleList if value != val]
resList = removeValue(list_1, 20)
print(resList)

#_________________________

def change(lst):
    new_start = lst.pop()
    new_end = lst.pop(0)
    lst.append(new_end)
    lst.insert(0, new_start)
    return lst
print(change([1, 2, 3]))
print(change(['p', 't', 'o', ' s']))

