# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а
# также других данных, можно использовать любую подходящую структуру (например, словарь).

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
# указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.


class Storage:
    def __init__(self):
        self._spec = {}  # Спецификация позиций на складе
        self.items = 0  # Количество позиций на складе, в шт.

        self.shelf: int = 0  # Количество занятых полок, в шт.
        self.shelf_access: int = 7  # Количество доступных полок, в шт.
        self.tonnage: float = 10.2  # Максимальная нагрузка на полку, в кг
        self.capacity: float = 13.3  # Объем для коробок на полке, в м3
        self.spec_full: dict = self.access()  # Спецификация занятости полок (доступность по весу / объему)

    def access(self):
        self.spec_full = {}
        [self.spec_full.update({s: (self.tonnage, self.capacity)}) for s in range(1, self.shelf_access + 1)]
        return self.spec_full

    def fullness(self, box_weight, box_volume):
        if not self.shelf:
            self.shelf += 1
        if self.shelf < self.shelf_access:
            if self.spec_full.get(self.shelf)[0] >= box_weight and self.spec_full.get(self.shelf)[1] >= box_volume:
                self.spec_full.update({self.shelf: (self.spec_full.get(self.shelf)[0] - box_weight,
                                                    self.spec_full.get(self.shelf)[1] - box_volume)})
                self.items += 1
                return True
            else:
                self.shelf += 1
                if self.spec_full.get(self.shelf)[0] >= box_weight and self.spec_full.get(self.shelf)[1] >= box_volume:
                    self.spec_full.update({self.shelf: (self.spec_full.get(self.shelf)[0] - box_weight,
                                                        self.spec_full.get(self.shelf)[1] - box_volume)})
                    self.items += 1
                    return True
        else:
            return False

    def to_append(self, equipment):
        if self.fullness(equipment.box_weight, equipment.box_volume):
            self._spec.update({self.items: {'Тип': equipment.kind, 'Размер': equipment.box_volume,
                                            'Вес': equipment.box_weight, 'Цвет': equipment.color,
                                            'Год': equipment.year, 'Страна': equipment.country}})
            # print(f'Стоит на полке {self.shelf}. Общее к-во: {self.items}. '
            #       f'Свободно на полке (вес): {self.spec_full.get(self.shelf)}')
        else:
            print(f'Не удалось добавить {equipment.kind}. Склад заполнен!')
            for el in range(1, self.items):
                print(self._spec.get(el))
        # return self._spec


class Equipment:
    def __init__(self, kind, box_weight, box_volume, color, year, country):
        self.kind = kind
        self.box_weight = box_weight
        self.box_volume = box_volume
        self.color = color
        self.year = year
        self.country = country

    def name_of_kind(self):
        print(f'{self.kind}')

    def box(self):
        print(f'Коробка {self.kind}а весом {self.box_weight} кг и объемом {self.box_volume} м3')

    def manufactured(self):
        print(f'Цвет {self.kind}а - {self.color}. '
              f'{self.kind.title()} произведен в {self.year} году, страна- производитель - {self.country}.')

    @property
    def get_kind(self):
        return self.kind

    @property
    def get_box_volume(self):
        return self.box_volume

    @property
    def get_box_weight(self):
        return self.box_weight

    @property
    def get_color(self):
        return self.color

    @property
    def get_year(self):
        return self.year

    @property
    def get_country(self):
        return self.country

    @staticmethod
    def action():
        pass


class Printer(Equipment):
    def __init__(self, kind, box_volume, box_weight, color, year, country, model):
        super().__init__(kind, box_volume, box_weight, color, year, country)
        self.model = model

    @staticmethod
    def action():
        print('Печатает!')

    @property
    def get_model(self):
        return self.model


class Scanner(Printer):
    def __init__(self, kind, box_volume, box_weight, color, year, country, model, multicolor=True):
        super().__init__(kind, box_volume, box_weight, color, year, country, model)
        self.multicolor = multicolor

    @staticmethod
    def action():
        print('Сканирует!')


class Copier(Scanner):
    @staticmethod
    def action():
        print('Копирует!')


a = Equipment('принтер', 5, 5, 'white', 2000, 'Canada')
b = Equipment('сканер', 4, 5, 'black', 2010, 'Russia')
c = Equipment('принтер', 7, 9, 'желтый', 2011, 'China')
d = Scanner('сканер', 10, 10, 'синий', 1999, 'USA', 'WRC-4366')
e = Copier('копир', 9, 11, 'red', 2000, 'Canada', 'RFT-376', False)
f = Printer('принтер', 8.8, 12, 'white', 2003, 'China', 'REVX-86')


a.name_of_kind()
print(a.get_kind)
c.manufactured()
print(d.get_box_weight)
print(e.get_box_volume)
f.box()
f.action()

st = Storage()

st.to_append(a)
st.to_append(b)
st.to_append(c)
st.to_append(d)
st.to_append(e)
st.to_append(f)
st.to_append(d)
st.to_append(e)

st.to_append(f)
st.to_append(e)

print(st.items)
