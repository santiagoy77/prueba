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


from DISClib.DataStructures.arraylist import newList
import copy
import time
from datetime import datetime
import config as cf
from math import pi

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
    artists_ids = artwork['ConstituentID'].strip("[]").split(",")
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

def countNationalities(catalog):
  """
  Cuenta el número de obras por la nacionalidad de los artistas
  """
  counter = {}
  iter_artworks = lt.iterator(catalog["artworks"])
  for artwork in iter_artworks:
    nationalities = lt.newList(cmpfunction=cmpArtistsByNationality)
    ids = artwork["ConstituentID"].strip("[]").split()
    disc_ids = lt.iterator(normalToStandardList(ids))
    for ide in disc_ids:
      artist_pos = lt.isPresent(catalog["artists"], ide)
      artist_obj = lt.getElement(catalog["artists"], artist_pos)
      nation = artist_obj["Nationality"]
      if nation.strip() == "":
        continue
      check = lt.isPresent(nationalities, nation)
      if check == 0:
        lt.addLast(nationalities, nation)

    iter_nationalities = lt.iterator(nationalities)
    for nationality in iter_nationalities:
      if nationality not in counter.keys():
        counter[nationality] = 1
      else:
        counter[nationality] += 1

  sorted_count = {k: v for k, v in sorted(counter.items(), key=lambda item: item[1], reverse=True)[:10]}
  return sorted_count

def showNationWork(catalog, nation_count):
    """
    Retorna la información de la nación con un mayor número de obras
    """
    nation = list(nation_count.keys())[0]
    count = nation_count[nation]
    nation_art = lt.newList("ARRAY_LIST")
    iter_artworks = lt.iterator(catalog["artworks"])
    artworks_pos = lt.newList()
    for ix, artwork in enumerate(iter_artworks):
      ids = artwork["ConstituentID"].strip("[]").split()
      disc_ids = normalToStandardList(ids)
      iter_ids = lt.iterator(disc_ids)
      names = lt.newList()
      for ide in iter_ids:
        ide = ide.strip(",")
        name = searchID(catalog, ide)
        lt.addLast(names, name)
      iter_names = lt.iterator(names)
      str_names = ""
      for name in iter_names:
        str_names += f", {name}"
      str_names = str_names.strip(", ")
      artwork["ArtistsNames"] = str_names
      pos = ix + 1
      lt.addLast(artworks_pos, pos)

    objs = lt.newList("ARRAY_LIST")
    first_three = lt.iterator(lt.subList(artworks_pos, 1, 3))
    last_three = lt.iterator(lt.subList(artworks_pos, lt.size(artworks_pos) - 3, 3))
    for pos in first_three:
      lt.addLast(objs, lt.getElement(catalog["artworks"], pos))
    for pos in last_three:
      lt.addLast(objs, lt.getElement(catalog["artworks"], pos))

    return objs

def selectArtworks(catalog, years, area):
  """
  Selecciona unas obras de arte entre los años pasados por parámetro hasta que se llene el área disponible
  """
  begin_year, end_year = [int(year) for year in years.split("-")]
  final_area = int(area)

  area_sum = 0
  proposed_works = lt.newList("ARRAY_LIST")
  iter_artworks = lt.iterator(catalog["artworks"])
  for artwork in iter_artworks:
    work_date = artwork["Date"].strip("()-c. ")
    try:
      work_date = abs(int(work_date))
    except:
      continue
    if work_date in range(begin_year, end_year + 1):
      diameter = artwork["Diameter (cm)"].strip()
      width = artwork["Width (cm)"].strip()
      height = artwork["Height (cm)"].strip()
      if diameter == "" and width != "" and height != "":
        work_area = calculateArea(width=width, height=height)
      elif diameter != "":
        work_area = calculateArea(diameter=diameter)
      if work_area + area_sum <= final_area:
        area_sum += work_area
        lt.addLast(proposed_works, artwork)
  return proposed_works



# Funciones utilizadas para comparar elementos dentro de una lista

def compareartists(artist_id, artist):
  if (artist_id in artist['ConstituentID']):
    return 0
  return -1

def compareartworks(artwork1, artwork2):
  if artwork1 is artwork2:
    return 1
  return 0

def cmpArtistsByBeginDate(artist1, artist2):
  """
  Devuelve verdadero (True) si el 'BeginDate' de artist1 es menores que el de artist2
    Args:
    artist1: informacion de la primera obra que incluye su valor 'BeginDate'
    artist2: informacion de la segunda obra que incluye su valor 'BeginDate'
  """
  if artist1['BeginDate'] == None:
    artist1['BeginDate'] = 0
  if artist2['BeginDate'] == None:
    artist2['BeginDate'] = 0
  if int(artist1['BeginDate']) < int(artist2['BeginDate']):
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

def cmpArtistsByNationality(artist1, artist2):
  """
  Verdadero si las nacionalidades son iguales.
  """
  if artist1 == artist2:
    return 1
  return 0

# Funciones de ordenamiento

def sortArtistsByBeginDate(catalog, implementation, initial_date, end_date):
  """
  Ordena los artistas en el rango de fechas dispuesto
  """
  new_artists = filterArtistsByBeginDate(catalog, initial_date, end_date)
  algorithm = sort_algo[int(implementation)]
  start_time = time.process_time()
  sorted_entries = algorithm.sort(new_artists, cmpArtistsByBeginDate)
  stop_time = time.process_time()
  elapsed_time_mseg = round((stop_time - start_time) * 1000, 3)
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
  iter_artists = lt.iterator(catalog["artists"])

  initial_date = datetime.strptime(initial_date, "%Y")
  end_date = datetime.strptime(end_date, "%Y")
  pos_to_delete = lt.newList()
  iter_artists = lt.iterator(catalog["artists"])
  new_artists = lt.newList()
  for artist in iter_artists:
    if artist["BeginDate"] == None or artist["BeginDate"] == "0":
      continue
    artist_date = datetime.strptime(artist["BeginDate"].strip(), "%Y")
    if initial_date <= artist_date <= end_date:
      lt.addLast(new_artists, artist)
  return new_artists


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

def normalToStandardList(normal_lst, implementation="ARRAY_LIST", cmpfunc=None):
  """
  Transforms a Python list into a DISClib list
  """
  new_list = lt.newList(implementation, cmpfunc)
  for element in normal_lst:
    lt.addLast(new_list, element)
  return new_list

def dictToStandardList(dictionary, feature="keys", implementation="ARRAY_FUNCTION", cmpfunc=None):
  """
  Transforms a feature of a dictionary into a DISClib list
  """
  dict_list = lt.newList(implementation, cmpfunc)
  if feature == "keys":
    normal_list = list(dictionary.keys())
  elif feature == "values":
    normal_list = list(dictionary.valus())
  for element in normal_list:
    lt.addLast(dict_list, element)
  return dict_list

def searchID(catalog, artist_id):
  """
  Devuelve el nombre del artista que tiene ese ID asignado
  """
  pos = lt.isPresent(catalog["artists"], artist_id)
  name = lt.getElement(catalog["artists"], pos)["DisplayName"]
  if pos != 0:
    return name
  return ""

def calculateArea(diameter="", width="", height=""):
  """
  Cálculo del área de una obra
  """
  if diameter == "":
    return float(width) * float(height)
  else:
    return 2 * pi * (float(diameter) / 2) ** 2