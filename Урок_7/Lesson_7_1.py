# 1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными
# числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
import random


def bubble_sort_reverse(a, reverse):
    if reverse == False :
        n = len(a)
        while n != 0:
            for i in range(len(a) - n):
                if a[i + n] > a[i + n - 1]:
                    a[i + n], a[i + n - 1] = a[i + n - 1], a[i + n]
            n -= 1
        return a
    else:
        n = 1
        while n < len(a):
            for i in range(len(a) - n):
                if a[i] > a[i + 1]:
                    a[i], a[i + 1] = a[i + 1], a[i]
            n += 1
        return a

L = 15
N = 100
array = [random.randrange(-N, N) for i in range(L)]

print(f'{array} - исходный массив')
print(f'{bubble_sort_reverse(array, True)} - отсортированный массив')
print(f'{bubble_sort_reverse(array, False)} - реверсивно отсортированный массив')
