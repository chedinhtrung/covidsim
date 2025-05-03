import random

class Person:
    def __init__(self, active=False, recovered=False, x=0, y=0, time=0, limit=0, living=True, pixel=0):
        self.active = active
        self.recovered = recovered
        self.x = x
        self.y = y
        self.time = time
        self.limit = limit
        self.living = living
        self.pixel = pixel
        
    def infect(self):
        self.active = True
        self.recovered = False

    def recover(self):
        self.active = False
        self.recovered = True

    def move(self, check):
        while True:
            x = random.randint(self.x - 5, self.x + 5)
            y = random.randint(self.y - 5, self.y + 5)
            if 0 < x < self.limit and 0 < y < self.limit and check.map[x][y] == 0:
                check.map[self.x][self.y] = 0
                i = check.population.index(self)
                self.x = x
                self.y = y
                check.map[x][y] = self
                check.population[i] = self
                break
            else:
                break

    def die(self, map1):
        self.living = False
        map1.map[self.x][self.y] = 0
        self.active = False
        map1.active.remove(self)

    def pixel_convert(self):
        pixel_x = int(self.x * 6 + 25)
        pixel_y = int(self.y * 6 + 25)
        return pixel_x, pixel_y


class Space:

    def __init__(self, size=0, prob=0, active=None, population=None, m=None, measures=False, recovered=0, death=0, total=0):
        self.size = size
        self.active = active
        self.population = population
        self.map = m
        self.measures = measures
        self.prob = prob
        self.death = death
        self.recovered = recovered
        self.total = total

    def spawn(self):
        self.active = []
        self.population = []
        self.map = []
        for i in range(0, self.size):
            f = []
            for j in range(0, self.size):
                f.append(0)
            self.map.append(f)

    def add_initial_patient(self):
        while True:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if self.map[x][y] == 0:
                p = Person(True, False, x, y, 0, self.size)
                self.map[p.x][p.y] = p
                self.active.append(p)
                self.population.append(p)
                break

    def add_person(self):
        while True:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if self.map[x][y] == 0:
                p1 = Person(False, False, x, y, 0, self.size)
                self.map[p1.x][p1.y] = p1
                self.population.append(p1)
                break




