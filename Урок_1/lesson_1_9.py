# Вводятся три разных числа. Найти, какое из них является
# средним (больше одного, но меньше другого).

a = int(input('Введите целое число a : \n'))
b = int(input('Введите целое число b : \n'))
c = int(input('Введите целое число c : \n'))

if b < a < c or c < a < b:
	print(f'Среднее число : {a}')
else:
	if a < b < c or c < b < a:
		print(f'Среднее число : {b}')
	else:
		print(f'Среднее число : {c}')
