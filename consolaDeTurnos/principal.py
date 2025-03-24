
import numeros 

def preguntar():

    print("Bienvenido a Farmacia Python")

    # Bucle infinito hasta que el usuario ingrese una opción válida.
    while True:
        print("[p] - Perfumeria\n [f] - Farmacia\n [C] - Cosmetica")
        try:
            mi_rubro = input("Elija una opcion: ").upper() # Solicita una opción y la convierte a mayúsculas.
            ["P", "F", "C"].index(mi_rubro)  # Verifica si la opción ingresada está en la lista de opciones válidas.
        except ValueError:  # Si la opción no es válida, se captura la excepción.
            print("Esa no es una opcion valida")
        else:
            break # Si la opción es válida, se rompe el bucle.
    
    numeros.decorador(mi_rubro)
    # Llama a la función 'decorador' del módulo 'numeros' con la opción seleccionada.
    
def inicio():

    while True:
        preguntar()
        try:
            otro_turno = input("Quieres sacar otro turno? [S] [N]:").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opcion valida")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break

inicio()