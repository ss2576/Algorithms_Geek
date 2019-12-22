# 3 способа составления ряда простых чисел до n-го.
# n-е число задаётся в качестве параметра при вызове функции.
# в конце каждого варианта решения сохранял ряд в разных типах данных
# str, list , tuple которые вместе со всеми локальными переменными
# далее и считал в функции memory на размер занимаемой памяти.
# Версия ОС Windows 8.1 64x ,Python 3.7.4

import math
import sys
import platform


def memory(f):
	memory_sum = 0
	print('*' * 80)
	for key, value in f.items():
		memory_sum += sys.getsizeof(value)
		print(f'переменная -{key}- имеет тип {type(value)} и занимает {sys.getsizeof(value)} байт')
	print(f'ОБЩАЯ СУММА ЗАНИМАЕМОЙ ПАМЯТИ : {memory_sum} байт')


def func_sieve(n):
	a = [i for i in range(n + 1)]
	a[1] = 0
	i = 2


	while i <= n:
		if a[i] != 0:
			j = i + i
			while j <= n:
				a[j] = 0
				j = j + i
		i += 1
	b = []
	for i in a:
		if a[i] != 0:
			b.append(a[i])
	a = str(a)
	b = str(b)
	return locals()




def func_not_sieve(n):
	a = set(range(2, n + 1))
	for i in range(2, int(math.sqrt(n + 1))):
		if i in a:
			a -= set(range(2 * i, n + 1, i))
	a = list(a)
	return locals()




def func_not_sieve_2(n):
	a = [2]
	for i in range(3, n + 1, 2):
		if (i > 10) and (i % 10 == 5):
			continue
		for j in a:
			if j * j - 1 > i:
				a.append(i)
				break
			if (i % j == 0):
				break
		else:
			a.append(i)
	a = tuple(a)
	return locals()


memory(func_sieve(200000))

memory(func_not_sieve(200000))

memory(func_not_sieve_2(200000))

print('#'*25, 'Разрядность ОС и версия Python','#'*25 )
print(platform.architecture())
print(sys.version_info)

