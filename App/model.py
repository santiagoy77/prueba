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


from DISClib.DataStructures.arraylist import addLast
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

def artistsInfo():
    artists_info = lt.newList('SINGLE_LINKED',
                cmpfunction=None)
    return artists_info

# Funciones para agregar informacion al catalogo

def addArtWork(catalog, artwork):
    lt.addLast(catalog['artworks'], artwork)
    artists = artwork['ConstituentID'].split(',')
    artworktitle = artwork['Title']

    for artist in artists:
        addArtWorkArtist(catalog, artist.strip() , artworktitle)
    

def addArtWorkArtist(catalog, artistname, artwork):

    artists = catalog['artists']
    posArtist = lt.isPresent(artists, artistname)
    if posArtist > 0:
        artist = lt.getElement(artists, posArtist)
    else:
        artist = newArtist(artistname)
        lt.addLast(artists, artist)
    artistname = artist['name']

    lt.addLast(artist['artworks'], artwork)

def addArtistsInfo(artists_info, info):
    var =  lt.isEmpty(artists_info)
    if var == True:
        lt.addFirst(artists_info, info)
    else:
        lt.addLast(artists_info, info)
    

# Funciones para creacion de datos

def newArtist(name):

    artist = {
        'name' : "",
        'artworks' : None,
        'info' : None,
            }
    artist['name'] = name
    artist['artworks'] = lt.newList('ARRAY_LIST')
    artist['info'] = 'x'
    return artist

def sublist(lst,pos,numelement):
    return lt.sublist(lst,pos,numelement)
        

# Funciones de consulta
def searchArtist(catalog,artist_info,artist):
    resultado = lt.newList()
    print(resultado)
    print(lt.size(catalog))
    for artwork in lt.size(catalog):
        print(artwork)

    return resultado

# Funciones utilizadas para comparar elementos dentro de una lista

def compareartists(artistname1, artist):
    if (artistname1.lower() in artist['name'].lower()):
        return 0
    return -1
    return None

def cmpArtworkByDateAdquired(artwork1,artwork2):
    resultado = False
    date1 = artwork1["DateAdquired"].split("-")
    date2 = artwork2["DateAdquired"].split("-")
    if date1[0] < date2[0]:
        resultado = True
    elif date1[1] < date2[1]:
        resultado = True
    elif date1[2] < date2[2]:
        resultado = True
    return resultado
        

# Funciones de ordenamiento