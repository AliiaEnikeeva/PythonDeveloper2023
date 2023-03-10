'''
Заполните массив элементами арифметической
прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. Формула для
получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15
'''

def arithmetic_sequence(a1: int, d: int, n:int):
    sequence = [a1]
    for i in range(2, n + 1):
        sequence.append(a1 + (i - 1) * d)
    return sequence


a1 = int(input('Введите первый член последовательности: '))
d = int(input('Введите разность между членами последовательности: '))
n = int(input('Введите количество членов последовательности: '))
print(*arithmetic_sequence(a1, d, n))