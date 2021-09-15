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
Se define la estructura de un catálogo de obras de arte. 
El catálogo tendrá dos listas, una para las obras de arte, 
otra para los artistas de estas.
"""

# Construccion de modelos

def newCatalog(lista: int):
    """
    Inicializa el catálogo de obras de arte. 
    Crea listas vacías con los siguientes própositos:
    Para guardar las obras de arte
    Para guardar los autores
    Quizá luego se añaden más listas con los autores ordenados o lo que se necesite.
    """
    catalog = {'artists': None,
               'artworks': None}
    if lista==1:
        catalog['artists'] = lt.newList('ARRAY_LIST',
                                        cmpfunction=compare_artists)
        catalog['artworks'] = lt.newList('ARRAY_LIST',
                                        cmpfunction=compare_artworks)
    else:
        catalog['artists'] = lt.newList('SINGLE_LINKED',
                                        cmpfunction=compare_artists)
        catalog['artworks'] = lt.newList('SINGLE_LINKED',
                                        cmpfunction=compare_artworks)
    return catalog

## NOTA: Se están cargando los datos de forma muy simple. 
# Se está pensando en la primera entrega, no en los requerimientos. 
# Pronto se estructurará el catálogo de mejor manera.

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    # Se añade el artista al final de la lista de artistas en el catálogo.
    lt.addLast(catalog['artists'], artist)

def addArtwork(catalog, artwork):
    # Se añade la obra de arte al final de la lista de obras de arte en el catálogo.
    lt.addLast(catalog['artworks'], artwork)

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def compare_artists():
    pass

def compare_artworks():
    pass

# Funciones de ordenamiento