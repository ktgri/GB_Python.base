# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

string = input('Введите строку из нескольких слов, разделённых пробелами: ')
list_of_words = string.split()

for i in range(len(list_of_words)):
    if len(list_of_words[i]) > 10:
        print(i + 1, list_of_words[i][:10])
    else:
        print(i + 1, list_of_words[i])
