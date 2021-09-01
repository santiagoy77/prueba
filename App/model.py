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

    catalog = {
        "artworks" : None,
        "artists" : None,
    }
    catalog['artworks'] =  lt.newList()
    catalog['artists'] = lt.newList('SINGLE_LINKED',
                                    cmpfunction=compareartists)
    return catalog


# Funciones para agregar informacion al catalogo

def addArtWork(catalog, artwork):

    lt.addLast(catalog['artworks'], artwork)
    artists = artwork['ConstituentID'].split(',')

    for artist in artists:
        addArtWorkArtist(catalog, artist.strip() , artwork)
    

def addArtWorkArtist(catalog, artistname, artwork):

    artists = catalog['artists']
    posArtist = lt.isPresent(artists, artistname)
    if posArtist > 0:
        artist = lt.getElement(artists, posArtist)
    else:
        artist = newArtist(artistname)
        lt.addLast(artists, artist)
    lt.addLast(artist['artworks'], artwork)

    

# Funciones para creacion de datos

def newArtist(name):

    artist = {
        'name' : "",
        'artworks' : None
            }
    artist['name'] = name
    artist['artworks'] = lt.newList('ARRAY_LIST')
    return artist
        

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def compareartists(artistname1, artist):
    if (artistname1.lower() in artist['name'].lower()):
        return 0
    return -1
    return None


# Funciones de ordenamiento