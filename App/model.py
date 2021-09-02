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
    catalog = {'artwork': None,
               'artist': None,}

    catalog['artwork'] = lt.newList()
    catalog['artist'] = lt.newList('ARRAY_LIST',
                                    cmpfunction=compareartists)

    return catalog
# Construccion de modelos

# Funciones para agregar informacion al catalogo
def addArtwork(catalog, artwork):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog['artwork'], artwork)
    # Se obtienen los autores del libro
    artists = artwork['artists'].split(",")
    # Cada autor, se crea en la lista de libros del catalogo, y se
    # crea un libro en la lista de dicho autor (apuntador al libro)
    for artist in artists:
        addArtworkArtist(catalog, artist.strip(), artwork)


def addArtworkArtist(catalog, artistname, artwork):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    artists = catalog['artists']
    posartist = lt.isPresent(artists, artistname)
    if posartist > 0:
        artist = lt.getElement(artists, posartist)
    else:
        author = newArtist(artistname)
        lt.addLast(artists, author)
    lt.addLast(author['artworks'], artwork)




# Funciones para creacion de datos

def newArtist(name):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    artist = {'name': "", "artwork": None,  "average_rating": 0}
    artist['name'] = name
    artist['artqork'] = lt.newList('ARRAY_LIST')
    return artist





# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def compareartists(authorname1, author):
    if (authorname1.lower() in author['name'].lower()):
        return 0
    return -1

# Funciones de ordenamiento