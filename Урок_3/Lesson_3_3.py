# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

L = (int(input('сколько сгенерировать чисел в строке ?: \n')))
max_number = int(input('какая максимальная цифра в  матрице ? :\n'))
arr = []
for i in range(L):
	arr.append(random.randint(1, max_number))
print(arr)

min_ = 0
max_ = 0
for i in range(L):
	if arr[i] < arr[min_]:
		min_ = i
	elif arr[i] > arr[max_]:
		max_ = i

print(f'менятся будут местами: \nмаксимальное число {arr[max_]} (порядковый № {max_ + 1}) и \n'
	  f'минимальное число {arr[min_]} (порядковый № {min_ + 1})')

temp = arr[min_]
arr[min_] = arr[max_]
arr[max_] = temp

print('массив после замены: \n', arr)