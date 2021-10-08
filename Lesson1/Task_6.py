# 6. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена
# составит не менее b километров. Программа должна принимать значения
# параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22

# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км


a = float(input("Enter quantity km at start date: "))
b = float(input("Enter finish quantity km: "))
day = 1
if a > b:
    print(day)
while a < b:
    i = day + 1
    a = a + a / 10
    print('At', i,'-day', round(a, 2))
    day = day + 1
print('At', day, 'day athlete reached a result — at least', b, 'km')