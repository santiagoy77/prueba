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
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    catalog = {'video': None, 'category': None}
    catalog['video'] = lt.newList()
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