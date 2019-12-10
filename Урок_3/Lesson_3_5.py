# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве




import random

L = (int(input('сколько сгенерировать чисел в строке ?: \n')))
max_number = abs(int(input('какое число сделать максимальным(минимальным)в строке ?: \n')))
arr = []
for i in range(L):
	arr.append(random.randint((max_number / -1), max_number))
print(arr)

i = 0
idx = -1
while i < L:
	if arr[i] < 0 and idx == -1:
		idx = i
	elif arr[i] < 0 and arr[i] > arr[idx]:
		idx = i
	i += 1

print()
print(f'макисм. отриц. элемент {arr[idx]} ,находится под индексом №{idx}')
