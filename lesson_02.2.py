# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

my_list = []
my_list_count = int(input('Введите количество элементов списка: '))
i = 1

while i <= my_list_count:
    my_list.append(input(f'Введите элемент {i} списка: '))
    i += 1

print(my_list)

i = 0

if my_list_count % 2 == 0:
    while i < my_list_count:
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        i += 2
else:
    while i < my_list_count - 1:
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        i += 2

print(f'\033[36m{my_list}')
