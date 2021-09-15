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


import copy
import time
from datetime import datetime
import config as cf


from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import insertionsort as insertion
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.Algorithms.Sorting import quicksort as quick
from DISClib.Algorithms.Sorting import shellsort as shell

assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Selectores

sort_algo = {1: insertion, 2: shell, 3: merge, 4: quick}

# Construccion de modelos

def newCatalog(implementation):
  """
  Inicializa el catálogo de artistas y obras (PENDIENTE)
  """
  catalog = {'artists': None,
             'artworks': None}

  if int(implementation) == 1:
    option = "ARRAY_LIST"
  elif int(implementation) == 2:
    option = "SINGLE_LINKED"

  catalog['artists'] = lt.newList(option, cmpfunction=compareartists)
  catalog['artworks'] = lt.newList(option, cmpfunction=cmpArtworkByDateAcquired)

  return catalog

def selectSample(catalog, sample):
  """
  Selecciona una muestra de los datos de la longitud que indique el parámetro sample
  """
  sample = int(sample)
  artworks_lenght = lt.size(catalog["artworks"])
  if sample not in range(artworks_lenght):
    lenght = artworks_lenght
  else:
    lenght = sample

  subsection = lt.subList(catalog["artworks"], 0, lenght)
  return subsection

# Funciones para agregar informacion al catalogo

def addArtwork(catalog, artwork):
    # Se adiciona la obra a la lista de obras
    lt.addLast(catalog['artworks'], artwork)
    # Se obtienen los artistas de la obra
    artists_ids = artwork['ConstituentID'].split(",")
    # Cada artista, se crea en la lista de artistas del catálogo, y se
    # crea una obraa en la lista de dicho artista (apuntador a la obra)
    for artist_id in artists_ids:
        addArtist(catalog, artist_id.strip(), artwork)

def addArtist(catalog, artist_id, artwork):
    """
    Adiciona un artista a lista de artistas, la cual guarda referencias
    a las obras de dicho artista
    """
    artists = catalog['artists']
    posartist = lt.isPresent(artists, artist_id)
    if posartist > 0:
        artist = lt.getElement(artists, posartist)
    else:
        artist = newArtist(artist_id)
        lt.addLast(artists, artist)

    lt.addLast(artist['Artworks'], artwork)

def addArtistInfo(catalog, artist_info):
  """
  Agrega la información de los artistas a la lista de artistas
  """
  artist_id = artist_info['ConstituentID']
  artists = catalog['artists']
  pos_artist = lt.isPresent(artists, artist_id)
  if pos_artist > 0:
    artist_info['Artworks'] = lt.getElement(artists, pos_artist)['Artworks']
    lt.changeInfo(artists, pos_artist, artist_info)
  else:
    artist_info['Artworks'] = lt.newList("ARRAY_LIST")
    lt.addLast(artists, artist_info)


# Funciones para creacion de datos
def newArtist(artist_id):
  """
  Crea una nueva estructura para modelar el perfil del artista (su información personal) y sus obras
  """
  artist = {"ConstituentID": None,
            "DisplayName": "",
            "BeginDate": None,
            "EndDate": None,
            "Nationality": "",
            "Gender": "",
            "ArtistBio": "",
            "Wiki QID": "",
            "ULAN": "",
            "Artworks": None}

  artist["ConstituentID"] = artist_id
  artist["Artworks"] = lt.newList('ARRAY_LIST')

  return artist

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def compareartists(artist_id, artist):
  if (artist_id in artist['ConstituentID']):
    return 0
  return -1

def cmpArtistsByBeginDate(artist1, artist2):
  """
  Devuelve verdadero (True) si el 'BeginDate' de artist1 es menores que el de artist2
    Args:
    artist1: informacion de la primera obra que incluye su valor 'BeginDate'
    artist2: informacion de la segunda obra que incluye su valor 'BeginDate'
  """
  if artist1['BeginDate'] < artist2['BeginDate']:
    return 1
  return 0

def cmpArtworkByDateAcquired(artwork1, artwork2):
  """
  Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork2
    Args:
    artwork1: informacion de la primera obra que incluye su valor 'DateAcquired'
    artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired'
  """
  if artwork1['DateAcquired'] < artwork2['DateAcquired']:
    return 1
  return 0

# Funciones de ordenamiento

def sortArtistsByBeginDate(catalog, implementation, initial_date, end_date):
  """
  Ordena los artistas en el rango de fechas dispuesto
  """
  filterArtistsByBeginDate(catalog, initial_date, end_date)
  algorithm = sort_algo[int(implementation)]
  start_time = time.process_time()
  sorted_entries = algorithm.sort(catalog["artists"], cmpArtistsByBeginDate)
  stop_time = time.process_time()
  elapsed_time_mseg = (stop_time - start_time) * 1000
  return elapsed_time_mseg, sorted_entries

def sortArtworksByDate(catalog, implementation, initial_year, end_year):
  """
  Ordena las obras en el rango de fechas dispuesto
  """
  filterArtworksByDate(catalog, initial_year, end_year)
  algorithm = sort_algo[int(implementation)]
  start_time = time.process_time()
  sorted_entries = algorithm.sort(catalog["artworks"], cmpArtworkByDateAcquired)
  stop_time = time.process_time()
  elapsed_time_mseg = (stop_time - start_time) * 1000
  return elapsed_time_mseg, sorted_entries
  
# Funciones auxiliares

def filterArtistsByBeginDate(catalog, initial_date, end_date):
  """
  Filtra los artistas que no se encuentren en el rango de años deseado
  (NO ESTÁ TERMINADA. FUNCIÓN ACTUALMENTE DEFECTUOSA)
  """
  iter_artists = enumerate(lt.iterator(catalog["artists"]))

  initial_date = datetime.strptime(initial_date, "%Y")
  end_date = datetime.strptime(end_date, "%Y")
  pos_to_delete = lt.newList()

  deleted_elements = 0
  for ix, artist in iter_artists:
    if type(artist["BeginDate"]) == None:
      print(f"TEMP: {type(artist['BeginDate'])}")
      lt.addLast(pos_to_delete, ix - deleted_elements)
      deleted_elements += 1
      continue
    elif artist["BeginDate"] == 0 or artist["BeginDate"] == "0":
      lt.addLast(pos_to_delete, ix - deleted_elements)
      deleted_elements += 1
      continue
    else:
      date = datetime.strptime(artist["BeginDate"], "%Y")
      if initial_date > date or end_date < date:
        lt.addLast(pos_to_delete, ix - deleted_elements)
        deleted_elements += 1
  
  for pos in lt.iterator(pos_to_delete):
    lt.deleteElement(catalog['artists'], pos)

def filterArtworksByDate(catalog, initial_date, end_date):
  """
  Filtra las obras que no se encuentren en el rango de años deseado
  """
  iter_artworks = lt.iterator(catalog["artworks"])

  initial_date = datetime.strptime(initial_date, "%Y-%m-%d")
  end_date = datetime.strptime(end_date, "%Y-%m-%d")
  pos_to_delete = lt.newList()

  deleted_elements = 0
  for ix, artwork in enumerate(iter_artworks):
    if artwork["DateAcquired"] == '':
      lt.addLast(pos_to_delete, ix - deleted_elements)
      deleted_elements += 1
      continue
    art_dates = datetime.strptime(artwork["DateAcquired"], "%Y-%m-%d")
    if initial_date > art_dates or end_date < art_dates:
      lt.addLast(pos_to_delete, ix - deleted_elements)
      deleted_elements += 1
  
  for pos in lt.iterator(pos_to_delete):
    lt.deleteElement(catalog['artworks'], pos)

# def createDateRange(first_date, second_date):
#   """
#   Given two datetime objects, it returns a list with all the dates in between
#   """
#   for 