# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

x = int(input('Enter positive integer: '))
max = 0
while x > 0:
    c = x % 10
    if c >= max:
        max = c
        x = x // 10
    else:
        break
print('The biggest number is:', max)




