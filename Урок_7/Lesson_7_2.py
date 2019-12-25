#  Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
#  заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random

def merge_sort_2(l, r):
	a = []
	a_left_idx = a_right_idx = 0
	a_left_l, a_right_l = len(l), len(r)
	for i in range(a_left_l + a_right_l):
		if a_left_idx < a_left_l and a_right_idx < a_right_l:
			if l[a_left_idx] <= r[a_right_idx]:
				a.append(l[a_left_idx])
				a_left_idx += 1
			else:
				a.append(r[a_right_idx])
				a_right_idx += 1
		elif a_left_idx == a_left_l:
			a.append(r[a_right_idx])
			a_right_idx += 1
		else:
			a_right_idx == a_right_l
			a.append(l[a_left_idx])
			a_left_idx += 1
	return a


def merge_sort_1(a):
	if len(a) <= 1:
		return a
	middle = len(a) // 2
	a_left = merge_sort_1(a[:middle])
	a_right = merge_sort_1(a[middle:])
	return merge_sort_2(a_left, a_right)


L = 10
N = 50
array = [round(random.uniform(0, N), 3) for i in range(L)]

print(f'{array} - исходный массив')
print(f'{merge_sort_1(array)} - отсортированный массив')
