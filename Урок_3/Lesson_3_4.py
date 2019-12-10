# Определить, какое число в массиве встречается чаще всего.



import random
L = (int(input('сколько сгенерировать чисел в строке ?: \n')))
max_number = int(input('какое максимальное число в  строке ? :\n'))


arr = []
for i in range(L):
	arr.append(random.randint(1, max_number))
print(arr)


max_num = arr[0]
max_num_of_times = 1
for i in range(L - 1):
	num_of_times = 1
	for j in range(i + 1, L):
		if arr[i] == arr[j]:
			num_of_times += 1
	if num_of_times > max_num_of_times:
		max_num_of_times = num_of_times
		max_num = arr[i]

if max_num_of_times > 1:
	print(f'число {max_num} встречается  {max_num_of_times} раз(а).')
else:
	print('Все элементы уникальны')