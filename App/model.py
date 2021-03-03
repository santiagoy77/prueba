'''
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
 '''


import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import selectionsort as sel
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as mer
assert cf

'''
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de los mismos.
'''


# Construccion de modelos
def newCatalog(tipo_de_dato):
    catalog = {'videos': None,
               'by_countries': None,
               'by_categories': None,
               'category-id': None}

    catalog['videos'] = lt.newList(datastructure=tipo_de_dato)
    catalog['by_countries'] = lt.newList(datastructure='ARRAY_LIST')
    catalog['by_categories'] = lt.newList(
        datastructure='ARRAY_LIST', cmpfunction=cmpCategories())
    catalog['category-id'] = lt.newList(datastructure='ARRAY_LIST')
    return catalog

# Funciones para agregar informacion al catalogo


def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)
    country = video['country'], strip()
    category = video['category_id']

    addVideoCountry(catalog, country, video)
    addVideoCategory(catalog, category, vidoe)


def addCategory(catalog, category):
    c = newCategory(category['id'], category['name'])
    lt.addLast(catalog['category-id'], c)


def addVideoCountry(catalog, country, video):
    pass


def addVideoCategory(catalog, category_id, video):
    categories = catalog['categories']
    posCategory = lt.isPresent(catalog, category_id)

    if posCategory > 0:  # La categoria ya ha sido creada dentro de la lista
        category = lt.getElement(catalog, posCategory)
    else:  # Debemos crear una nueva categoria
        category = newCategory(category_id)
        lt.addLast(catalog(categories, category))

    lt.addLast(category['videos'], video)


def newCategory(category_id):
    category_list = {'name': "", "videos": None}
    category_list['name'] = category_id
    category_list['videos'] = lt.newList('ARRAY_LIST')
    return category_list


def newCategoryId(id, name):
    """
        Crea un diccionario en el que guarda el nombre de la categoria y su id correpondiente
    """
    category = {'id': '', 'name': ''}
    category['id'] = int(id)
    category['name'] = name.strip()
    return category


def compVideosByViews(video1, video2):
    """
    Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2
    Args:
        video1: informacion del primer video que incluye su valor 'views'
        video2: informacion del segundo video que incluye su valor 'views'
    """
    views1 = video1["views"]
    views2 = video2["views"]

    return views1 < views2


def sortVideosSelection(catalog, size):
    sub_list = lt.subList(catalog['videos'], 0, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    sorted_list = sel.sort(sub_list, compVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list


def sortVideosInsertion(catalog, size):
    sub_list = lt.subList(catalog['videos'], 0, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    sorted_list = ins.sort(sub_list, compVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list


def sortVideosShell(catalog, size):
    sub_list = lt.subList(catalog['videos'], 0, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    sorted_list = sa.sort(sub_list, compVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list


def getId(category_ids, category_name):
    for item in lt.iterator(category_ids):
        if item['name'] == category_name:
            return item['id']


def auxList(catalog, data_type, list_of):
    pass


def sortDays(catalog):
    pass


def cmpByDays(video1, video2):
    pass


def sortCategory(catalog):
    cat_sort = lt.subList(catalog['videos'], 1, lt.size(catalog['videos']))
    cat_sort = mer.sort(cat_sort, cmpCategories)
    return cat_sort


def cmpCategoriesSort(video1, video2):
    return video1['category_id'] < video2['category_id']


def cmpCategories(video1, video2):
    if video1['category_id'] < video2['category_id']:
        return -1
    elif video1['category_id'] > video2['category_id']:
        return 1
    else:
        return 0

# def orderedList(catalog,country,category):
#     videoList = catalogo["videos"]
#     sublist = lt.newList(datastructure=)


# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
