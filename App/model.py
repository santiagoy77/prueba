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

import datetime
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as mrgsort
from DISClib.Algorithms.Sorting import quicksort as quicks
import time
assert cf
"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    catalog = {'artworks': None,
               'artists': None}

    catalog['artworks'] = lt.newList()
    catalog['artists'] = lt.newList('SINGLE_LINKED',
                                    cmpfunction=compareartists)
    return catalog

# Funciones para creacion de datos

def nuevoArtwork(name,dateacquired,constituentid,date,medium,dimensions,department,creditline,classification):
    if dateacquired:
        datel=dateacquired.split('-')
        dateacquired2=datetime.date(int(datel[0]),int(datel[1]),int(datel[2]))
    else:
        dateacquired2=datetime.date(1,1,1)
    
    artwork={'name':'','dateacquired':'','constituentid':'','date':'','medium':'','dimensions':'','department':'','creditline':'','classification':''}
    artwork['name']=name
    artwork['dateacquired']=dateacquired2
    artwork['constituentid']=constituentid
    artwork['date']=date
    artwork['medium']=medium
    artwork['dimensions']=dimensions
    artwork['department']=department
    artwork['creditline']=creditline
    artwork['classification']=classification 
    return artwork

def nuevoArtist(name,begindate,enddate,nationality,gender,constituentid):
    artist={'name':'','begindate':'','enddate':'','nationality':'','gender':'','constituentid':''}
    artist['name']=name
    artist['begindate']=begindate
    artist['enddate']=enddate
    artist['nationality']=nationality
    artist['gender']=gender
    artist['constituentid']=constituentid
    return artist

# Funciones para agregar informacion al catalogo

def addArtwork(catalog, artwork):
    nuevo=nuevoArtwork(artwork['Title'],artwork['DateAcquired'],artwork['ConstituentID'],artwork['Date'],artwork['Medium'],artwork['Dimensions'],artwork['Department'],artwork['CreditLine'],artwork['Classification'])
    lt.addLast(catalog['artworks'],nuevo)

def addArtist(catalog, artist): 
    nuevo=nuevoArtist(artist['DisplayName'],artist['BeginDate'],artist['EndDate'],artist['Nationality'],artist['Gender'],artist['ConstituentID'])
    lt.addLast(catalog['artists'],nuevo)


# Funciones de consulta

def getUltimos(lista):
    posicionl=lt.size(lista)-2
    return lt.subList(lista, posicionl, 3)

def fechaCompArtistas(art1, art2):
    return art1["edad"] < art2["edad"]

def artistasCronologico(lista, inicio, final):
    artistas = lista["artists"]
    cont = 0
    retorno = lt.newList()
    for artista in range(lt.size(artistas)):
        llave = lt.getElement(artistas, artista)
        edad = int(llave["begindate"])
        nombre = llave["name"]
        muerte = int(llave["enddate"])
        genero = llave["gender"]
        nacionalidad = llave["nationality"]

        if edad != 0 and edad != None and edad >= inicio and edad <= final:
            agregar = {"nombre" : nombre, "edad" : edad, "muerte" : muerte, "genero" : genero, "nacionalidad" : nacionalidad}
            lt.addLast(retorno, agregar)
    
    sa.sort(retorno, fechaCompArtistas)

    return retorno

def obrasCronologicoacq(lista,inicio,final,metodo,sizesublista): 
    obras = lista["artworks"]
    retorno = lt.newList()
    for i in range(round(lt.size(obras)*sizesublista)):
        llave = lt.getElement(obras, i)
        dateacquired = llave["dateacquired"]
        name = llave["name"]
        medium = llave["medium"]
        dimensions = llave["dimensions"]
        if  dateacquired >= inicio and dateacquired <= final:
            agregar = {"name" : name, "dateacquired" : dateacquired, "medium" : medium, "dimensions" : dimensions}
            lt.addLast(retorno, agregar)
    StartTime=time.process_time()
    if metodo=='ShellSort':
        sa.sort(retorno, cmpArtworkByDateAcquired)
    elif metodo=='InsertionSort':
        ins.sort(retorno, cmpArtworkByDateAcquired)
    elif metodo=='MergeSort':
        mrgsort.sort(retorno, cmpArtworkByDateAcquired)
    elif metodo=='':
        quicks.sort(retorno,cmpArtworkByDateAcquired)
    StopTime=time.process_time()
    TimeMseg=(StopTime-StartTime)*1000
    return retorno


# Funciones utilizadas para comparar elementos dentro de una lista

def compareartists(artist1,artist2):
    if (artist1.lower() in artist2['name'].lower()):
        respuesta=0
    else: 
        respuesta=-1
    return respuesta
    

def cmpArtworkByDateAcquired(artwork1,artwork2): 
    """
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork2
    Args:
    artwork1: informacion de la primera obra que incluye su valor 'DateAcquired'
    artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired'
    """
    return artwork1['dateacquired']<artwork2['dateacquired']
