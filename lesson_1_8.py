# Определить, является ли год, который ввел пользователь, високосным или не високосным.

# год, номер которого кратен 400, — високосный;
# остальные годы, номер которых кратен 100, — невисокосные;
# годы, номер которых кратен 4, — високосные.


year = int(input('Введите год для определения его на високостность : \n'))

if year % 400 == 0:
	print('Этот год високостный.')
else:
	if year % 100 == 0:
		print('Этот год НЕвисокостный.')
	else:
		if year % 4 == 0:
			print('Этот год високостный.')
		else:
			print('Этот год НЕвисокостный.')
