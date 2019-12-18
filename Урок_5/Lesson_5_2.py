# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры
# числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
# [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

BIN_MATRIX = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
			  '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
			  'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

HEX_MATRIX = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']

x = deque(input('Введите первое число в hex формате: ').upper())
y = deque(input('Введите второе число в hex формате: ').upper())

a = x.copy()
b = y.copy()
if len(b) > len(a):
	a, b = b, a

b.extendleft('0' * (len(a) - len(b)))
addition = deque()
surplus = 0

for i in range(len(a) - 1, -1, -1):
	a_bin = BIN_MATRIX[a[i]]
	b_bin = BIN_MATRIX[b[i]]
	addition_sum = a_bin + b_bin + surplus
	if addition_sum >= 16:
		surplus = 1
		addition_sum -= 16
	else:
		surplus = 0
	addition.appendleft(HEX_MATRIX[addition_sum])
if surplus == 1:
	addition.appendleft('1')

print(*x, ' + ', *y, ' = ', *addition)
