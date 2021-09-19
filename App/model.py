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
    a = newArtist(artist['DisplayName'], artist['ConstituentID'], artist['Nationality'], artist['Gender'], artist['BeginDate'], artist['EndDate'])
    lt.addLast(catalog['artists'], a)

def addArtwork(catalog, artwork):
    """
    Adiciona una obra a la lista de obras
    """
    art = newArtwork(artwork['Title'], artwork['ObjectID'], artwork['ConstituentID'], artwork['Medium'])
    lt.addLast(catalog['artworks'], art)

# Funciones para creacion de datos
def newArtist(name, id, nacionality, gender, begin, end):
    """
    Esta estructura almancena los artistas utilizados.
    """
    artist = {'DisplayName': '', 'ConstituentID': '', 'Nationality': '','Gender': '','BeginDate': '','EndDate': '' }
    artist['DisplayName'] = name
    artist['ConstituentID'] = id
    artist['Nationality'] = nacionality
    artist['Gender'] = gender
    artist['BeginDate'] = begin
    artist['EndDate'] = end
    return artist

def newArtwork(name, id, constituentid, medium):
    """
    Esta estructura almancena las obras utilizadas.
    """
    artist = {'Title': '', 'ObjectID': '', 'ConstituentID': ''}
    artist['Title'] = name
    artist['ObjectID'] = id
    artist['ConstituentID'] = constituentid
    artist['Medium'] = medium
    return artist

# Funciones de consulta



def getArtistsbyYear(catalog, year1, year2):
    
    artists = catalog['artists']
    ArtistsbyYear = lt.newList()
    i=0
    for a in artists:
        artist = lt.getElement(artists, i)
        year=artist['BeginDate']
        if year1<int(year)<year2:
            lt.addLast(ArtistsbyYear, artist)
        i+=1
    return ArtistsbyYear


def ArtistID (catalog, artistname):

    artists = catalog['artists']     
    i=0
    flag=True

    while i <= lt.size(artists) and flag == True:
        artist = lt.getElement(artists, i)
        
        Name = artist['DisplayName'] 
        
        if Name == artistname:
            artistID = artist["ConstituentID"]
            flag=False
            return artistID
    
        i+=1

        if i > lt.size(artists):
            return("No se he encontrado el artista especificado")



def ArtworksByID (catalog, artistID):
    
    artworks = catalog["artworks"]
    artworksByID = lt.newList()
    i=0
    
    while i <= lt.size(artworks):
        artwork = lt.getElement(artworks, i)
        catalogID = artwork["ConstituentID"]
        
        if artistID in catalogID:
            lt.addLast(artworksByID, artwork)
        
        i+=1    

    return artworksByID


def MediumInArtworks (artworksByID):
    
    mediums = []
    i=0
    
    while i <= lt.size(artworksByID):
        artwork = lt.getElement(artworksByID, i)
        Medium = artwork["Medium"]
       
        lt.addLast(mediums, Medium)

        i+=1  
   
    print(mediums)
    return mediums

# Funciones utilizadas para comparar elementos dentro de una lista

def compareartistyears(year1, year2):
    return (int(year1['BeginDate']) > int(year2['BeginDate']))

def compareartworkyears(year1, year2):
    return (int(year1['Date']) > int(year2['Date']))

# Funciones de ordenamiento

def sortArtist(catalog):
    sa.sort(catalog['artist'], compareartistyears)

def sortArtworks(catalog):
    sa.sort(catalog['artworks'], compareartworkyears)
