import pygame
from simulation_engine import simulate, setup
import matplotlib.pyplot as plt

pygame.display.set_caption("Covid Simulation")
screen = pygame.display.set_mode((700, 700))
fps = 20

patient_image = pygame.transform.scale(pygame.image.load("clipart120469.png"), (6, 12))
recovered_image = pygame.transform.scale(pygame.image.load("clipart470308.png"), (4, 8))
normal_image = pygame.transform.scale(pygame.image.load("clipart194559.png"), (4, 8))
died_image = pygame.transform.scale(pygame.image.load("clipart-of-the-grey-human.png"), (5, 13))

maps = 100
prob = 0.1
initial = 100
population = 500

map1 = setup(maps, prob, initial, population)

#def draw_screen():
    #screen.fill((0, 0, 0))
    #simulation1 = simulate(map1, prob)[0]
    #for person in simulation1:
        #if person.active:
            #screen.blit(patient_image, (person.pixel_convert()[0], person.pixel_convert()[1]))
        #elif person.recovered == True:
            #screen.blit(recovered_image, (person.pixel_convert()[0], person.pixel_convert()[1]))
        #else:
            #screen.blit(normal_image, (person.pixel_convert()[0], person.pixel_convert()[1]))
    #pygame.display.update()

plt.axis([0, 300, 0, 1200])

def main():
    pygame.init()
    clock = pygame.time.Clock()
    running = True
    framecount = 0
    while running:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        if framecount % 1 == 0:
            simulate(map1)
            for person in map1.population:
                if person.active:
                    screen.blit(patient_image, (person.pixel_convert()[0], person.pixel_convert()[1]))
                elif person.recovered:
                    screen.blit(recovered_image, (person.pixel_convert()[0], person.pixel_convert()[1]))
                elif person.living == False:
                    screen.blit(died_image, (person.pixel_convert()[0], person.pixel_convert()[1]))
                else:
                    screen.blit(normal_image, (person.pixel_convert()[0], person.pixel_convert()[1]))
            pygame.display.update()

        framecount += 1

        #if frame %10 == 0:
            #plt.scatter(simulation1[1], frame)
            #plt.show()

        #frame += 1
        #draw_screen()

    pygame.quit()

if __name__ == "__main__":
    main()


