# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого
# числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
import math
import timeit

L = 200000


# s = """
def func_sieve(n):
	a = [i for i in range(L + 1)]
	a[1] = 0
	i = 2

	while i <= L:
		if a[i] != 0:
			j = i + i
			while j <= L:
				a[j] = 0
				j = j + i
		i += 1
	b = []
	for i in a:
		if a[i] != 0:
			b.append(a[i])
	return (b[n - 1])


# func_sieve(14)"""

# s_1 = """
def func_not_sieve(n):
	a = set(range(2, L + 1))
	for i in range(2, int(math.sqrt(L + 1))):
		if i in a:
			a -= set(range(2 * i, L + 1, i))
	a = list(a)
	return (a[n - 1])


# func_not_sieve(14)"""

# s_2 = """
def func_not_sieve_2(n):
	a = [2]
	for i in range(3, L + 1, 2):
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
	return (a[n - 1])


# func_not_sieve_2(14)"""


print(func_sieve(14))
print(func_not_sieve(14))
print(func_not_sieve_2(14))
# print(timeit.timeit(s, number=100, globals=globals()))
# print(timeit.timeit(s_1, number=100, globals=globals()))
# print(timeit.timeit(s_2, number=100, globals=globals()))

# 0.010269301000000002   func_sieve(14) L=200
# 0.128082144            func_sieve(14) L=2000
# 1.424428825            func_sieve(14) L=20000
# 16.049712243           func_sieve(14) L=200000

# 0.002509941999999994   func_not_sieve(14) L=200
# 0.044982076 			 func_not_sieve(14) L=2000
# 0.8138122369999999     func_not_sieve(14) L=20000
# 8.039038459            func_not_sieve(14) L=200000

# 0.006403150000000003   func_not_sieve_2(14) L=200
# 0.096462475            func_not_sieve_2(14) L=2000
# 1.722318794            func_not_sieve_2(14) L=20000
# 30.523845847           func_not_sieve_2(14) L=200000
