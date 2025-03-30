import re
import os
import time
import datetime
from pathlib import Path
import math

inicio = time.time()

ruta = 'D:\\programacion\\proyectos\\Mi_Gran_Directorio'
mi_patron = r'N\D{3}-\d{5}'
hoy = datetime.date.today()
numeros_encontrados = []
archivos_encontrados = []

def buscar_numero(archivo, patron):
    try:   
        # Verifica si el archivo existe y es un archivo válido
        if not Path(archivo).is_file():
            print(f"Advertencia:{archivo} no es un archivo valido")
            return ''
        # Abre el archivo de forma segura
        with open(archivo, 'r',encoding='utf-8', errors='ignore') as este_archivo:
            texto = este_archivo.read()
            # Busca el patrón en el texto
        if re.search(patron, texto):
            return re.search(patron, texto)
        else:
            return ''
    except Exception as e:
         # Maneja cualquier error que ocurra al abrir o leer el archivo
        print(f"Error al procesar el archivo {archivo}: {e}")
        return ''
    
def crear_listas():
    try:
        for carpeta, subcarpeta, archivo in os.walk(ruta):
            for a in archivo:
                resultado = buscar_numero(Path(carpeta, a), mi_patron)
                if resultado != '':
                    numeros_encontrados.append(resultado.group())
                    archivos_encontrados.append(a.title())
    except Exception as e:
        # Maneja errores generales en el recorrido de directorios
        print(f"Error al recorrer la ruta {ruta}: {e}")

def mostrar_todo():
    indice = 0
    print('-' * 50)
    print(f"Fecha de Busqueda: {hoy.day}/{hoy.month}/{hoy.year}")
    print('\n')
    print('ARCHIVO\t\t\tNRO. SERIE')
    print('----------\t\t\t----------')
    for a in archivos_encontrados:
        print(f"{a}\t{numeros_encontrados[indice]}")
        indice += 1
    print('\n')
    print(f"Numeros encontrados: {len(numeros_encontrados)}")
    fin = time.time()
    duracion = fin - inicio
    print(f"Duracion de la busqueda: {math.ceil(duracion)} segundos")
    print('-' * 50)

crear_listas()
mostrar_todo()

"""

--------------------------------------------------
Fecha de Busqueda: 29/3/2025


ARCHIVO                 NRO. SERIE        
----------                      ----------
Archivo3.Txt    Nhjn-54885
Archivo9.Txt    Nlkj-41523
Archivo11.Txt   Nann-74705
Archivo13.Txt   Nqqs-82506
Archivo16.Txt   Nopp-10052
Archivo17.Txt   Nmrn-20155
Archivo20.Txt   Njko-60603
Archivo26.Txt   Nbbg-90999
Archivo34.Txt   Nwwe-88985
Archivo38.Txt   Naac-11022
Archivo40.Txt   Nerp-66532


Numeros encontrados: 11
Duracion de la busqueda: 1 segundos
--------------------------------------------------
"""
