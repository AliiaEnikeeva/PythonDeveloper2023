''' Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел. Из
всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
Input 2 2
Output 4 '''


def summa(a, b):
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    return 1 + summa(a, b - 1)


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(summa(a, b))

# Вариант Романа
# def sum(x, y):
#     if y == 0:
#         return x
#     return (sum(x, y-1))+1

# a = int(input('Введите число а = '))
# b = int(input('Введите число b = '))

# print('Сумма чисел a и b = ', sum(a, b))