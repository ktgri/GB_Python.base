# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [605, "My_list", 948.98, [3, 'Hello!'], None]
for i in my_list:
    print(i, type(i))
