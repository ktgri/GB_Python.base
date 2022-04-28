# Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

with open("text_file_01.txt", 'a') as f:
    line = input('Добавить текст в файл:\n')
    while line:
        f.writelines(line + '\n')
        line = input('Добавить текст в файл:\n')
        if not line:
            print('Текст сохранен!')
            break
print(f.closed)

with open("text_file_01.txt") as f_read:
    for line in f_read.readlines():
        print(line)
