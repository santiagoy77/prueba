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
import sys
sys.path.append("C:/Users/maria/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages")
import openpyxl
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
    print("2- Consultar n videos con más views en un país, por categoría")
    print("3- Consultar video que más días ha sido trending en un país")
    print("4- Consultar video que más dias ha sido trending, por categoría")
    print("5- Consultar n videos con más likes en un país, por tag")
    print("0- Salir")


def initCatalog(chosenType):
    """
    Inicializa el catálogo de videos
    """
    return controller.initCatalog(chosenType)


def loadData(catalog):
    """
    Carga los videos en la estructura de datos
    """
    controller.loadData(catalog)


def printVideoInfo(video):
    """
    Imprime la información principal de un video
    """
    print("Título: " + video["title"])
    print("Canal: " + video["channel_title"])
    print("Fecha en que fue trending: " + video["trending_date"])
    print("País: " + video["country"])
    print("Cantidad de vistas: " + video["views"])
    print("Cantidad de Likes: " + video["likes"])
    print("Cantidad de Dislikes: " + video["dislikes"])


def printCategoriesList(catalog):
    "Imprime la lista de categorías"
    for category in lt.iterator(catalog['categories']):
        idpluscategory = category["id\tname"].split("\t ")
        print(idpluscategory[0], idpluscategory[1])


def printListMenu():
    """
    Imprime el menú para escoger en qué tipo de representación
    de lista se guardará el catálogo
    """
    print("Seleccione un tipo de lista para guardar el catálogo de videos:")
    print("0- ARRAY_LIST")
    print("1- LINKED_LIST")


def printAlgorithmMenu():
    """
    Imprime el menú para escoger el tipo de algoritmo de ordenamiento
    """
    print("Seleccione un tipo de algoritmo de ordenamiento:")
    # print("0- selection")
    # print("1- insertion")
    # print("2- shell")
    print("0- Merge")
    print("1- Quick")


def askForDataSize(catalog):
    """
    Pregunta al usuario el tamaño de la muestra a comparar y valida la cantidad
    """
    data_size = int(input("Tamaño de muestra de: "))
    if data_size > int(lt.size(catalog['videos'])):
        print("Error: valor excede tamaño de los datos cargados.")
        askForDataSize()
    else:
        return data_size


def firstReq(catalog, data_size, algorithm):
    """
    Solicita al controller la información del requerimiento 1
    """
    return controller.firstReq(catalog, data_size, algorithm)


catalog = None
"""
"""
# Menu principal

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        printListMenu()
        chosenType = int(input("Su selección (0 o 1) es: "))
        print("Cargando información de los archivos ....")
        catalog = initCatalog(chosenType)
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print("Información sobre el primer video cargado:\n")
        video = lt.firstElement(catalog["videos"])
        printVideoInfo(video)
        print("Las categorías cargadas y sus id son:")
        printCategoriesList(catalog)

    elif int(inputs[0]) == 2:
        # n_videos = int(input("Consultando los Top ? : "))
        data_size = askForDataSize(catalog)
        printAlgorithmMenu()
        algorithm = int(input("Su selección (0 o 1) es: "))
        result = firstReq(catalog, data_size, algorithm)
        for video in lt.iterator(result[0]):
            printVideoInfo(video)
        print("El tiempo de ejecución fue de: " + str(result[1]))
    else:
        sys.exit(0)
sys.exit(0)
