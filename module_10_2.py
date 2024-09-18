from threading import Thread
import time


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        warrior = 100
        day = 0
        print(f'{self.name}, на нас напали!')
        while warrior > 0:
            day += 1
            warrior -= self.power
            print(f'{self.name} сражается {day} день(дня)..., осталось {warrior} воинов.')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {day} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()



