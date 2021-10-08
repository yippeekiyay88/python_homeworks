# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.

seconds = int(input('Enter seconds: '))
n = 86400
hour = (seconds // 3600) % 24
minutes = (seconds // 60) % 60
sec = seconds % 60
if seconds <= n:
    print('%02d:%02d:%02d' % (hour, minutes, sec))
else:
    print('Format time error')

# print(f"{hour}:{minutes}:{sec}")    - не понимаю, как сделать через f"























