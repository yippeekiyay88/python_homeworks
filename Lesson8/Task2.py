# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyException(Exception):
    def __unit__(selfself, text):
        self.text = text

try:
    a = int(input("Введите число: "))
    b = int(input("Введите число: "))
    if b == 0:
        raise MyException("Вы не можете делить на 0")
    c = a / b
    print(c)
except Exception as e:
    print('Не наше исключение')
    print(e)
