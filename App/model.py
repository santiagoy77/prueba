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
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar
    todos los videos, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y videos. Retorna el catalogo inicializado.
    """
    catalog = {'videos': None,
               'channel_title': None,
               }

    catalog['videos'] = lt.newList()
    catalog['channel_title'] = lt.newList('ARRAYLIST')
  

    return catalog

# Funciones para agregar informacion al catalogo


def addVideo(catalog, video):
    # Se adiciona el video a la lista de videos
    lt.addLast(catalog['videos'], video)
    # Se obtiene el autor del video
    


def addVideoYoutuber(catalog, authorname, videos):
    """
    Adiciona un youtuber a lista de youtubers, la cual guarda referencias
    a los videos de dicho youtuber
    """
    channel_title = catalog['channel_title']
    poschannel_title = lt.isPresent(channel_title, authorname)
    if poschannel_title > 0:
        channel_titlee = lt.getElement(channel_title, poschannel_title)
    else:
        channel_titlee = newAuthor(authorname)
        lt.addLast(channel_title, channel_titlee)
    lt.addLast(channel_titlee['videos'], videos)



def newAuthor(name):
    """
    Crea una nueva estructura para modelar los videos de
    un autor y su promedio de ratings
    """
    channel_titlee = {'name': "", "videos": None,  "likes": 0}
    channel_titlee['name'] = name
    channel_titlee['videos'] = lt.newList('ARRAY_LIST')
    return channel_titlee







