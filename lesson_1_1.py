# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

x = int(input('Введите целое трёхначное число : \n'))

a = x // 100
b = x % 100 // 10
c = x % 10

s = a + b + c
m = a * b * c

print(f'Сумма чисел равна : {s}.')
print(f'Произведение чисел равно : {m}.')
