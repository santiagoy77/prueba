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
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import selectionsort as sls
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import shellsort as shl
assert cf


def newCatalog(listType):
    """
    The catalog starts where two empty lists are created, one for the videos and the other for the categories.
    Return the catalog
    """
    catalog = {'videos': None,
               'categories': None,}

    catalog['videos'] = lt.newList(listType, cmpfunction=cmpVideosByViews)
    catalog['categories'] = lt.newList(listType, cmpfunction=None)
    
    return catalog


# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    'The video is added to the video list'
    lt.addLast(catalog['videos'], video)

def addCategory(catalog, category):
    'The category is added to the category list'
    lt.addLast(catalog['categories'], category)

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpVideosByViews(video1, video2):
    'Return True if vid1 < vid2'
    return (float(video1['views']) < float(video2['views']))


# Funciones de ordenamiento

def selectSortMethod(method):
    if method == 'sls':
        sortType = sls
    elif method == 'ins':
        sortType = ins
    elif method ==  'shl':
        sortType = shl
    return sortType

def sortVideos(catalog, size, method):
    sortmet = selectSortMethod(method)
    sub_list = lt.subList(catalog['videos'], 0, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    sorted_list = sortmet.sort(sub_list, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list

