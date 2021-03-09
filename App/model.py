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
from DISClib.Algorithms.Sorting import quicksort as qck
import time
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
    catalog["videos"] = lt.newList(typeofList)
    catalog["categories"] = lt.newList(typeofList)

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
    "Completa el requerimiento #1"
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

    data_sublist = lt.subList(filtered["videos"], 1, data_size)
    data_sublist = data_sublist.copy()
    sorted_list = qck.sort(data_sublist, cmpVideosByViews)
    return sorted_list
    