# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен
# разместиться после них.

numbers = input('Введите набор натуральных чисел, разделённых пробелами: ')
list_of_numbers = numbers.split()

for i in range(len(list_of_numbers)):
    list_of_numbers[i] = int(list_of_numbers[i])
list_of_numbers.sort(reverse=True)

new_element = int(input('Введите новый элемент рейтинга: '))
try:
    list_of_numbers.insert(list_of_numbers.index(new_element) + 1, new_element)
except ValueError:
    list_of_numbers.append(new_element)
    list_of_numbers.sort(reverse=True)

print(f'Пользователь ввёл число {new_element}. Результат:', end=' ')
for i in range(len(list_of_numbers)):
    if i != (len(list_of_numbers) - 1):
        print(list_of_numbers[i], end=', ')
    else:
        print(list_of_numbers[i], end='.\n')
