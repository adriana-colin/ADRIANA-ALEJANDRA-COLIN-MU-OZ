#Calculo de pi por el Método de Monte Carlo 
import random
import math

cuantos = 100000
cuantossi = 0

for i in range(cuantos):
    x = random.random()
    y = random.random()

    y_calculada = math.sqrt(1-x*x)
    if y > y_calculada:
        None
    else:
        cuantossi += 1

cuarto_area = float(cuantossi) / float(cuantos)

print("el cuarto del área es: ", cuarto_area)
pi = cuarto_area * 4
print("pi es igual a:",  pi)

