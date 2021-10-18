# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def exp(x, y):
    if x < 0:
        return 'x must be > 0'
    if y > 0:
        return 'y must be <0'
    a = 1
    for i in range(y * -1):
        a = a * x
    return 1 / a

def exp_2(a, b):
    res = a ** b
    return res

x = float(input("Enter a positive number: "))
y = int(input("Enter a nagative number "))
a = float(input("Enter a positive number: "))
b = int(input("Enter a nagative number "))
print(exp(x, y))
print(exp_2(a, b))






