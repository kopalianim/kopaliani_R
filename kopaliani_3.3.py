# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

def my_func(num_1: int, num_2: int, num_3: int) -> int:
    my_list = [num_1, num_2, num_3]
    try:
        my_list.remove(min(my_list))
        return sum(my_list)
    except TypeError:
        return 'Enter only a numbers'



def my_func(arg_1, arg_2, arg_3):
    my_list = [arg_1, arg_2, arg_3]
    return sum(sorted(my_list)[1:])

print(my_func(345, 4, -30))

