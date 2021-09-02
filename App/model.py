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
    Inicializa el catálogo del museo. Crea una lista vacia para guardar
    todos los artistas, adicionalmente, crea una lista vacia para las obras de arte.
    Retorna el catalogo inicializado.
    """
    catalog = {'artists': None,
               'artworks': None}

    catalog['artists'] = lt.newList('ARRAY_LIST',
                                    cmpfunction=compareartistyears)
    catalog['artworks'] = lt.newList('ARRAY_LIST',
                                    cmpfunction=compareartworkyears)
    
    return catalog

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    """
    Adiciona un artista a la lista de artistas
    """
    a = newArtist(artist['DisplayName'], artist['Wiki QID'])
    lt.addLast(catalog['artists'], a)

def addArtwork(catalog, artwork):
    """
    Adiciona una obra a la lista de obras
    """
    art = newArtwork(artwork['Title'], artwork['ConstituentID'])
    lt.addLast(catalog['artworks'], art)

# Funciones para creacion de datos
def newArtist(name, id):
    """
    Esta estructura almancena los artistas utilizados.
    """
    artist = {'DisplayName': '', 'Wiki QID': ''}
    artist['DisplayName'] = name
    artist['Wiki QID'] = id
    return artist

def newArtwork(name, id):
    """
    Esta estructura almancena las obras utilizadas.
    """
    artist = {'Title': '', 'ConstituentID': ''}
    artist['Title'] = name
    artist['ConstituentID'] = id
    return artist

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def compareartistyears(year1, year2):
    return (int(year1['BeginDate']) > int(year2['BeginDate']))

def compareartworkyears(year1, year2):
    return (int(year1['Date']) > int(year2['Date']))