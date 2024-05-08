
acumulador = 0.0

contador = 0
division_actual = 1.0
essuma = True

while division_actual > 0.00052:
    contador +=1
    if contador % 2 !=0:
        if essuma:
            acumulador += 1/contador
        else:
            acumulador -= 1/contador
        essuma = not essuma
    division_actual = 1/contador

print("el cuarto del área es: ", acumulador)
pi = acumulador * 4
print("pi es igual a:",  pi)


