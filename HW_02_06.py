''' 6. *Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})]

Необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”] '''

product_list = []
number_of_positions = 3

for i in range(number_of_positions):
    art_num = int(input('Введите номер товара: '))
    art_name = input('Введите название товара: ')
    art_prise = int(input('Введите цену товара: '))
    art_count = int(input('Введите количество товара: '))
    art_unit = input('Введите единицу измерения товара: ')
    parameters = {'Название': art_name, 'Цена': art_prise,
                  'Количество': art_count, 'Ед.': art_unit}
    articul = (art_num, parameters)
    product_list.append(articul)
print(*product_list, sep='\n')
k_name = 'Название'
k_prise = 'Цена'
k_count = 'Количество'
k_unit = 'Ед.'
name = []
prise = []
count = []
unit = []
for i in range(len(product_list)):
    parameter = product_list[i][1]
    name.append(parameter[k_name])
    prise.append(parameter[k_prise])
    count.append(parameter[k_count])
    unit.append(parameter[k_unit])
name = list(set(name))
prise = list(set(prise))
count = list(set(count))
unit = list(set(unit))
specification = {k_name: name, k_prise: prise, k_count: count, k_unit: unit}
print(specification)
