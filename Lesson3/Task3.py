# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def func(number_1, number_2, number_3):
    sum_numbers = number_1 + number_2 + number_3
    return sum_numbers - min((number_1, number_2, number_3))

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
print(func(a, b, c))




