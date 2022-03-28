# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict

# Мой комментарий: Лаконичного решения именно через months_list = list() и months_dict = dict() не найдено

month = int(input('Введите порядковый номер месяца: '))

print('\033[36mРешение через list:\033[0m')
months_list = ['зима', 'весна', 'лето', 'осень']
# print(months_list, type(months_list))

if 3 <= month < 6:
    print(f'Время года - {months_list[1]}')
elif 6 <= month < 9:
    print(f'Время года - {months_list[2]}')
elif 9 <= month < 12:
    print(f'Время года - {months_list[3]}')
else:
    print(f'Время года - {months_list[0]}')

print('\n\033[36mРешение через dict:\033[0m')
months_dict = {3: 'зима', 6: 'весна', 9: 'лето', 12: 'осень'}
# print(months_dict, type(months_dict))

if 3 <= month < 6:
    print(f'Время года - {months_dict.get(6)}')
elif 6 <= month < 9:
    print(f'Время года - {months_dict.get(9)}')
elif 9 <= month < 12:
    print(f'Время года - {months_dict.get(12)}')
else:
    print(f'Время года - {months_dict.get(3)}')
