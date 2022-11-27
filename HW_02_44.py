''' 4.Задайте список из N элементов, заполненных числами из промежутка [-N, N].
 Найдите произведение элементов на указанных позициях.
 Позиции хранятся в файле file.txt в одной строке одно число.'''

import random

n = int(input('Введите число N: '))
numbers = []
for i in range(n):
    temp = random.randint(-n, n)
    numbers.append(temp)
print(numbers)

positions = input('Введите позиции нескольких элементов через пробел: ')
positions = positions.split()

product = 1
for i in range(len(positions)):
    product = product * numbers[int(positions[i])]
print(product)
