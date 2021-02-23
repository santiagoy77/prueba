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
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newCatalogSingle():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'title': None,
               'information_videos': None
               }

    catalog['title'] = lt.newList()
    catalog['information_videos'] = lt.newList('SINGLE_LINKED',
                                    cmpfunction=cmpVideosByViews)

    return catalog

def newCatalogArray():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'title': None,
               'information_videos': None
               }

    catalog['title'] = lt.newList()
    catalog['information_videos'] = lt.newList('ARRAY_LIST',
                                    cmpfunction=cmpVideosByViews)

    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, videos):

    lt.addLast(catalog['title'], videos)
 
    infoVideos = videos['information_videos'].split(",")

    for video in infoVideos:
        addInfoVideos(catalog, video.strip(), videos)


def addInfoVideos(catalog, information_videos, video):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    info = catalog['information_videos']
    posinfo = lt.isPresent(info, information_videos)
    if posinfo > 0:
        video = lt.getElement(info, posinfo)
    else:
        video = newVideo(information_videos)
        lt.addLast(info, video)
    lt.addLast(info['views'], video)


# Funciones para creacion de datos


def newVideo(name):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    video = {'name': "", "views": 0}
    video['name'] = name
    return author

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista




def cmpVideosByViews(video1, video2): 
    """ Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2 
    Args: 
        video1: informacion del primer video que incluye su valor 'views' 
        video2: informacion del segundo video que incluye su valor 'views' """
    return video1['views'] < video2['views']


def comparechannel(authorname1, author):
    if (authorname1.lower() in author['name'].lower()):
        return 0
    return -1



# Funciones de ordenamiento

def sortVideos(catalog):
    sa.sort(catalog['title'], cmpVideosByViews)