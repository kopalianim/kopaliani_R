# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

my_str = (input('Пользователь, введите несколько слов:\n')).split()
for i, word in enumerate(my_str, 1):
    print(f'{i}--> {word:10}')
