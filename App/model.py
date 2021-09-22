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
    catalog = {'artists_BeginDate': None,
               'artworks_DateAcquired': None,
               'artists_artworks':None}
    
    catalog['artists_BeginDate'] = lt.newList('ARRAY_LIST', cmpfunction=compare_artists)
    catalog['artworks_DateAcquired'] = lt.newList('ARRAY_LIST', cmpfunction=compare_artworks)
    catalog['artists_artworks'] = lt.newList('ARRAY_LIST')

    return catalog

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    # Se añade el artista al final de la lista de artistas en el catálogo.
    lt.addLast(catalog['artists_BeginDate'], artist)

def addArtwork(catalog, artwork):
    # Se añade la obra de arte al final de la lista de obras de arte en el catálogo.
    lt.addLast(catalog['artworks_DateAcquired'], artwork)
    artists = artwork['ConstituentID']
    for artist in artists:
        addArtworkArtist(catalog, artist, artwork)
    
def addArtworkArtist(catalog, artist, artwork):
    artist_artwork = catalog['artists_artworks']
    posartist = lt.isPresent(artist_artwork, artist)
    if posartist > 0:
        author = lt.getElement(artist_artwork, posartist)
    else:
        author = newArtist(artist)
        lt.addLast(artist_artwork, author)
    lt.addLast(artist_artwork['Medium'],artwork )

# Funciones para creacion de datos

# =============================================================================
# def match_ids(catalog):
#     for i in lt.iterator(catalog['artists_BeginDate']):
#     ids = {'artist_id': artist_id, 'artwork_id': artwork_id}
#     return ids
# =============================================================================
def newArtist(artist):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    author = {'name': "", "Medium": None,  "average_rating": 0}
    author['name'] = artist
    author['Medium'] = lt.newList('ARRAY_LIST')
    return author

# Funciones de consulta
def rangoArtists(catalog, anio1, anio2):
    artists = catalog["artists_BeginDate"].copy()
    start_time = time.process_time()
    start=float("inf")
    pos=1
    while pos<=lt.size(artists):
        if int(lt.getElement(artists,pos)["BeginDate"])>=anio1:
            start=pos
            break
        pos+=1
    initial=start
    num=0
    while start<=lt.size(artists):
        if int(lt.getElement(artists,start)["BeginDate"])<=anio2:
            num+=1
        else:
            break
        start+=1
    answ = lt.subList(artists,initial,num)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return answ
    
def rangoArtworks(catalog, fecha1, fecha2):
    artworks = catalog["artworks_DateAcquired"].copy()
    start_time = time.process_time()
    start=float("inf")
    pos=1
    while pos<=lt.size(artworks):
        if lt.getElement(artworks,pos)["DateAcquired"] != "":
            if datetime.strptime(lt.getElement(artworks,pos)["DateAcquired"], '%Y-%m-%d').date()>=datetime.strptime(fecha1, '%Y-%m-%d').date():
                start=pos
                break
        pos+=1
    initial=start
    num=0
    while start<=lt.size(artworks):
        if datetime.strptime(lt.getElement(artworks,start)["DateAcquired"], '%Y-%m-%d').date()<=datetime.strptime(fecha2, '%Y-%m-%d').date():
            num+=1
        else:
            break
        start+=1
    answ = lt.subList(artworks,initial,num)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return answ

def id_artists(catalog, author):
    id_=0
    for i in lt.iterator(catalog['artists_BeginDate']):
        if catalog['artists_BeginDate']['DisplayName']==author:
            id_ = catalog['artists_BeginDate']['ConstituentID']
            break
    return id_

def id_artworks(catalog, author):
    """

    Returns
    -------
    list_ : TYPE
        Lista de las obras de un artista determinado.
    """
    id_=id_artists(catalog, author)
    list_=lt.newList('ARRAY_LIST')
    for i in lt.iterator(catalog['artworks_DateAcquired']):
        if id_ in i['ConstituentID']:                
            lt.addLast(list_, i)
    return list_

def list_artworks_artist(artworks_artist):
    mediums = lt.newList('ARRAY_LIST')
    for i in lt.iterator(artworks_artist):
        if i['Medium'] not in mediums:
            medio = lt.newList('ARRAY_LIST')
            
    return 

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

def sortArtworks_DateAcquired(catalog):
    sub_list = catalog["artworks_DateAcquired"].copy()
    start_time = time.process_time()
    sorted_list= mer.sort(sub_list, cmpArtworkByDateAcquired)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list

def sortArtists_BeginDate(catalog):
    sub_list = catalog["artists_BeginDate"].copy()
    start_time = time.process_time()
    sorted_list= mer.sort(sub_list, compare_artists)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list

# =============================================================================
# def sortArtists_ConstituentID(catalog):
#     sub_list = catalog["artists_ConstituentID"].copy()
#     start_time = time.process_time()
#     sorted_list= mer.sort(sub_list)
#     stop_time = time.process_time()
#     elapsed_time_mseg = (stop_time - start_time)*1000
#     return elapsed_time_mseg, sorted_list
# 
# =============================================================================
# Nosotros elejimos el algoritmo: sa.sort, ins.sort, mer.sort, quc.sort, sel.sort.

