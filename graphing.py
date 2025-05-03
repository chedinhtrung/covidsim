from simulation_engine import setup, simulate
import matplotlib.pyplot as plt

mapsize = 120
prob = 0.08
initial = 10
population = 3000

frame = 0

frame_array = []
active_patient_array = []
recovered_array = []
death_array = []
total_array = []

map1 = setup(mapsize, prob, initial, population)

for frame in range(0, 500):
    simulation1 = simulate(map1)

    frame_array.append(frame)
    active_patient_array.append(simulation1[1])
    recovered_array.append(simulation1[3])
    death_array.append(simulation1[2])
    total_array.append(simulation1[4])

plt.plot(frame_array, active_patient_array, color='red')
plt.plot(frame_array, recovered_array, color='green')
plt.plot(frame_array, death_array, color='grey')
plt.plot(frame_array, total_array, color="blue")
plt.show()
