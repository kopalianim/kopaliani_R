#1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [1, 1.45, [56, 789], 'hello', True, None, False, (-1 + 454), ("R" + "T"), {34, 67}, (934, 865), (9, 54, 67, 3),{67: 'type'}, {78: 'ret'}]
for i, item in enumerate(my_list, 1):
    print(f'{i}) {item}-{type(item)}')

