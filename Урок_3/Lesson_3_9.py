# Найти максимальный элемент среди минимальных элементов столбцов матрицы.


import random

l = int(input('какой длины сделать матрицу ? :\n'))
h = int(input('какой высоты сделать матрицу ? :\n'))
max_number = int(input('какая максимальная цифра в  матрице ? :\n'))
arr = []
for i in range(h):
	a = []
	for j in range(l):
		n = random.randint((max_number) / -1 ,max_number)
		a.append(n)
		print(n, ' ', end='')
	arr.append(a)
	print()

max = (max_number) / -1
for j in range(l):
	min_ = max_number
	for i in range(h):
		if arr[i][j] < min_:
			min_ = arr[i][j]

	if min_ > max_:
		max_ = min_

print()
print(f'Максимальный среди минимальных: {max_}')
