# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать
# данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

with open("firms_07.txt", 'r', encoding='utf-8') as f:
    data_revenue = {}
    profit = 0
    len_profit = 0
    for line in f.readlines():
        name_firm = line.split(' ')[0]
        revenue_inp = float(line.split(' ')[2])
        costs_inp = float(line.split(' ')[3][:-1])
        if revenue_inp >= costs_inp:
            profit += revenue_inp - costs_inp
            len_profit += 1
        data_revenue.update({name_firm: (revenue_inp - costs_inp)})
    list_revenue = (data_revenue, {'average_profit': round(profit / len_profit, 2)})
    print(list_revenue)
    with open("firms_07_JSON.json", 'w', encoding='utf-8') as j:
        json.dump(list_revenue, j)

with open("firms_07_JSON.json", 'r', encoding='utf-8') as j_r:
    print(j_r.readlines())

# for i in list_revenue:
#     for key, val in list_revenue[0].items():
#         print(f'{key} : {val}')
#     print(list_revenue[1])
