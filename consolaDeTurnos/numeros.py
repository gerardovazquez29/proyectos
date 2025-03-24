# Generador para números de perfumería
def numeros_perfumeria():
    # Genera números en el formato "p - <n>" desde 1 hasta 9999
    for n in range(1, 10000):
        yield f"P -{n}"

def numeros_farmacia():
    for n in range(1, 10000):
        yield f"F - {n}"

def numeros_cosmetica():
    for n in range(1, 10000):
        yield f"C - {n}"

P = numeros_perfumeria()
F = numeros_farmacia()
C = numeros_cosmetica()

# Función decoradora que imprime el número asignado según el rubro
def decorador(rubro):
     # Imprime un encabezado decorativo
    print("\n" + "*" * 23)
    print("Su numero es: ")
    # Determina el rubro y obtiene el siguiente número del generador correspondiente
    if rubro == "P":
        print(next(P))
    elif rubro == "F":
        print(next(F))
    else:
        print(next(C))
    print("Aguarde y sera atendido")
    print("*" * 23 + "\n")

