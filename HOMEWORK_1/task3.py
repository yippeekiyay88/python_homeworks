# # 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# # Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = int(input("Enter number: "))
n1 = str(n)
n2 = n1 + n1
n3 = n1 + n1 + n1
nn = n + int(n2) + int(n3)
print("Input:", nn)


