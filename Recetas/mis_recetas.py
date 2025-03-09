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



inicio()


menu = 0

if menu == 1:
    # mostrar categorias
    # elegir categoria
    # mostrar recetas
    # elegir recetas
    # leer receta
    # volver inicio
    pass
elif menu == 2:
    # mostrar categorias
    # elegir categorias
    # crear receta nueva
    # volver inicio
    pass
elif menu == 3:
    # crear categoria
    # volver inicio
    pass
elif menu == 4:
    # mostrar categorias
    # elegir categoria
    # mostrar recetas
    # elegir recetas
    # eliminar receta
    # volver inicio
    pass
elif menu == 5:
    # mostrar categorias
    # elegir categoria
    # eliminar categoria
    # volver inicio
    pass
elif menu == 6:
    # finalizar programa
    pass
