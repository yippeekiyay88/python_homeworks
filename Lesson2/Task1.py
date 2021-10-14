# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = ['a', '22', 55]
my_float = 8.8
my_int = 10
my_str = "Team"
my_tuple = ('b', '33', 45)
my_dict = {'First':'Первый', 'Third':'Третий'}
my_none = (None)

full_list = [my_list,my_float, my_int, my_str, my_tuple, my_dict, my_none]
for i in full_list:
    print(f'{i} is {type(i)}')



