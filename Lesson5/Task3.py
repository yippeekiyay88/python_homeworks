# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('Task3.txt') as workers:
    emploeyees = workers.readlines()
    sum_salary = 0
    min_salary = 20000
    for employee in emploeyees:
        name, salary = employee.split()
        try:
            salary = float(salary)
        except ValueError:
            continue
        sum_salary = sum_salary + salary
        if salary < min_salary:
            print(name)
    print('Total salary: ', round(sum_salary / len(emploeyees), 2))

