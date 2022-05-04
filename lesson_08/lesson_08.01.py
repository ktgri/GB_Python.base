# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Date:
    def __init__(self, date: str):
        self.date = date
        self._day, self._month, self._year = self.dd_mm_yyyy(date)
        self._leap = self._is_leap(self._year)

    @property
    def day(self):
        return self._day

    @property
    def month(self):
        return self._month

    @property
    def year(self):
        return self._year

    @property
    def leap(self):
        return self._leap

    @staticmethod
    def _is_leap(year):
        if not year % 4 and year % 100:
            return True
        elif not year % 400:
            return True
        else:
            return False

    @classmethod
    def dd_mm_yyyy(cls, date: str):
        if Date.validation_date(date):
            return tuple(map(int, date.split('-')))
        else:
            raise ValueError('Неверный формат даты!\nВведите в формате dd-mm-yyyy.')

    @staticmethod
    def validation_date(date: str):
        if len(date.split('-')) == 3:
            d, m, y = map(int, date.split('-'))
            if len(str(y)) == 4 and y in range(1500, 3001):
                if m in range(1, 13):
                    if m == 2 and (Date._is_leap(y) and d in range(1, 30))\
                            or (not Date._is_leap(y) and d in range(1, 29)):
                        print(f'Дата валидна: {d}-{m}-{y}.')
                        return True
                    elif ((m < 8 and m % 2) or (m > 7 and not m % 2)) and d in range(1, 32):
                        print(f'Дата валидна: {d}-{m}-{y}.')
                        return True
                    elif d in range(1, 31):
                        print(f'Дата валидна: {d}-{m}-{y}.')
                        return True
                    else:
                        print('Неверный формат даты! Укажите день от 1 до 31, в зависимости от месяца.')
                        return False
                else:
                    print('Неверный формат даты! Укажите месяц от 1 до 12.')
                    return False
            else:
                print('Неверный формат даты! Укажите год от 1500 до 3000.')
                return False
        else:
            print('Неверный формат даты!\nВведите в формате dd-mm-yyyy.')
            return False


d = Date('03-09-1906')
print(Date.dd_mm_yyyy('05-03-1666'))
Date.validation_date('28-02-2020')

print(d.day)
print(d.month)
print(d.year)
print(d.leap)

print(Date.dd_mm_yyyy('05-11-1666'))
Date.validation_date('30-02-2020')
