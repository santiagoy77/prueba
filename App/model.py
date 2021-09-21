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

def newCatalog():
    """
    Inicializa el catálogo de obras de arte. 
    Crea listas vacías con los siguientes própositos:
    Para guardar las obras de arte
    Para guardar los autores
    Quizá luego se añaden más listas con los autores ordenados o lo que se necesite.
    """
    catalog = {'artists': None,
               'artworks': None,
               'artists_chronologically': None}
    
    catalog['artists'] = lt.newList('ARRAY_LIST', cmpfunction=compare_artists)
    catalog['artworks'] = lt.newList('ARRAY_LIST', cmpfunction=compare_artworks)
    catalog['artists_chronologically'] = lt.newList('ARRAY_LIST', cmpfunction=compare_artworks)
    
    return catalog

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    # Se añade el artista al final de la lista de artistas en el catálogo.
    lt.addLast(catalog['artists'], artist)

def addArtwork(catalog, artwork):
    # Se añade la obra de arte al final de la lista de obras de arte en el catálogo.
    lt.addLast(catalog['artworks'], artwork)

# Funciones para creacion de datos

# Funciones de consulta
def rangoArtists(catalog, anio1, anio2):
    artists = catalog["artists"].copy()
    start_time = time.process_time()
    n=1
    while n<=lt.size(artists):
        if int(lt.firstElement(artists)["BeginDate"])<anio1:
            lt.removeFirst(artists)
        else:
            n=lt.size(artists)
        n+=1
    n=1
    while n<=lt.size(artists):
        if int(lt.lastElement(artists)["BeginDate"])>anio2:
            lt.removeLast(artists)
        else:
            n=lt.size(artists)
        n+=1
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return artists

def rangoArtworks(catalog, anio1, anio2):
    sub_list = catalog["artworks"].copy()
    n=1
    while n<=lt.size(artists):
        if lt.firstElement(artists)["BeginDate"]<anio1:
            artists=lt.removeFirst(artists)
        else:
            n=lt.size(artists)
        n+=1
    n=1
    while n<=lt.size(artists):
        if lt.lastElement(artists)["BeginDate"]>anio2:
            artists=lt.removeLast(artists)
        else:
            n=lt.size(artists)
        n+=1
    return artists

# Funciones utilizadas para comparar elementos dentro de una lista

def compare_artists(artist1,artist2):
    if artist1["BeginDate"]<=artist2["BeginDate"]:
        return -1
    else:
        return 0

def compare_artworks():
    pass

def cmpArtworkByDateAcquired(artwork1:dict , artwork2:dict)->int:
    """
    Compara dos obras de arte por la fecha en la que fueron adquiridas, 
    'DateAcquired'.
    
    Si el 'DateAcquired' de una obra de arte es vacío, la obra se toma como 
    la más antigua.

    Parámetros
    ----------
    artwork1 : dict
        Informacion de la primera obra que incluye su valor 'DateAcquired'.
    artwork2 : dict
        Informacion de la segunda obra que incluye su valor 'DateAcquired'.

    Retorno
    -------
    int
        0 si artwork1 fue adquirido más recientemente que artwork2.
        -1 si artwork2 fue adquirido más recientemente que artwork1.
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

def sortArtworks(catalog):
    sub_list = catalog["artworks"].copy()
    start_time = time.process_time()
    sorted_list= mer.sort(sub_list, cmpArtworkByDateAcquired)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list

def sortArtists(catalog):
    sub_list = catalog["artists"].copy()
    start_time = time.process_time()
    sorted_list= mer.sort(sub_list, compare_artists)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list

# Nosotros elejimos el algoritmo: sa.sort, ins.sort, mer.sort, quc.sort, sel.sort.

