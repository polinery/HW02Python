''' 5. Реализуйте алгоритм перемешивания списка.'''

form = ['Иван Иванов', '01.01.2019', 3.92, True, (2, 5), ['a', 'd', 'e']]

import random

random.shuffle(form)
print(form)
