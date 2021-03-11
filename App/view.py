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

default_limit = 1000
sys.setrecursionlimit(default_limit*10) 

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("\nBienvenido: ")
    print("1- Cargar informacion en el catalogo.")
    print('2- Ordenar los videos por views')
    print("3- Consultar buenos videos por categoria y pais.")
    print('4- Consultar video tendencia por pais.')
    print('5- Consultar video tendencia por categoria.')
    print('6- Consultar videos con mas likes.')
    print("0- Salir\n")

def printListOptions():
    print('Ingrese el numero del tipo de lista que desee: ')
    print(' 1. ARRAY_LIST.')
    print(' 2. LINKED LIST.')

def printSortMethods():
    print('Ingrese el numero del tipo de ordenamiento que desee: ')
    print(' 1. SELECTION_SORT.')
    print(' 2. INSERTION_SORT.')
    print(' 3. SHELL_SORT.')
    print(' 4. MERGE_SORT')
    print(' 5. QUICK_SORT')

def printResults(ord_videos, sample=10):
    size = lt.size(ord_videos)
    if size > sample:
        print("Los primeros ", sample, " videos ordenados son:")
        i=1
        while i <= sample:
            video = lt.getElement(ord_videos, i)
            print('Titulo: ' + video['title'] + ' Fecha de Tendencia: ' + video['trending_date'] + ' Vistas: ' + video['views'])
            i+=1

def printResultsReq2(filtered, pais, sample=10):
    size = lt.size(filtered)
    if size > sample:
        print("Los primeros ", sample, " videos en tendencia en " + pais + ' son: ')
        i=1
        while i <= sample:
            video = lt.getElement(filtered, i)
            print('Titulo: ' + video['title'] + ' |- Canal: ' + video['channel_title'] + ' |- Pais: ' + video['country'] + ' |- Dias en tendencia: ' + str(video['trending_days']))
            i+=1
    
def printResultsReq3(filtered, pais, sample=10):
    size = lt.size(filtered)
    if size > sample:
        print("Los primeros ", sample, " videos con mas likes en " + pais + ' son: ')
        i=1
        while i <= sample:
            video = lt.getElement(filtered, i)
            print('Titulo: ' + video['title'] + ' |- Canal: ' + video['channel_title'] + ' |- Publicación: ' + video['publish_time'] + ' |- Vistas: ' + video['views'] + ' |- Likes: ' + str(video['likes']) + ' |- Dislikes: ' + video['dislikes'] + ' |- Tags: ' + video['tags'])
            i+=1

def initCatalog(listType):
    'The catalog is initialized'
    return controller.initCatalog(listType)

def loadData(catalog):
    'Load the videos into the data structure'
    controller.loadData(catalog)

catalog = None

listType = None

'Menu principal'

while True:
    printMenu()
    inputs = input('Seleccione una opcion para continuar: ')

    # Option 1 Starts Here

    if int(inputs[0]) == 1:
        listSelection = False
        while listSelection == False:
            printListOptions()
            listTypeSelection = input('Opción seleccionada: ')
            if int(listTypeSelection[0]) == 1:
                listType = 'ARRAY_LIST'
                print('\nSeleciono ARRAY_LIST')
                input('Seleccion exitosa! Oprima ENTER para continuar...')
                listSelection = True
            elif int(listTypeSelection[0]) == 2:
                listType = 'SINGLE_LINKED'
                print('\nSeleciono LINKED_LIST')
                input('Seleccion exitosa! Oprima ENTER para continuar...')
                listSelection = True
            else:
                input('\nSeleccion Erronea! Oprima ENTER para continuar...')
        print("Cargando información de los archivos...\n")
        catalog = initCatalog(listType)
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print('Categorias cargados: ' + str(lt.size(catalog['categories'])))
        #print(print(catalog['videos']['elements']),'\n')
    
    #Option 1 Ends Here
    #------------------------
    #Option 2 Starts Here

    elif int(inputs[0]) == 2:
        size = input("Indique tamaño de la muestra: ")
        sortSelection = False
        while sortSelection == False:
            printSortMethods()
            sortTypeSelection = input('Opción seleccionada: ')
            if int(sortTypeSelection[0]) == 1:
                sortType = 'sls'
                print('\nSeleciono SELECTION_SORT')
                input('Seleccion exitosa! Oprima ENTER para continuar...')
                sortSelection = True
            elif int(sortTypeSelection[0]) == 2:
                sortType = 'ins'
                print('\nSeleciono INSERTION_SORT')
                input('Seleccion exitosa! Oprima ENTER para continuar...')
                sortSelection = True
            elif int(sortTypeSelection[0]) == 3:
                sortType = 'shl'
                print('\nSeleciono SHELL_SORT')
                input('Seleccion exitosa! Oprima ENTER para continuar...')
                sortSelection = True
            elif int(sortTypeSelection[0]) == 4:
                sortType = 'mgs'
                print('\nSeleciono MERGE_SORT')
                input('Seleccion exitosa! Oprima ENTER para continuar...')
                sortSelection = True
            elif int(sortTypeSelection[0]) == 5:
                sortType = 'qks'
                print('\nSeleciono QUICK_SORT')
                input('Seleccion exitosa! Oprima ENTER para continuar...')
                sortSelection = True
            else:
                input('\nSeleccion Erronea! Oprima ENTER para continuar...')

        result = controller.sortVideos(catalog, int(size), sortType)
        print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ", str(result[0]))
        printResults(result[1])

    #Options 2 Ends Here
    #------------------------
    #Options 3 Starts Here
    
    elif int(inputs[0]) == 3:
        pass

    #Options 3 Ends Here
    #------------------------
    #Options 4 Starts Here

    elif int(inputs[0]) == 4:
        pais = input('Ingrese el pais deseado: ')
        trendingVideos = controller.videosCountry(catalog, pais)
        wantSee = int(input('Ingrese el numerdo de videos que desea ver: '))
        trendingVideosDays = controller.videosCountryTrendingResumed(trendingVideos)
        printResultsReq2(trendingVideosDays, pais, wantSee)

    #Options 4 Ends Here
    #------------------------
    #Options 5 Starts Here

    elif int(inputs[0]) == 5:
        pass

    #Options 5 Ends Here
    #------------------------
    #Options 6 Starts Here

    elif int(inputs[0]) == 6:
        pais = input('Ingrese el pais deseado: ')
        tag = input('Ingrese el tag deseado: ')
        wantSee = int(input('Ingrese el numero de videos que desea ver: '))
        videosLikesCountryTags = controller.videosLikesCountryTags(catalog, pais, tag)
        printResultsReq3(videosLikesCountryTags, pais, wantSee)
    #Options 6 Ends Here
    #------------------------

    else:
        sys.exit(0)
sys.exit(0)
