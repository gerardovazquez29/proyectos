import os 
from pathlib import Path
from os import system


mi_ruta = Path("Recetas")

def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador


# menu de inicio

def inicio():
    system('cls')
    print('*'*50)
    print('*'*5 + "Bienvenido al administrador de recetas" + '*'*5)
    print('*'*50)
    print('\n')
    print(f"Las recetas se encuentran en {mi_ruta}")
    print(f"Total recetas: {contar_recetas(mi_ruta)}")

    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1, 7 ):
        print("Elige una opcion: ")
        print('''
        [1] -Leer receta
        [2] - Crear receta nueva
        [3] - Crear categoria nueva
        [4] - Eliminar receta
        [5] - Eliminar categoria
        [6] - Salir del programa''')
        eleccion_menu = input()
    return (eleccion_menu)

def mostrar_categorias(ruta):
    print("categorias:")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1


    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador += 1
    
    return lista_categorias

def elegir_categoria(lista):
    eleccion_correcta = 'x'

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input("\n Elije una categoria: ")

    return lista[int(eleccion_correcta) - 1]

def mostrar_recetas(ruta):
    print("Recetas: ")
    ruta_recetas = Path(ruta)
    lista_receta = []
    contador = 1

    for receta in ruta_recetas.glob('*.txt'):
       receta_str = str(receta.name)
       print(f"[{contador}] - {receta_str}")
       lista_receta.append(receta)
       contador += 1
    return lista_receta 

def elegir_recetas(lista):
    eleccion_receta = 'x'

    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) + 1):
        eleccion_receta = input("\nElije una receta: ")
    return lista[int(eleccion_receta) - 1]
    

menu = 0

if menu == 1:
    # mostrar categorias
    mis_categorias = mostrar_categorias(mi_ruta)
    # elegir categoria
    mi_categoria = elegir_categoria(mis_categorias)
    # mostrar recetas
    mis_recetas = mostrar_recetas(mi_categoria)
    # elegir recetas
    mi_receta = elegir_recetas(mis_recetas)
    # leer receta
    # volver inicio
    pass
elif menu == 2:
    # mostrar categorias
    mis_categorias = mostrar_categorias(mi_ruta)
    # elegir categorias
    mi_categoria = elegir_categoria(mis_categorias)
    # crear receta nueva
    # volver inicio
    pass
elif menu == 3:
    # crear categoria
    # volver inicio
    pass
elif menu == 4:
    # mostrar categorias
    mis_categorias = mostrar_categorias(mi_ruta)
    # elegir categoria
    mi_categoria = elegir_categoria(mis_categorias)
    # mostrar recetas
    mis_recetas = mostrar_recetas(mi_categoria)
    # elegir recetas
    mi_receta = elegir_recetas(mis_recetas)
    # eliminar receta
    # volver inicio
    pass
elif menu == 5:
    # mostrar categorias
    mis_categorias = mostrar_categorias(mi_ruta)
    # elegir categoria
    mi_categoria = elegir_categoria(mis_categorias)
    # eliminar categoria
    # volver inicio
    pass
elif menu == 6:
    # finalizar programa
    pass
