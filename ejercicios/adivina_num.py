
# Adivina un numero del 1 al 100

import random

def jugar_adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("Bienvenido a 'Adivina el numero'!")
    print("Estoy pensando en un numero entre 1 y 100. Adivina!")

    while True:
        intento = int(input("Ingresa un numero: "))
        intentos += 1

        if intento < numero_secreto:
            print("Demaciado bajo Intentalo de nuevo!")
        elif intento > numero_secreto:
            print("Demaciado alto Intentalo de nuevo!")
        else:
            print(f"Felicidades! Adivinaste el numero en {intentos} intentos ")
            break

if __name__ == "__main__":
    jugar_adivina_el_numero()
