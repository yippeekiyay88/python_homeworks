# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

seasons_list = [
    ['Winter', ['12', '1', '2']],
    ['Spring', ['3', '4', '5']],
    ['Summer', ['6', '7', '8']],
    ['Autumn', ['9', '10', '11']]
]

seasons_dict = {
    'Winter': ['12', '1', '2'],
    'Spring': ['3', '4', '5'],
    'Summer': ['6', '7', '8'],
    'Autumn': ['9', '10', '11']
}

while True:
    month_number = input('Enter the number of the month: ')
    if month_number not in sum(seasons_dict.values(), []):
        print('Incorrect month, try again')
        continue

    break

for season, months in seasons_list:
    if month_number in months:
        print(f'{month_number} is {season}')

for season, months in seasons_dict.items():
    if month_number in months:
        print(f'{month_number} is {season}')

