# Пользователь вводит две строчные буквы латинского алфавита.
# Определить, на каких местах алфавита
# они стоят, и сколько между ними находится букв.


a = input('Введите первую строчную букву латинского алфавита : \n')
b = input('Введите первую вторую букву латинского алфавита : \n')


a1 = ord(a)
b1 = ord(b)

x = a1 - ord('a') + 1
y = b1 - ord('a') + 1
# если пользователь решит ввести первой букву находящуюся к концу алфавита,
# а второй введёт букву находящуюся ближе к началу алфавита
z = (abs(y - x) - 1)

print(f'буква -{a}- стоит на месте под номером : {x}')
print(f'буква -{b}- стоит на месте под номером : {y}')
print(f'количество букв между -{a}- и -{b}- : {z}')

