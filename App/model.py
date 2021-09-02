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
  Inicializa el catálogo de artistas y obras (PENDIENTE)
  """
  catalog = {'artists': None,
             'artworks': None}

  catalog['artists'] = lt.newList('SINGLE_LINKED', cmpfunction=compareartists)
  catalog['artworks'] = lt.newList()

  return catalog

# Funciones para agregar informacion al catalogo

def addArtwork(catalog, artwork):
    # Se adiciona la obra a la lista de obras
    lt.addLast(catalog['artworks'], artwork)
    # Se obtienen los artistas de la obra
    artists = artwork[''].split(",")
    # Cada artista, se crea en la lista de artistas del catálogo, y se
    # crea una obraa en la lista de dicho artista (apuntador a la obra)
    for artist in artists:
        addArtworkArtist(catalog, artist.strip(), artwork)

def addArtworkArtist(catalog, artistname, born, death, gender, nation):
    """
    Adiciona un artista a lista de artistas, la cual guarda referencias
    a las obras de dicho artista (PENDIENTE)
    """
    artists = catalog['artists']
    posartist = lt.isPresent(artists, artistname)
    if posartist > 0:
        artist = lt.getElement(artists, posartist)
    else:
        artist = newArtist(artistname, born, death, gender, nation)
        lt.addLast(artists, artist)

    # lt.addLast(artist['artworks'], artwork)

# Funciones para creacion de datos
def newArtist(name, begin_date, end_date, gender, nationality):
  """
  Crea una nueva estructura para modelar el perfil del artista (su información personal) y sus obras
  """
  artist = {'name': "",
            'born_date': None,
            'death_date': None,
            'gender': "",
            'nationality': "",
            'artworks': None}
  
  artist['name'] = name
  artist['born_date'] = begin_date
  artist['death_date'] = end_date
  artist['gender'] = gender
  artist['nationality'] = nationality
  artist['artworks'] = lt.newList('ARRAY_LIST')

  return artist

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def compareartists(artistname1, artist):
  if (artistname1.lower() in artist['name'].lower()):
    return 0
  return -1

# Funciones de ordenamiento