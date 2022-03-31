# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open("text_file_05_sum.txt", 'w', encoding='utf-8') as f:
    numbers = input('Введите набор чисел, разделённых пробелами: ')
    f.writelines(numbers)
    sum_numbers = []
    for n in numbers.split(' '):
        n = float(n)
        sum_numbers.append(n)
    f.writelines(f'\nСумма чисел = {str(sum(sum_numbers))}\n')
