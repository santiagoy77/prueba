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
               'authors': None,
               'tags': None,
               'video_tags': None}

    catalog['videos'] = lt.newList()
    catalog['authors'] = lt.newList('SINGLE_LINKED',
                                    cmpfunction=compareauthors)
    catalog['tags'] = lt.newList('ARRAY_LIST',
                                 cmpfunction=comparetagnames)
    catalog['video_tags'] = lt.newList('ARRAY_LIST')

    return catalog

# Funciones para agregar informacion al catalogo


def addVideo(catalog, video):
    # Se adiciona el video a la lista de videos
    lt.addLast(catalog['videos'], video)
    # Se obtiene el autor del video
    authors = video['authors'].split(",")
    # Cada autor, se crea en la lista de videos del catalogo, y se
    # crea un video en la lista de dicho autor (apuntador al video)
    for youtuber in authors:
        addVideoYoutuber(catalog, youtuber.strip(), video)


def addVideoYoutuber(catalog, authorname, video):
    """
    Adiciona un youtuber a lista de youtubers, la cual guarda referencias
    a los videos de dicho youtuber
    """
    authors = catalog['authors']
    posauthor = lt.isPresent(authors, authorname)
    if posauthor > 0:
        author = lt.getElement(authors, posauthor)
    else:
        author = newAuthor(authorname)
        lt.addLast(authors, author)
    lt.addLast(author['videos'], video)


def addTag(catalog, tag):
    """
    Adiciona un tag a la lista de tags
    """
    t = newTag(tag['tag_name'], tag['tag_id'])
    lt.addLast(catalog['tags'], t)


def addVideoTag(catalog, videotag):
    """
    Adiciona un tag a la lista de tags
    """
    t = newVideoTag(videotag['tag_id'], videotag['goodreads_book_id']
                    )  # No se si acá iría category_id y video_id
    lt.addLast(catalog['video_tags'], t)

# Funciones para creacion de datos


def newAuthor(name):
    """
    Crea una nueva estructura para modelar los videos de
    un autor y su promedio de ratings
    """
    author = {'name': "", "videos": None,  "average_rating": 0}
    author['name'] = name
    author['videos'] = lt.newList('ARRAY_LIST')
    return author


def newTag(name, id):
    """
    Esta estructura almancena los tags utilizados para marcar libros.
    """
    tag = {'name': '', 'tag_id': ''}
    tag['name'] = name
    tag['tag_id'] = id
    return tag


def newVideoTag(tag_id, video_id):
    """
    Esta estructura crea una relación entre un tag y
    los videos que han sido marcados con dicho tag.
    """
    videotag = {'tag_id': tag_id, 'book_id': video_id}
    return videotag

# Funciones de consulta


def getVideosByAuthor(catalog, authorname):
    """
    Retorna un autor con sus videos a partir del nombre del autor
    """
    posauthor = lt.isPresent(catalog['authors'], authorname)
    if posauthor > 0:
        author = lt.getElement(catalog['authors'], posauthor)
        return author
    return None


def getBestVideos(catalog, number):
    """
    Retorna los mejores videos
    """
    videos = catalog['videos']
    bestvideos = lt.newList()
    for cont in range(1, number+1):
        book = lt.getElement(videos, cont)
        lt.addLast(bestvideos, book)
    return bestvideos


def countVideosByTag(catalog, tag):
    """
    Retorna los videos que fueron etiquetados con el tag
    """
    tags = catalog['tags']
    videocount = 0
    pos = lt.isPresent(tags, tag)
    if pos > 0:
        tag_element = lt.getElement(tags, pos)
        if tag_element is not None:
            for video_tag in lt.iterator(catalog['video_tags']):
                if tag_element['tag_id'] == video_tag['tag_id']:
                    videocount += 1
    return videocount

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
