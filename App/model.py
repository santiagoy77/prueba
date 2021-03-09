"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import quicksort as quick
import operator
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo
tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newCatalog():

    typeofList = "ARRAY_LIST"
    catalog = {"videos": None, "categories": None}
    catalog["videos"] = lt.newList(typeofList, cmpfunction=cmpVideosByViews)
    catalog["categories"] = lt.newList(typeofList, cmpfunction=cmpVideosByViews)

    return catalog


# Funciones para agregar informacion al catalogo


def addVideo(catalog, video):
    # Se adiciona el video a la lista de videos
    lt.addLast(catalog['videos'], video)


def addCategory(catalog, category):
    # Se adiciona la categoria a la lista de categorias
    lt.addLast(catalog['categories'], category)

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento


def cmpVideosByViews(video1, video2):
    """
    Devuelve verdadero (True) si los 'views' de video1 son menores que
    los del video2
    Args:
    video1: informacion del primer video que incluye su valor 'views'
    video2: informacion del segundo video que incluye su valor 'views'
    """
    return (video1["views"] < video2["views"])


def firstReq(catalog, data_size, country, category):
    """
    Completa el requerimiento 1
    """
    filtered = catalog.copy()
    i = 1
    t = lt.size(filtered["videos"])
    while i <= t:
        elem = lt.getElement(filtered["videos"], i)
        if (elem["country"].lower()) != (country.lower()) or elem["category_id"] != category:
            lt.deleteElement(filtered["videos"], i)
            t -= 1
            i -= 1
        i += 1
    print("list ------------------------------------------------------------------")
    print(filtered["videos"])
    sorted_list = quick.sort(filtered["videos"], cmpVideosByViews)
    print("Sorted list -----------------------------------------------------------")
    print(sorted_list)
    data_sublist = lt.subList(sorted_list, 1, data_size)
    data_sublist = data_sublist.copy()
    print("Data sublist ----------------------------------------------------------")
    print(data_sublist)
    return data_sublist


def secondReq():
    """
    Completa el requerimiento 2
    """
    pass


def thirdReq(catalog, category):
    """
    Completa el requerimiento 3
    """
    dicc = {}
    filtered = catalog.copy()
    i = 1
    t = lt.size(filtered["videos"])
    while i <= t:
        elem = lt.getElement(filtered["videos"], i)
        if elem["category_id"] != category:
            lt.deleteElement(filtered["videos"], i)
            t -= 1
            i -= 1
        i += 1
    i = 1
    t = lt.size(filtered["videos"])
    x = 0
    while i <= t:
        elem = lt.getElement(filtered["videos"], i)
        #titulo = (elem["title"])
        titulo = (elem["title"] + "#,@,#" + elem["channel_title"])
        if titulo not in dicc:
            dicc[titulo] = 1
            x += 1
        else:
            dicc[titulo] += 1
        i += 1
    dicc_sort = sorted(dicc.items(), key=operator.itemgetter(1), reverse=True)
    mayor = dicc_sort[0]
    primerosdatos = mayor[0].split("#,@,#")
    resultado = [primerosdatos[0], primerosdatos[1], mayor[1], category]
    return resultado

    

    


def fourthReq(catalog, data_size, country, tag):
    """
    Completa el requerimiento 3
    """
    pass

    