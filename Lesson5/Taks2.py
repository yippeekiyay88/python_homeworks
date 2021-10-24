# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('Task2.txt', 'r') as f_obj:
    content = f_obj.readlines()
    str_quant = 0
    for num, line in enumerate(content):
        str_quant = str_quant + 1
        words_quant = len(line.split())
        print(f'in {num + 1} string {words_quant} words. ' + '\n')
print(f'All string quantity {str_quant}')

