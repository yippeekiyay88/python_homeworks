# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_data(name, lastname, yearbirth, city, email, phone):
    print(f'{name}, {lastname}, {yearbirth}, {city}, {email}, {phone}')

a = input("Name: ")
b = input("Lastname: ")
c = input("Yearbirth: ")
d = input("City: ")
e = input("Email: ")
f = input("Phone: ")
user_data(name=a, lastname=b, yearbirth=c, city=d, email=e, phone=f)



