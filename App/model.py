#channel_title = information_videos
#
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
from DISClib.Algorithms.Sorting import selectionsort as ss
from DISClib.Algorithms.Sorting import insertionsort as ins
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newCatalog(tipo_lista):
    tipo = ""
    if tipo_lista == 1:
        tipo = "ARRAY_LIST"
        print("array_list")
    elif tipo_lista == 2:
        tipo = "SINGLE_LINKED"
        print("single_linked")
    catalog = {'title': None,
               'categories': None}

    catalog['title'] = lt.newList(tipo)
    catalog['categories'] = lt.newList(tipo)
    print("carga completada")
    print("catalog model:",catalog)
    return catalog


# Funciones para agregar informacion al catalogo

def addVideo(catalog, videos):
    lt.addLast(catalog['title'], videos)


def newVideo(name):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    video = {'name': "", 'views': None}
    video['name'] = name
    video['views'] = lt.newList('ARRAY_LIST')
    return video

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista




def cmpVideosByViews(video1, video2): 
    """ Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2 
    Args: 
        video1: informacion del primer video que incluye su valor 'views' 
        video2: informacion del segundo video que incluye su valor 'views' """
    return (float(video1['views']) < float(video2['views']))

# Funciones de ordenamiento

def sortVideos(catalog,size,orden):
    nueva = lt.subList(catalog["title"],0,size)
    copia_lista = nueva.copy()
    if orden == 1:
        return sa.sort(copia_lista, cmpVideosByViews)
    elif orden == 2:
        return ss.sort(copia_lista, cmpVideosByViews)
    elif orden == 3:
        return ins.sort(copia_lista, cmpVideosByViews)
    else:
        return "Ha seleccionado una opcion invalida"


    

