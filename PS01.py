import math

def area_rectángulo (base, altura):
    return base * altura

def area_circulo(radio):
    return math.pi * (radio ** 2)

def area_triangulo(base, altura):
    return (base * altura)/2

def menu():
    print("Bienvenido al programa de cálculo de áreas")
    print("Seleccione una opción")
    print("a) Calcular área de un rectángulo")
    print("b) Calcular área de un círculo")
    print("c) Calcular área de un triángulo")
    print("d) Salir del programa")

def main():
    while True:
        menu()
        opcion=input("Ingrese su opción: ").lower()

        if opcion== "a":
            base= float(input("Ingresa la base del rectángulo: "))
            altura= float(input("Ingresa la altura del rectángulo: "))
            print("El área del rectángulo es: ", area_rectángulo(base,altura))
        elif opcion== "b":
            radio= float(input("Ingresa el radio del círculo: "))
            print("El área del círculo es: ", area_circulo(radio))
        elif opcion=="c":
            base= float(input("Ingresa la base del triángulo: "))
            altura= float(input("Ingresa la altura del triángulo: "))
            print("El área del triángulo es: ", area_triangulo(base, altura))

        elif opcion=="d":
            print ("Adiós.")
            break
        else:
            print("Opción no válida. Selecciona otra opción:")

if __name__ == "__main__":
    main ()