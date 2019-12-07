# Найти сумму n элементов следующего ряда чисел:
# 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

number = int(input('Введите количество элементов в списке :\n'))
first_e = 1
summ = 0
lst = []
for i in range(number):
    # каждый второй элемент списка(чётный) будет отрицательным
    if i % 2 != 0:
        summ += first_e
        lst.append(first_e)
        first_e /= -2
    else:
        summ += first_e
        lst.append(first_e)
        first_e /= -2

print(f'считаем сумму по заданному списку {lst}, \nполучившаяся сумма {summ}')