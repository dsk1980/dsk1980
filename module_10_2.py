# Домашнее задание по теме "Потоки на классах".
# Задача "За честь и отвагу!".
import time
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.power = power
        self.name = name

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemies = 100
        days = 0
        while enemies > 0:
            time.sleep(1)
            days += 1
            enemies -= self.power
            if enemies < 0:
                enemies = 0
            print(f'{self.name}, сражается {days} день(дня)...,'
                  f'отсталось {enemies} войнов.')
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
two_knight = Knight("Sir Galahad", 20)
first_knight.start()
two_knight.start()
first_knight.join()
two_knight.join()
print("Все битвы закончились!!!")
