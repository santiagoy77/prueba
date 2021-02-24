"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Encontrar buenos videos por categoría y país (Grupal)")
    print("3- Encontrar video tendencia por país ")
    print("4- Encontrar video tendencia por categoría")
    print("5- Buscar los videos con más Likes")
    print("0- Salir")

def initCatalog():
    """
    Inicializa el catalogo de videos
    """
    return controller.initCreate_videos()

def initTags():
    tags=controller.initLista_tags()
    for a in tags["elements"]:
        print (a[0],"  ",a[1])

def printMostViewed(ord_videos, sample= 10):
    size = lt.size(ord_videos)
    if size <= sample:
        sample = size
    print('\n\n\n Videos más vistos: ')
    print("trending date","title", "channel", "publish time", "views", "likes", "dislikes", sep="   ")
    i = 1
    while sample >= i:
        dir=ord_videos["elements"][-i][0]["elements"]
        print(dir[1],dir[2], dir[3], dir[5], dir[6], dir[7], dir[8], sep="   ")
        i+=1
    

catalog = None
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("\nCargando información de los archivos ....")
        catalog= initCatalog()
        dir=catalog["elements"][0][0]["elements"]
        print("Se han cargado " , lt.size(catalog), "registros de videos")
        print("\nPrimer video: ",dir[2])
        print("Canal: ", dir[3])
        print("Fecha de tendencia: ",dir[1])
        print("País: ",dir[-1])
        print("vistas: ",dir[6])
        print("Likes: ",dir[7])
        print("Dislikes: ",dir[8],"\n")
        print("Id  Nombre")
        initTags()
        
    elif int(inputs[0]) == 2:
        size = int(input("Introduzca el tamaño de la muestra que quiere ordenar: "))
        print("1. ShellSort\n2.InsertionSort\n3.SelectionSort")
        algorithm = int(input("Introduzca el índice del algoritmo que quiere usar: "))
        if (algorithm == 1):
            algorithm = 'shell'
        elif(algorithm == 2):
            algorithm = 'insertion'
        else:
            algorithm = 'selection'
        sample = int(input("Introduzca el número de vídeos que quiere listar: "))
        result = controller.order_by_Views(catalog, size, algorithm)
        print("El tiempo de ordenamiento fue de",result[0],"ms.")
        printMostViewed(result[1], sample=sample)
        input("Presione cualquier tecla para continuar.")
    elif int(inputs[0]) == 3:
        pass

    elif int(inputs[0]) == 4:
        pass

    elif int(inputs[0]) == 5:
        pass

    else:
        sys.exit(0)
sys.exit(0)
