from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.day = 0
        self.enemies = 100


    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemies > 0:
            self.day += 1
            self.enemies -=self.power
            print(f"{self.name} сражается {self.day}, осталось {self.enemies} воинов.")
            sleep(1)
        print(f"{self.name} одержал победу спустя {self.day} дней(дня)!")




# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print("Все битвы закончились!")