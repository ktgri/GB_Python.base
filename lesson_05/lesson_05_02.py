# Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
# подсчёт строк и слов в каждой строке.

with open("text_file_02.txt", 'a') as f:
    line = input('Добавить текст в файл:\n')
    while line:
        f.writelines(line + '\n')
        line = input('Добавить текст в файл:\n')
        if not line:
            print('Текст сохранен!')
            break

with open("text_file_02.txt") as f_read:
    count_line = 0
    for line in f_read.readlines():
        count_word = 0
        for word in line.split(" "):
            if len(word) and not('\n' in word and len(word) == 1):
                count_word += 1
        print(f'В строке № {count_line + 1} слов: {count_word} ')
        count_line += 1
    f_read.seek(0)
    print(f'Всего строк в файле: {len(f_read.readlines())}')
print(f.closed)
