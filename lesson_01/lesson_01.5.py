# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.

revenue = int(input('Введите значение выручки: '))
costs = int(input('Введите значение издержек: '))

if revenue > costs:
    print('Ваш финансовый результат: \033[32mВы работаете в прибыль, поздравляем!')
elif revenue < costs:
    print('Ваш финансовый результат: \033[31mВы работаете в убыток! Есть над чем поработать')
else:
    print('Ваш финансовый результат: \033[34mВы работаете в ноль!')
