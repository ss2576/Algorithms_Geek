# В программе генерируется случайное целое число от 0 до 100. Пользователь должен
# его отгадать не более чем за 10 попыток. После каждой неудачной попытки должно
# cообщаться больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, то вывести загаданное число.

import  random

number = random.randint(0, 100)
# оставил подсказку для проверки
print(number)


user_number = None
count = 0

while number != user_number:
	count += 1
	if count > 10:
		print(f'Вы проиграли!!!\nЗагаданное число -{user_number}-')
		break
	print(f'Попытка № {count}')
	user_number = int(input('Введите число: \n'))
	if number < user_number:
		print('Ваше число больше загаданного!')
	elif number > user_number:
		print('Ваше число меньше загаданного!')
else:
	print('Победа!вы угадали!!!')