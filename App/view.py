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

import copy
import sys
from os import X_OK
import config as cf
import controller
import model
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from prettytable import PrettyTable
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

# Selector para identificar el nombre del algoritmo
algo_sel = {1: 'insertion', 2: 'shell', 3: 'merge', 4: 'quick'}

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronológicamente los artistas por un rango de años")
    print("3- Listar cronológicamente las adquisiciones")
    print("4- Clasificar las obras de un artista por técnica")
    print("5- Calcular costo de transportar obras de un departamento")
    print("6- Salir del programa")

def printListOptions():
    print("Seleccione la implementación de las listas del catálogo")
    print("1- ARRAY_LIST")
    print("2- SINGLE_LINKED")

def printSortOptions():
    print("Seleccione con qué tipo de implementación desea organizar la lista")
    print("1- Insertion")
    print("2- Shell")
    print("3- Merge")
    print("4- Quick")

def initCatalog(implementation):
    """
    Inicia el catálogo de obras
    """
    return controller.initCatalog(implementation)

def loadData(catalog):
    """
    Carga las obras en la estructura de datos
    """
    controller.loadData(catalog)

def sortArtistsByBeginDate(catalog, implementation, initial_date, end_date):
    """
    Ordena los artistas en el rango de fechas dispuesto
    """
    return controller.sortArtistsByBeginDate(catalog, implementation, initial_date, end_date)

def selectSample(catalog, sample):
    """
    Selecciona una muestra de los datos de la longitud que indique el parámetro sample
    """
    return controller.selectSample(catalog, sample)

def sortArtworksByDate(catalog, implementation, initial_date, end_date):
    """
    Ordena las obras en el rango de fechas dispuesto
    """
    return controller.sortArtworksByDate(catalog, implementation, initial_date, end_date)

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    
    if int(inputs[0]) == 1:

        printListOptions()
        option = input("Seleccione una opción para continuar\n")
        print("Cargando información de los archivos ....")
        
        catalog = initCatalog(option)
        loadData(catalog)

        num_artists = lt.size(catalog["artists"])
        num_artworks = lt.size(catalog["artworks"])

        print(f"{num_artists} artistas cargados.")
        print(f"Hay {num_artworks} obras en total.")
        
    elif int(inputs[0]) == 2:

        printSortOptions()
        option = input("Seleccione una opción para continuar\n")
        
        initial_year = input("Digite el año inicial:\n")
        end_year = input("Digite el año final:\n")

        time, sorted_artists = sortArtistsByBeginDate(catalog, option, initial_year, end_year)
        size = lt.size(sorted_artists)

        print(f"{size} artists were loaded.")
        print(f"Tiempo del algoritmo {algo_sel[int(option)]} es {time} milisegundos.")


    elif int(inputs[0]) == 3:

        sample = input("Digite el tamaño que desea de la muestra\nEn caso de que digite un número que sobrepase de alguna u otra manera el los límites del arreglo, el catálogo quedará intacto.\n")
        catalog["artworks"] = selectSample(catalog, sample)

        printSortOptions()
        option = input("Seleccione una opción para continuar\n")

        initial_date = input("Digite el año, mes y día inicial en el formato AAAA-MM-DD:\n")
        end_date = input("Digite el año, mes y día final en el formato AAAA-MM-DD:\n")

        time, sorted_artworks = sortArtworksByDate(catalog, option, initial_date, end_date)
        size = lt.size(sorted_artworks)

        print(f"Hay {size} obras en este rango.")
        print(f"Tiempo del algoritmo {algo_sel[int(option)]} es {time} milisegundos.")

    elif int(inputs[0]) == 4:

        artistname= input("Digite el nombre del artista a examinar: ")
        respuestas= controller.getArtworksByArtist(catalog, artistname)
        print("El número de obras del artista es de: ", lt.getElement(respuestas, 1))
        print()
        print("Las técnicas utilizadas son: ")
        estilos= lt.getElement(respuestas, 2)
        for x in estilos:
            print(x, ":", estilos[x], end="\n")
        print()
        print("La técnica más utilizada fue: ", lt.getElement(respuestas, 3))
        print()
        print("Una muestra de tres obras con la técnica más utilizada: ")
        print()
        lista_obras= lt.getElement(respuestas, 4)
        for x in lt.iterator(lista_obras):
            print("Título:", x["Title"],"| Fecha de la obra:", x["Date"], "| Medio:", x["Medium"], "| Dimensiones:", x["Dimensions"], end= "\n")

    elif int(inputs[0]) == 5:

        departamento= input("Digite el departamento del cual desea transportar TODAS sus obras: ")
        respuestas= controller.transportar_obras(departamento, catalog)
        print("===================== Req No. 5 Inputs =====================\n")
        print(f"Estimate all the cost to transport all artifacts in {departamento} Moma's Department")
        print("\n===================== Req No. 5 Answer =====================")
        print(f"The MoMa is going to transport {lt.getElement(respuestas, 1)} artifacts from the {departamento}")
        print(f"Estimated cargo weight (kg): {lt.getElement(respuestas, 3)}")
        print(f"Estimated cargo cost: {lt.getElement(respuestas, 2)}")
        x= 1
        print("Top 5 most expensive cargo: ")
        for artworks in lt.iterator(lt.getElement(respuestas, 5)):
            print("===========================================================")
            print(f"ObjectID: ", artworks["ObjectID"])
            print(f"Title: ", artworks["Title"])
            print(f"Artists ConstituentID: ", artworks["ConstituentID"])
            print(f"Medium: ", artworks["Medium"])
            print(f"Date: ", artworks["Date"])
            print(f"Dimensions: ", artworks["Dimensions"])
            print(f"Classification: ", artworks["Classification"])
            print(f"Transportation Cost (USD): ", artworks["prize"])
            print(f"URL: ", artworks["URL"])
            print("===========================================================")
            x+=1
            if(x == 6):
                break
        x= 1
        print("Top 5 oldest items to transport: ")
        for artworks in lt.iterator(lt.getElement(respuestas, 4)):
            print("===========================================================")
            print(f"ObjectID: ", artworks["ObjectID"])
            print(f"Title: ", artworks["Title"])
            print(f"Artists ConstituentID: ", artworks["ConstituentID"])
            print(f"Medium: ", artworks["Medium"])
            print(f"Date: ", artworks["Date"])
            print(f"Dimensions: ", artworks["Dimensions"])
            print(f"Classification: ", artworks["Classification"])
            print(f"Transportation Cost (USD): ", artworks["prize"])
            print(f"URL: ", artworks["URL"])
            print("===========================================================")
            x+=1
            if(x == 6):
                break
    else:
        sys.exit(0)
