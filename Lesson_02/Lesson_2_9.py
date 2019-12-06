# Среди натуральных чисел, которые были введены, найти наибольшее
# по сумме цифр. Вывести на экран это число и сумму его цифр.

number = int(input('Введите любое натуральное число :\n'))
max_summ = 0
max_number = 0
while number != 0:
	m = number
	count = 0
	while number > 0:
		count += number % 10
		number //= 10
	if count > max_summ:
		max_summ = count
		max_number = m
	number = int(input('Введите ещеё одно натуральное число(для начала подсчёта введите цифру НОЛЬ) :\n'))
print('Число', max_number, 'имеет максимальную сумму цифр:', max_summ)
