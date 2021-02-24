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
from DISClib.Algorithms.Sorting import shellsort as shell
from DISClib.Algorithms.Sorting import selectionsort as sel
from DISClib.Algorithms.Sorting import insertionsort as ins
import time
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo
tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newCatalog(chosenType):

    typeofList = "ARRAY_LIST"
    if chosenType == 1:
        typeofList = "LINKED_LIST"
    catalog = {"videos": None, "categories": None}
    catalog["videos"] = lt.newList(typeofList)
    catalog["categories"] = lt.newList()

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


def firstReq(catalog, n_videos, data_size, algorithm):
    "Completa el requerimiento 1"
    data_sublist = lt.subList(catalog["videos"], 1, data_size)
    data_sublist = data_sublist.copy()
    if algorithm == 0:
        start_time = time.process_time()
        sorted_list = sel.sort(data_sublist, cmpVideosByViews)
        stop_time = time.process_time()
    elif algorithm == 1:
        start_time = time.process_time()
        sorted_list = ins.sort(data_sublist, cmpVideosByViews)
        stop_time = time.process_time()
    elif algorithm == 2:
        start_time = time.process_time()
        sorted_list = shell.sort(data_sublist, cmpVideosByViews)
        stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    sorted_top_n = lt.subList(sorted_list, 1, n_videos)
    return [sorted_top_n, elapsed_time_mseg]
