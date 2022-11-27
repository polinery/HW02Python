''' 1. Напишите программу, которая принимает на вход вещественное число
и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11 '''

num = int(input('Введите число: '))
number = str(num)
summ = 0
for i in (range(0, len(number))):
    summ += int(number[i])
print(summ)
