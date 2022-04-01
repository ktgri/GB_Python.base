# Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния
# (красный) составляет 7 секунд,
# второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep, time

start_time = time()


class TrafficLight:
    # атрибуты класса
    __color = ['красный', 'желтый', 'зеленый']

    # методы класса
    def running(self):
        switched_on = 'Светофор горит: '
        switches = 'светофор переключается на '
        while True:
            i = 0
            print(f'{switched_on}{self.__color[i]}\n'
                  f'{switches}{TrafficLight.__color[i + 1]}')
            sleep(7)
            print(f'{switched_on}{self.__color[i + 1]}\n'
                  f'{switches}{TrafficLight.__color[i + 2]}')
            sleep(2)
            print(f'{switched_on}{self.__color[i + 2]}\n'
                  f'{switches}{TrafficLight.__color[i]}')
            sleep(9)
            if time() - start_time > 36:
                print(f'Тестовая работа светофора завершена! {time() - start_time}')
                break


TrafficLight = TrafficLight()
TrafficLight.running()
