# Создать (не программно) текстовый файл со следующим содержимым:
# text_file_04.txt
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.

import re

with open("text_file_04.txt", 'r', encoding='utf-8') as f:
    numbers = {'One': 'Один',
               'Two': 'Два',
               'Three': 'Три',
               'Four': 'Четыре'}
    with open("text_file_04_RUS.txt", 'w', encoding='utf-8') as f_new:
        for line in f.readlines():
            for key, value in numbers.items():
                if re.search(key, line):
                    result = re.sub(key, value, line)
                    f_new.writelines(result)
