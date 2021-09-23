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
    print("\n")
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2 (Req. 1)- Listar cronológicamente los artistas por un rango de años")
    print("3 (Req. 2)- Listar cronológicamente las adquisiciones")
    print("4 (Req. 3)- Clasificar las obras de un artista por técnica")
    print("5 (Req. 4)- Clasificar las obras por la nacionalidad de sus creadores")
    print("6 (Req. 5)- Transportar obras de un departamento")
    print("7 (Req. 6)- Proponer una nueva exposición en el museo")
    print("Digite cualquier otra tecla para salir del programa")
    print("\n")

def printListOptions():
    print("\n")
    print("Seleccione la implementación de las listas del catálogo")
    print("1- ARRAY_LIST")
    print("2- SINGLE_LINKED")
    print("\n")


def printSortOptions():
    print("\n\n")
    print("Seleccione con qué tipo de implementación desea organizar la lista")
    print("1- Insertion")
    print("2- Shell")
    print("3- Merge")
    print("4- Quick")
    print("\n")

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

def calculateArea(artist):
    return controller.area(artist)

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

def countNationalities(catalog):
    """
    Cuenta el número de obras por la nacionalidad de los artistas
    """
    return controller.countNationalities(catalog)

def showNationWork(catalog, nation_count):
    """
    Retorna la información de la nación con un mayor número de obras
    """
    return controller.showNationWork(catalog, nation_count)

def selectArtworks(catalog, years, area):
    """
    Selecciona unas obras de arte entre los años pasados por parámetro hasta que se llene el área disponible
    """
    return controller.selectArtworks(catalog, years, area)

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

        print("\n")
        print(f"{num_artists} artistas cargados.")
        print(f"Hay {num_artworks} obras en total.")
        
    elif int(inputs[0]) == 2:

        printSortOptions()
        option = input("Seleccione una opción para continuar\n")
        
        initial_year = input("Digite el año inicial:\n")
        end_year = input("Digite el año final:\n")

        time, sorted_artists = sortArtistsByBeginDate(catalog, option, initial_year, end_year)
        size = lt.size(sorted_artists)

        first_three = lt.subList(sorted_artists, 1, 3)
        last_three = lt.subList(sorted_artists, lt.size(sorted_artists) - 3, 3)
        new_artists = lt.newList()
        for element in lt.iterator(first_three):
            lt.addLast(new_artists, element)
        for element in lt.iterator(last_three):
            lt.addLast(new_artists, element)

        print("===================== Req No. 1 Inputs =====================\n")
        print(f"Artist born between {initial_year} and {end_year}")
        print("\n===================== Req No. 1 Answer =====================")
        print(f"There are {size} artists born between {initial_year} and {end_year}")
        print("The first and last 3 artists in range are...")
        req2 = PrettyTable()
        req2.field_names = ["ConstituentID", "DisplayName", "BeginDate", "Nationality", "Gender", "ArtistBio", "Wiki QID", "ULAN"]
        for artist in lt.iterator(new_artists):
            ide = artist["ConstituentID"]
            name = artist["DisplayName"]
            born = artist["BeginDate"]
            nation = artist["Nationality"]
            gender = artist["Gender"]
            bio = artist["ArtistBio"]
            wiki = artist["Wiki QID"]
            ulan = artist["ULAN"]
            req2.add_row([ide, name, born, nation, gender, bio, wiki, ulan])
        print(f"{req2}\n\n")
        
        

        print(f"Algorithm {algo_sel[int(option)]} took: {time} ms.")


    elif int(inputs[0]) == 3:

        sample = input("Digite el tamaño que desea de la muestra\nEn caso de que digite un número que sobrepase de alguna u otra manera el los límites del arreglo, el catálogo quedará intacto.\n")
        catalog["artworks"] = selectSample(catalog, sample)

        printSortOptions()
        option = input("Seleccione una opción para continuar\n")

        initial_date = input("Digite el año, mes y día inicial en el formato AAAA-MM-DD:\n")
        end_date = input("Digite el año, mes y día final en el formato AAAA-MM-DD:\n")

        time, sorted_artworks, size_artists, purchase = sortArtworksByDate(catalog, option, initial_date, end_date)
        size = lt.size(sorted_artworks)

        first_three = lt.subList(sorted_artworks, 1, 3)
        last_three = lt.subList(sorted_artworks, lt.size(sorted_artworks) - 3, 3)
        new_artworks = lt.newList()
        for element in lt.iterator(first_three):
            lt.addLast(new_artworks, element)
        for element in lt.iterator(last_three):
            lt.addLast(new_artworks, element)

        print("===================== Req No. 2 Inputs =====================\n")
        print(f"Artworks acquired between {initial_date} and {end_date}")
        print(f"With {size_artists} different artists and purchased {purchase} of them")
        print("The first and last 3 artists in the range are....")

        req3 = PrettyTable()
        req3.field_names = ["ObjectID", "Title", "ArtistsNames", "Medium", "Dimensions", "Date", "DateAcquired", "URL"]
        for artwork in lt.iterator(new_artworks):
            ide = artwork["ObjectID"]
            title = artwork["Title"]
            names = artwork["ArtistsNames"]
            medium = artwork["Medium"]
            dimensions = artwork["Dimensions"]
            date = artwork["Date"]
            acquired = artwork["DateAcquired"]
            url = artwork["URL"]
            req3.add_row([ide, title, names, medium, dimensions, date, acquired, url])
        print(req3)
        # print(f"Tiempo del algoritmo {algo_sel[int(option)]} es {time} milisegundos.")
    elif int(inputs[0]) == 4:

        artistname= input("Digite el nombre del artista a examinar: ")
        respuestas= controller.getArtworksByArtist(catalog, artistname)
        print("===========================================================================================================================")
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
            print("===========================================================================================================================")
            print("Título:", x["Title"],"\n| Fecha de la obra:", x["Date"], "\n| Medio:", x["Medium"], "\n| Dimensiones:", x["Dimensions"], end= "\n")
            print("===========================================================================================================================")

    elif int(inputs[0]) == 5:

        nation_count = countNationalities(catalog)
        top_nation = max(nation_count.items(), key=lambda x: x[1])
        top_name = top_nation[0]
        top_count = top_nation[1]
        nation_artwork = showNationWork(catalog, nation_count)

        print("===================== Req No. 4 Inputs =====================")
        print(f"Ranking countries by their number of artworks in the MoMA...")
        print("\n===================== Req No. 4 Answer =====================")
        print("The TOP 10 Countries in the MoMA are:")
        print("========================================")

        req41 = PrettyTable()
        req41.field_names = ["Nationality", "Artworks"]
        for k, v in nation_count.items():
            nation = k
            count = v
            req41.add_row([nation, count])
        print(req41)

        req42 = PrettyTable()

        print(f"The TOP nationality in the museum is: {top_name} with {top_count} unique pieces")
        
        req42.field_names = ["ObjectID", "Title", "ArtistsNames", "Medium", "Dimensions", "Date", "DateAcquired", "URL"]

        for artwork in lt.iterator(nation_artwork):
            ide = artwork["ObjectID"]
            title = artwork["Title"]
            names = artwork["ArtistsNames"]
            medium = artwork["Medium"]
            dimensions = artwork["Dimensions"]
            date = artwork["Date"]
            acquired = artwork["DateAcquired"]
            url = artwork["URL"]
            req42.add_row([ide, title, names, medium, dimensions, date, acquired, url])
        print(req42)

    elif int(inputs[0]) == 6:
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
    elif int(inputs[0]) == 7:
        
        years = input("Digite el año inicial y final de las obras que quiere en su exposición en el formato 'YYYY-YYYY':\n")
        area = input("Digite el área disponible para sugerirle una exposición (en m^2):\n")
        selected_artworks, counter, area_sum = selectArtworks(catalog, years, area)

        print("===================== Req No. 6 (BONUS) Inputs =====================")
        print("Searching artworks between 1995 to 2001")
        print(f"With an available area of: {area} m^2")
        print("\n===================== Req No. 6 (BONUS) Answer =====================")
        print(f"The MoMA is going to exhibit pieces from {years.split(':')[0]} to {years.split(':')[0]}")
        print(f"There are {counter} possible items in an available area of: {area} m^2")
        print(f"The possible exhibit has {lt.size(selected_artworks)} items")
        print(f"Filling {area_sum} m^2 of the {area} m^2 available\n")
        print("The first and last 3 objects in the artwork list are:")

        req6 = PrettyTable()
        req6.field_names = ["ObjectID", "Title", "ArtistsNames", "Medium", "Dimensions", "Date", "Department", "Est. Area", "Classification", "URL"]
        for artwork in lt.iterator(selected_artworks):
            ide = artwork["ObjectID"]
            title = artwork["Title"]
            names = artwork["ArtistsNames"]
            medium = artwork["Medium"]
            dimensions = artwork["Dimensions"]
            date = artwork["Date"]
            department = artwork["Department"]
            estimated_area = artwork["Est. Area"]
            classification = artwork["Classification"]
            url = artwork["URL"]
        req6.add_row([ide, title, names, medium, dimensions, date, department, estimated_area, classification, url])
        print(req6)
        # Table

    else:
        sys.exit(0)
