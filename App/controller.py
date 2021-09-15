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
 """

import config as cf
import model
import csv
import datetime


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog(implementation):
  """
  Llama la función de inicialización del catálogo del modelo
  """
  catalog = model.newCatalog(implementation)
  return catalog

# Funciones para la carga de datos
def loadData(catalog):
  """
  Carga los datos de los archivos y cargar los datos en la
  estructura de datos
  """
  loadArtwork(catalog)
  # loadArtists(catalog)

def loadArtwork(catalog):
  """
  Carga los obras del archivo.  Por cada obra se toman sus artistas y por
  cada uno de ellos, se crea en la lista de artistas, a dicho artista y una
  referencia a la obra que se está procesando.
  """
  artworks_file = f"{cf.data_dir}/MoMA/Artworks-utf8-5pct.csv"
  input_file = csv.DictReader(open(artworks_file, encoding='utf-8'))
  for artwork in input_file:
    model.addArtwork(catalog, artwork)

def loadArtists(catalog):
  """
  Carga los datos de los artistas del archivo y los agrega a la lista de artistas
  """
  artists_info_file = f"{cf.data_dir}/MoMA/Artists-utf8-5pct.csv"
  input_file = csv.DictReader(open(artists_info_file, encoding='utf-8'))
  for artist_info in input_file:
    model.addArtistInfo(catalog, artist_info)

def cmpArtworkByDateAcquired(artwork1, artwork2):

  """ Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork2 Args: artwork1: informacion de la primera obra que incluye su valor 'DateAcquired' artwork2:
      artwork1: informacion de la primera obra que incluye su valor 'DateAcquired' 
      artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired'
  """
  dateacquired1= artwork1["DateAcquired"]
  dateacquired2= artwork2["DateAcquired"]
  if(dateacquired1 < dateacquired2):
    return 1
  else:
    return 0
    
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
