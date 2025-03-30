
import zipfile
import os


zip_path = 'D:\\programacion\\proyectos\\buscador_numeros\\Proyecto+Dia+9.zip'

if os.path.exists(zip_path):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_encontrado:
            zip_encontrado.extractall()
            print("Archivo descomprimido correctamente")
    except zipfile.BadZipFile:
        print("El archivo no es un zip valido")
else:
    print(f"Elarchivo '{zip_path}' ni se encontro")

