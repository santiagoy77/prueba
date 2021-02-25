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
from DISClib.Algorithms.Sorting import shellsort as she
from DISClib.Algorithms.Sorting import selectionsort as sel
from DISClib.Algorithms.Sorting import insertionsort as ins

assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""


def newCatalog(list_type):
    catalog = {'videos': None,
               'country': None,
               'category': None,
               'tags': None}

    catalog['videos'] = lt.newList(list_type,
                                   cmpfunction=compVideosByViews)
    catalog['country'] = lt.newList(list_type,
                                    cmpfunction=None)
    catalog['category'] = lt.newList(list_type,
                                 cmpfunction=None)
    catalog['tags'] = lt.newList(list_type)
    return catalog

def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)
    countries = video['country'].split(",")
#for country in countries:
#        addVideoCountry(catalog, country.strip(), video)

def addVideoCountry(catalog, countryname, video):
    countries = catalog['country']
    poscountry = lt.isPresent(countries, countryname)
    if poscountry > 0:
        country = lt.getElement(countries, poscountry)
    else:
        country = newCountry(countryname)
        lt.addLast(countries, country)
    lt.addLast(country['videos'], video)

def newCountry(name):
    country = {'country': "", "videos": None,  "trending": 0}
    country['country'] = name
    country['videos'] = lt.newList('ARRAY_LIST')
    return country

def addVideoCategory(catalog, categoryname, video):
    categories = catalog['category']
    poscategory = lt.isPresent(categories, countryname)
    if poscategory > 0:
        category = lt.getElement(categories, poscategory)
    else:
        category = newCategory(categoryname)
        lt.addLast(categories, category)
    lt.addLast(category['videos'], video)

def newCategory(name):
    category = {'category': "", "videos": None,  "trending": 0}
    category['category'] = name
    category['videos'] = lt.newList('ARRAY_LIST')
    return category



#def addTag(catalog, tag):
#    t = newTag(tag['id'])
#    lt.addLast(catalog['tags'], t)

def newTag(idname):
    tag = {'idname': ''}
    tag['idname'] = idname
    return tag

def newSList(lst, pos, numelem):
    return lt.subList(lst, pos, numelem)




# Funciones para creacion dzae datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def compVideosByViews(video1,video2):
    if int(video1["views"]) < int(video2["views"]):
        return True
    else: 
        return False 
# Funciones de ordenamiento

def sort(lst, fun):
    if fun == "selectionsort":
        return selesort(lst)
    elif fun == "insertionsort":
        return insersort(lst)
    elif fun == "shellsort":
        return shesort(lst)
    else:
        print("Funcion de ordenamiento no existe.")

def selesort(lst):
    return sel.sort(lst, lst["cmpfunction"])

def insersort(lst):
    return ins.sort(lst, lst["cmpfunction"])

def shesort(lst):
    return she.sort(lst, lst["cmpfunction"])






