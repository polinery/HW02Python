''' 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict. '''

num_month = int(input('Введите номер месяца от 1 до 12: '))
seasons = ['зима', 'весна', 'лето', 'осень']
if num_month < 3 or num_month == 12:
    season = seasons[0]
elif num_month < 6:
    season = seasons[1]
elif num_month < 9:
    season = seasons[2]
else:
    season = seasons[3]
print(f'через list: {season}')

seasons2 = {12: 'зима', 1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна',
            5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень',
            10: 'осень', 11: 'осень', }
print(f'через dict: {seasons2[num_month]}')
