# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал
# (т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import namedtuple

Company = namedtuple('Company', ['name', 'profit', 'quarter'])
companies = set()
Q = 4
number_of_enterprises = int(input('Какое кол-во предприятий будем вводить ? '))
all_profit = 0

for i in range(number_of_enterprises):
	quarter = []
	profit = 0
	name_of_enterprises = input(f'Введите наименование предприятия № {i + 1}: ')
	for j in range(Q):
		quarter.append(int(input(f'Введите прибыль за {j + 1} квартал : ')))
		profit += quarter[j]

	company = Company(name=name_of_enterprises, profit=profit, quarter=tuple(quarter))
	companies.add(company)
	all_profit += profit

average = all_profit / number_of_enterprises
print(f'Средняя прибыль равна равна : {average}')

print('Предприятие с прибылью ниже среднего:')
for company in companies:
	if company.profit < average:
		print(f'Компния {company.name} заработала {company.profit}')

print('Предприятие с прибылью выше среднего:')
for company in companies:
	if company.profit > average:
		print(f'Компния {company.name} заработала {company.profit}')
