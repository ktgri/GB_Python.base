# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами, то есть характеристиками товара:
# название, цена, количество, единица измерения. Структуру нужно сформировать программно,
# запросив все данные у пользователя.

list_of_goods = []
goods_count = int(input('Введите\033[33m количество\033[m товаров: '))
i = 1

while i <= goods_count:
    name = input(f'Введите\033[31m название\033[0m товара №{i}: ')
    price, amount = map(int, input(f"Введите\033[31m цену и кол-во\033[0m "
                                   f"товара №{i} через разделитель '/': ").split('/'))
    unit = input(f'Введите\033[31m единицу\033[0m измерения товара №{i}: ')
    good = (i, dict(название=name, цена=price, количество=amount, ед=unit))
    list_of_goods.append(good)
    i += 1

print('\033[36mСпецификация товаров:\033[0m')
for i in range(len(list_of_goods)):
    print(list_of_goods[i])

# Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например, название. Тогда значение — список значений-характеристик, например, список названий товаров.

print('\033[36mАналитика товаров:\033[0m')

names = []
prices = []
amounts = []
units = []
list_of_goods_analysis = {}
i = 0

for i in range(len(list_of_goods)):
    d = list_of_goods[i][1]
    names.append(d.get('название'))
    prices.append(d.get('цена'))
    amounts.append(d.get('количество'))
    units.append(d.get('ед'))

list_of_goods_analysis = dict(название=list(set(names)),
                              цена=list(set(prices)),
                              количество=list(set(amounts)),
                              ед=list(set(units)))

for key, value in list_of_goods_analysis.items():
    print(key, ':', value)
