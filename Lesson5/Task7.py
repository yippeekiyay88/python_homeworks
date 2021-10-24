# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 200 0}]

# Подсказка: использовать менеджеры контекста.

import json

my_dicts = [{}, {}]

with open('Task7.txt') as file:
    file_lines = file.readlines()
    for line in file_lines:
            name, _, proceeds, expenses = line.split()
            my_dicts[0][name] = int(proceeds) - int(expenses)
            average_profit = sum(profit for _, profit in my_dicts[0].items() if profit > 0) / len(my_dicts[0])
            my_dicts = [my_dicts[0], {'average_profit': average_profit}]
print(my_dicts)

with open('Task7.json', 'w') as file:
    json.dump(my_dicts, file)

