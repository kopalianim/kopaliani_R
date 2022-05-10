# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.

def user_date(name, surname, year_birth, city_residence, email, telephone):
    return f'Name - {name}; Surname - {surname}; Year_birth - {year_birth};'\
           f'City_residence - {city_residence}; Email - {email}; Telephone - {telephone};'


def users_date(**kwargs):
    return " ".join(kwargs.values())


Name = input('Введите name - ')
Surname = input('Введите Surname - ')
Year_birth = input('Введите Year_birth - ')
City_residence = input('Введите City_residence - ')
Email = input('Введите Email - ')
Telephone = input('Введите Telephone - ')

print(users_date(Name=Name, Surname=Surname, Year_birth=Year_birth, City_residence=City_residence, Email=Email, Telephone=Telephone))




