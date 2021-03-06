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
from DISClib.Algorithms.Sorting import shellsort as She
from DISClib.Algorithms.Sorting import selectionsort as Sel
from DISClib.Algorithms.Sorting import insertionsort as Inser
from DISClib.Algorithms.Sorting import mergesort as Merge
from DISClib.Algorithms.Sorting import quicksort as Quick
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    catalog = {'video': None, 'category': None}
    catalog['video'] = lt.newList('ARRAY_LIST',cmpfunction=cmpVideosByViews)
    catalog['category'] = lt.newList('ARRAY_LIST')#, cmpfunction=compareCategories
    return catalog

def addVideo(catalog, video):
    lt.addLast(catalog['video'], video)

def addCategory(catalog, category):
    cat = newCategory(category['id'], category['name'])
    lt.addLast(catalog['category'], cat)

def newCategory(id, name):
    Category = {'Category_id': '', 'name': ''}
    Category['Category_id'] = id
    Category['name'] = name
    return Category


# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

def VideosByViews(catalog, numElementos):
    sub_list = lt.subList(catalog['video'], 0, numElementos)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    sorted_list = Merge.sort(sub_list, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list

def cmpVideosByViews(video1, video2):
    return (float(video1['views']) < float(video2['views']))






"""    categories = video['category'].split(",")
    for category in categories:
        addVideoCategory(catalog, category.strip(), video)
def addVideoCategory(catalog, category_id, video):
    categories = catalog['category']
    positioncategory = lt.isPresent(categories, category_id)
    if positioncategory > 0:
        category = lt.getElement(categories, positioncategory)
    else:
        category = newCategory(category_id)
        lt.addLast(categories, category)
    lt.addLast(category['category'], video)"""