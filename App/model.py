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
from datetime import datetime
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as mer
from DISClib.Algorithms.Sorting import quicksort as quc
from DISClib.Algorithms.Sorting import selectionsort as sel
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

def compare_artists(artist1,artist):
    if artist1.lower() in artist["artists"].lower():
        return 0
    return -1

def compare_artworks():
    pass

def cmpArtworkByDateAcquired(artwork1, artwork2):
    """
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork2 Args:
        artwork1: informacion de la primera obra que incluye su valor 'DateAcquired'
        artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired'
    """
    if artwork1["DateAcquired"]=="" or artwork2["DateAcquired"]=="":
        if artwork1["DateAcquired"]=="":
            return -1
        else:
            return 0
    elif datetime.strptime(artwork1["DateAcquired"], '%Y-%m-%d').date()<datetime.strptime(artwork2["DateAcquired"], '%Y-%m-%d').date():
        return -1
    return 0

# Funciones de ordenamiento

def sortArtworks(catalog, size,sor):
    sub_list = lt.subList(catalog['artworks'], 1, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    if sor==1:
        sorted_list= sa.sort(sub_list, cmpArtworkByDateAcquired)
    elif sor==2:
        sorted_list= ins.sort(sub_list, cmpArtworkByDateAcquired)
    elif sor==3:
        sorted_list= mer.sort(sub_list, cmpArtworkByDateAcquired)
    elif sor==4:
        sorted_list= quc.sort(sub_list, cmpArtworkByDateAcquired)
    elif sor==5:
        sorted_list= sel.sort(sub_list, cmpArtworkByDateAcquired)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list


