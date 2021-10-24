# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('file.txt', 'a') as f_obj:
    while True:
        user_input = input('Enter some strings: ')
        f_obj.write(user_input + '\n')
        if not user_input:
            break
f_obj = open('file.txt', 'r')
content = f_obj.readlines()
print(content)

