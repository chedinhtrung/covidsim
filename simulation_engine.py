from control import Person
import random


def setup(mapsize, prob, initial, population):
    from control import Space
    # maps = int(input("map size"))
    # prob = float(input("probabilty"))
    # initial = int(input("intitial patients"))
    # population = int(input("population"))
    map1 = Space(mapsize, prob)
    map1.spawn()

    for i in range(0, initial):
        map1.add_initial_patient()

    for i in range(0, population - len(map1.active)):
        map1.add_person()
    map1.population.extend(map1.active)
    return map1


def simulate(map1):
    for p in map1.active:
        for x in range(p.x - 2, p.x + 2):
            if x != p.x:
                try:
                    for y in range(p.y - 2, p.y + 2):
                        if y != p.y:
                            try:
                                if type(map1.map[x][y]) == Person and map1.map[x][y].active == False and map1.map[x][y].recovered == False:
                                    r = random.randint(1, 100)
                                    if r <= 100 * map1.prob:
                                        map1.population.remove(map1.map[x][y])
                                        map1.map[x][y].infect()
                                        map1.active.append(map1.map[x][y])
                                        map1.population.append(map1.map[x][y])
                                        map1.total += 1
                            except IndexError:
                                pass
                except IndexError:
                    pass

    for patient in map1.active:
        patient.time += 1
        if patient.time == 40:
            mortality = random.randint(1, 1000)
            if mortality <= 6:
                patient.die(map1)
                map1.death += 1
            else:
                patient.recover()
                patient.time = 0
                map1.active.remove(patient)
                map1.recovered += 1

    for p in map1.population:
        if p.living == True:
            p.move(map1)

    if len(map1.active) >= 0.1* len(map1.population) and map1.measures == False:
        map1.measures = True
        map1.prob = map1.prob * 0.8

    elif len(map1.active) < 0.1 * len(map1.population) and map1.measures == True:
        map1.measures = False
        map1.prob = map1.prob / 0.8

    return map1.population, len(map1.active), map1.death, map1.recovered, map1.total

    #return np.array(patientset), np.array(frameset)
    #patients = np.array(patientset)
    #time = np.array(frameset)
    #plt.plot(time, patients)
    #plt.show()

