# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


list = [1, 1, 2, 3, 4, 5, 6, 7, 8]
new_list = [str(i) + '\n' for i in list]

with open('Task5_1.txt', 'w') as file:
        file.writelines(new_list)

with open('Task5_1.txt') as file:
    numbers = file.read().split()
    sum = 0
    for num in numbers:
        sum = sum + int(num)

print(sum)

