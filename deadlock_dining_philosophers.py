import threading
from threading import Semaphore, Thread, Condition
from time import sleep
import random
import enum


class Status(enum.Enum):  # creating an enum structure for status of philosophers sitting around the table
    thinking = 1
    eating = 2


class IsReady(enum.Enum):  # creating an enum structure for status of philosophers sitting around the table
    ready = 0
    not_ready = 1


class Dining:
    def __init__(self, number_of_philosphers):
        self.philosphers = number_of_philosphers
        self.number_of_forks = number_of_philosphers
        self.forks = [threading.Semaphore(1) for i in range(number_of_philosphers)]
        self.sits = []


class Philosopher:
    def __init__(self, name, dining):
        self.name = name
        self.status = Status.thinking
        self.dining_table = dining
        self.position = len(self.dining_table.sits)
        self.dining_table.sits.append(self)
        self.right_hand = 0
        self.left_hand = 0
        self.hungry_coef = 50

    def take_fork(self):
        if self.right_hand != 0:
            self.dining_table.forks[self.position % 5].acquire()
            return IsReady.not_ready
        elif self.left_hand != 0:
            self.dining_table.forks[(self.position - 1) % 5].acquire()
            return IsReady.not_ready
        return IsReady.ready

    def eat_food(self):
        if self.right_hand and self.left_hand:
            self.status = Status.eating
            if self.hungry_coef != 0:
                self.hungry_coef -= 1
                return IsReady.not_ready
            return IsReady.ready
        else:
            return IsReady.not_ready

    def drop_forks(self):
        if self.right_hand and self.left_hand:
            self.dining_table.forks[self.position % 5].release()
            self.dining_table.forks[(self.position - 1) % 5].release()
            self.status = Status.thinking

    def sit_under_table(self):
        print(f'\r\nHello, I am {self.name}')  # introducing himself
        while (self.hungry_coef != 0) and (self.status == Status.thinking):
            self.take_fork()
            self.eat_food()
            self.drop_forks()
        print(f'I am full, thank you for dinner guys! :)')


if __name__ == "__main__":
    number_of_philosophers = 5
    names = ["Adam", "Wiesiek", "Zbigniew", "Jacek", "Bogus"]
    threads = []
    dining_table = Dining(number_of_philosphers=number_of_philosophers)
    for i in range(number_of_philosophers):
        Philosopher(names[i], dining_table)
    for i in range(5):
        print(i)
        threads.append(Thread(target=dining_table.sits[i].sit_under_table))
        threads[-1].start()
