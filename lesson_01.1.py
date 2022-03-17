# Поработайте с переменными, создайте несколько, выведите на экран.

str_01 = 'Hello!'
print('{} (type = {})'.format(str_01, type(str_01)))

str_02 = 'Hallo!!'
print('{} (type = {})'.format(str_02, type(str_02)))

int_01 = 6050
print('{} (type = {})'.format(int_01, type(int_01)))

float_01 = 60.503
print('{} (type = {})'.format(float_01, type(float_01)))

list_01 = ['Test01', 906]
print('{} (type = {})'.format(list_01, type(list_01)))

tuple_01 = ('Test02', 5786)
print('{} (type = {})'.format(tuple_01, type(tuple_01)))
print()

# Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.

str_03 = input('Введите текст: ')
print('{} (type = {})'.format(str_03, type(str_03)))

str_04 = input('Введите число: ')
print('{} (type = {})'.format(str_04, type(str_04)))

int_02 = int(input('Преобразуем в число?) Введите число: '))
print('{} (type = {})'.format(int_02, type(int_02)))

float_02 = float(input('Введите число с плавающей точкой: '))
print('{} (type = {})'.format(float_02, type(float_02)))
