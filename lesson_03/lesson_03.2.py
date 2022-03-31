# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой

list_user_data = input(f'Введите через запятую:\nимя, фамилию, год рождения,'
                       f'город проживания, email, телефон: ').split(',')


def user_data(**kwargs):
    """ Принимает данные пользователя и выводит их на печать:
    имя, фамилия, год рождения, город проживания, email, телефон

    :param kwargs: именованные данные пользователя
    """
    # for key, value in kwargs.items():
    #     print(f'{key} : {value}')
    return kwargs


print(user_data(name=list_user_data[0],
                surname=list_user_data[1],
                year_of_birth=list_user_data[2],
                residence=list_user_data[3],
                email=list_user_data[4],
                phone=list_user_data[5]))
