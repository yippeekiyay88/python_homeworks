# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

dict = {
    'One' : 'Один',
    'Two' : 'Два',
    'Three' : 'Три',
    'Four' : 'Четыре'
}
new_file = []
with open('Task4.txt', 'r') as file_obj:
    l = file_obj.readlines()
    for i in l:
        i = i.split()
        new_file.append(dict[i[0]] + ' ' + i[1] + ' ' + i[2] + '\n')
    print(new_file)
with open('Task4_new.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)

