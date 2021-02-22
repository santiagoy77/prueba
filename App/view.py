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
    print("2- Ordenar el catálogo con un algoritmo iterativo")
    print("2- Encontrar buenos videos por categoría y país")
    print("4- Encontrar video tendencia por país ")
    print("5- Encontrar video tendencia por categoría")
    print("6- Buscar los videos con más likes")
    print("0- Salir")

def initCatalogArray():
    """
    Inicializa el catalogo de videos
    """
    return controller.initCatalogArray()

def initCatalogSingleLinked():
    """
    Inicializa el catalogo de videos
    """
    return controller.initCatalogSingleLinked()

def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)


catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print('Tipos de estructuras de datos disponibles:\n1. Lista encadenada\n2. Arreglo')
        dataType = int(input('Seleccione el tipo de estructura de datos con el que desea cargar la información\n'))
        print("Cargando información de los archivos ....")
        if dataType == 1:
            catalog = initCatalogSingleLinked()
            loadData(catalog)
            print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        elif dataType == 2:
            catalog = initCatalogArray()
            loadData(catalog)
            print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        else:
            print('Ingrese una opcion valida')
        

    elif int(inputs[0]) == 2:
        print('Los tipos de algorritmos de ordenamiento disponibles son los siguientes:\n1. Selection Sort\n2. Insertion Sort\n3. Shell Sort')
        algorithm = int(input('Sleccione el tipo de algoritmo que desea utilizar para ordenar los datos:\n'))
        print('Ordenando los datos...')
        if algorithm == 1:
            size = input("Indique tamaño de la muestra: ")
            result = controller.selectionSortVideoscatalog(catalog, int(size))
            print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ", str(result[0]))
        elif algorithm ==2:
            size = input("Indique tamaño de la muestra: ")
            result = controller.insertionSortVideoscatalog(catalog, int(size))
            print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ", str(result[0]))
        elif algorithm ==3:
            size = input("Indique tamaño de la muestra: ")
            result = controller.shellSortVideoscatalog(catalog, int(size))
            print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ", str(result[0]))
        else:
            print('Ingrese una opcion valida')
        

    else:
        sys.exit(0)
sys.exit(0)

