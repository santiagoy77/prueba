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
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'title': None,
               'channel_title': None
               }

    catalog['videos'] = lt.newList()
    catalog['channel_title'] = lt.newList('SINGLE_LINKED',
                                    cmpfunction=comparechannel)

    return catalog

# Funciones para agregar informacion al catalogo

def addBook(catalog, videos):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog['title'], videos)
    # Se obtienen los autores del libro
    authors = videos['channel_title'].split(",")
    # Cada autor, se crea en la lista de libros del catalogo, y se
    # crea un libro en la lista de dicho autor (apuntador al libro)
    for video in videos:
        addChannelTitle(catalog, video.strip(), videos)


def addChannelTitle(catalog, channel_title, video):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    channel = catalog['channel_title']
    poschannel = lt.isPresent(channel, channel_title)
    if posauthor > 0:
        author = lt.getElement(channel, poschannel)
    else:
        author = newAuthor(channel_title)
        lt.addLast(channel, author)
    lt.addLast(author['videos'], video)


# Funciones para creacion de datos


def newAuthor(name):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    author = {'name': "", "videos": None,  "likes": 0}
    author['name'] = name
    author['videos'] = lt.newList('ARRAY_LIST')
    return author

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def comparechannel(authorname1, author):
    if (authorname1.lower() in author['name'].lower()):
        return 0
    return -1

# Funciones de ordenamiento