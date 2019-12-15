# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random
import timeit
import cProfile


# для анализа передаём в функцию данные по высоте h и длине l матрицы.

#s = """
def max_from_min(l, h):
	MAX_NUMBER = 1000
	MIN_NUMBER = - 1000
	matrix = [[random.randint(MIN_NUMBER, MAX_NUMBER) for i in range(l)] for i in range(h)]
	#[print(i) for i in matrix]
	max_ = MIN_NUMBER
	for j in range(l):
		min_ = MAX_NUMBER
		for i in range(h):
			if matrix[i][j] < min_:
				min_ = matrix[i][j]
		if min_ > max_:
			max_ = min_
	return max_

#max_from_min(40, 40)"""

print(f'Максимальный среди минимальных: {max_from_min(10, 5)}')

# При увеличении матрицы в 4 раза (l*2 , h*2),скорость выполнения увеличивается в 4 раза

# 0.004872926  max_from_min(5, 5)
# 0.018042655  max_from_min(10, 10)
# 0.068074473  max_from_min(20, 20)
# 0.269445984  max_from_min(40, 40)
#print(timeit.timeit(s, number=100, globals=globals()))
#cProfile.run('max_from_min(40, 40)')
# 25 0.000 0.000 0.000 0.000 random.py: 174(randrange)     max_from_min(5, 5)
# 25 0.000 0.000 0.000 0.000 random.py: 218(randint)
# 25 0.000 0.000 0.000 0.000 random.py: 224(_randbelow)

# 100 0.000 0.000 0.000 0.000 random.py: 174(randrange)     max_from_min(10, 10)
# 100 0.000 0.000 0.000 0.000 random.py: 218(randint)
# 100 0.000 0.000 0.000 0.000 random.py: 224(_randbelow)

# 400 0.000 0.000 0.000 0.000 random.py: 174(randrange)     max_from_min(20, 20)
# 400 0.000 0.000 0.000 0.000 random.py: 218(randint)
# 400 0.000 0.000 0.000 0.000 random.py: 224(_randbelow)


#s_2 = """
def max_from_min_2(l, h):
	MAX_NUMBER = 1000
	MIN_NUMBER = - 1000
	matrix = [[random.randint(MIN_NUMBER, MAX_NUMBER) for i in range(l)] for i in range(h)]
	#[print(i) for i in matrix]
	d = []
	for j in range(l):
		b = []
		for i in range(h):
			b.append(matrix[i][j])
		c = min(b)
		d.append(c)
	e = max(d)
	return e

#max_from_min_2(40, 40)"""
print(f'Максимальный среди минимальных: {max_from_min_2(10, 5)}')

# При увеличении матрицы в 4 раза (l*2 , h*2),скорость выполнения увеличивается в 4 раза
# но в сравнении с первым алгоритмом он выполняется на 20% долше.

# 0.005752805          max_from_min_2(5, 5)
# 0.02525710600000001  max_from_min_2(10, 10)
# 0.069498796          max_from_min_2(20, 20)
# 0.344850141          max_from_min_2(40, 40)
#print(timeit.timeit(s_2, number=100, globals=globals()))
#cProfile.run('max_from_min_2(20, 20)')

# 25 0.000 0.000 0.000 0.000 random.py: 174(randrange)     max_from_min_2(5, 5)
# 25 0.000 0.000 0.000 0.000 random.py: 218(randint)
# 25 0.000 0.000 0.000 0.000 random.py: 224(_randbelow)

# 100 0.000 0.000 0.000 0.000 random.py: 174(randrange)     max_from_min_2(10, 10)
# 100 0.000 0.000 0.000 0.000 random.py: 218(randint)
# 100 0.000 0.000 0.000 0.000 random.py: 224(_randbelow)

# 400 0.000 0.000 0.000 0.000 random.py: 174(randrange)     max_from_min_2(20, 20)
# 400 0.000 0.000 0.000 0.000 random.py: 218(randint)
# 400 0.000 0.000 0.000 0.000 random.py: 224(_randbelow)