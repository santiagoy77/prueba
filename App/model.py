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
def newCatalog():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'videoTittle': None,
               'channelName': None,
               'categorynum': None,
               'VideoLink': None}

    catalog['videoTittle'] = lt.newList()
    catalog['channelName'] = lt.newList('ARRAY_LIST',
                                    cmpfunction=comparechannelname)
    catalog['Categorynum'] = lt.newList('SINGLE_LINKED',
                                 cmpfunction=comparecategory)
    catalog['VideoLink'] = lt.newList('SINGLE_LINKED')

    return catalog


# Funciones para agregar informacion al catalogo

def addBook(catalog, video):
    # Se adiciona el video a la lista de videos
    lt.addLast(catalog['videoTittle'], video)
    # Se obtiene el nombre del canal autor del video
    name = book['channelName']
    # crea un libro en la lista de dicho canal
    addChannelName(catalog, author, name, video)


def addChannelChannel(catalog, name, video):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    channels = catalog['channelname']
    poschannel = lt.isPresent(channels, name)
    if posauthor > 0:
        channel = lt.getElement(channels, poschannel)
    else:
        channel = newChannel(channelname)
        lt.addLast(channels, channel)
    lt.addLast(channel['books'], book)


def addCategoryNum(catalog, tag):
    """
    Adiciona un tag a la lista de tags
    """
    t = newTag(tag['tag_name'], tag['tag_id'])
    lt.addLast(catalog['tags'], t)


def addVideoLink(catalog, booktag):
    """
    Adiciona un tag a la lista de tags
    """
    t = newBookTag(booktag['tag_id'], booktag['goodreads_book_id'])
    lt.addLast(catalog['book_tags'], t)


# Funciones para creacion de datos

def newChannel(name):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    author = {'name': "", "books": None,  "average_rating": 0}
    author['name'] = name
    author['books'] = lt.newList('ARRAY_LIST')
    return author


def newTag(name, id):
    """
    Esta estructura almancena los tags utilizados para marcar libros.
    """
    tag = {'name': '', 'tag_id': ''}
    tag['name'] = name
    tag['tag_id'] = id
    return tag


def newBookTag(tag_id, book_id):
    """
    Esta estructura crea una relación entre un tag y
    los libros que han sido marcados con dicho tag.
    """
    booktag = {'tag_id': tag_id, 'book_id': book_id}
    return booktag


# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento