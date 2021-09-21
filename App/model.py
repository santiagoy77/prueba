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
    art = newArtwork(artwork['Title'], artwork['ObjectID'], artwork['ConstituentID'], artwork['Medium'], artwork['Circumference (cm)'], 
                    artwork['Depth (cm)'], artwork['Diameter (cm)'], artwork['Height (cm)'], artwork['Length (cm)'], artwork['Weight (kg)'], 
                    artwork['Width (cm)'], artwork['Seat Height (cm)'], artwork['Duration (sec.)'], artwork['Date'], artwork['DateAcquired'],artwork['CreditLine'], artwork['Dimensions'], artwork['Department'])
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

def newArtwork(name, id, constituentid, medium, circunferencia, profundidad, diametro, altura, largo, peso, ancho, altura_asiento, duracion, 
                fecha, fecha_compra, adquisicion, dimensions, departamento):
    """
    Esta estructura almancena las obras utilizadas.
    """
    artwork = {'Title': '', 'ObjectID': '', 'ConstituentID': '', 'Medium': '','Circumference (cm)': '','Depth (cm)': '','Diameter (cm)': '',
                'Height (cm)': '','Length (cm)': '','Weight (kg)': '','Width (cm)': '','Seat Height (cm)': '','Duration (sec.)': '',
                'Date': '','DateAcquired': '','CreditLine': '','Department':''}
    artwork['Title'] = name
    artwork['ObjectID'] = id
    artwork['ConstituentID'] = constituentid
    artwork['Medium'] = medium
    artwork['Dimensions'] = dimensions
    artwork['Circumference (cm)'] = circunferencia
    artwork['Depth (cm)'] = profundidad
    artwork['Diameter (cm)'] = diametro
    artwork['Height (cm)'] = altura
    artwork['Length (cm)'] = largo
    artwork['Weight (kg)'] = peso
    artwork['Width (cm)'] = ancho
    artwork['Seat Height (cm)'] = altura_asiento
    artwork['Duration (sec.)'] = duracion
    artwork['Date'] = fecha
    artwork['DateAcquired'] = fecha_compra
    artwork['CreditLine'] = adquisicion
    artwork['Department'] = departamento
    
    return artwork

# Funciones de consulta


def getArtistsbyYear(catalog, year1, year2):
    
    artists = catalog['artists']
    ArtistsbyYear = lt.newList()
    size = lt.size(artists)
    for cont in range(1,size+1):
        artist = lt.getElement(artists, cont)
        year=artist['BeginDate']
        if year1<=int(year)<=year2:
            lt.addLast(ArtistsbyYear, artist)
       
    return ArtistsbyYear

def getArtworksbyDate(catalog, date1, date2):
    
    artworks = catalog['artworks']

    ArtworksByYear = lt.newList()
    
    size = lt.size(artworks)

    fecha1 = date1.split("-")
    fecha2 = date2.split("-") 

    for cont in range(1,size+1):
        artwork = lt.getElement(artworks, cont)
        date = artwork['DateAcquired'].split("-")

        if (fecha1[0])<=(date[0])<=(fecha2[0]):
            lt.addLast(ArtworksByYear, artwork)

    size2 = lt.size(ArtworksByYear)

    for cont in range(1,size2+1):
        artwork = lt.getElement(ArtworksByYear, cont)
        
        date = artwork['DateAcquired'].split("-")

        if fecha1[0]==date[0]:
            if date[1]<fecha1[1]:
                pos = lt.isPresent(ArtworksByYear, artwork)
                lt.deleteElement(ArtworksByYear,pos)

        if fecha2[0]==date[0]:
            if date[1]>fecha1[1]:
                pos = lt.isPresent(ArtworksByYear, artwork)
                lt.deleteElement(ArtworksByYear,pos)

        if fecha1[0]==date[0] and fecha1[1==date[1]]:
            if date[2]<=fecha1[2]:
                pos = lt.isPresent(ArtworksByYear, artwork)
                lt.deleteElement(ArtworksByYear,pos)
        
        if fecha2[0]==date[0] and fecha2[1==date[1]]:
            if date[2]>=fecha1[2]:
                pos = lt.isPresent(ArtworksByYear, artwork)
                lt.deleteElement(ArtworksByYear,pos)
                  


    return ArtworksByYear

def PurchaseArtworks(obras):

    purchased = lt.newList()
    size = lt.size(obras)
    for count in range(1, size+1):
        obra = lt.getElement(obras, count)
        adquisicion = obra["CreditLine"]
        if adquisicion == "Purchase":
            lt.addLast(purchased, obra)

    return purchased




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
    artworksByID = lt.newList('ARRAY_LIST')
    i=1
    
    while i <= lt.size(artworks):
        artwork = lt.getElement(artworks, i)
        catalogID = artwork["ConstituentID"]
        
        if artistID in catalogID:
            lt.addLast(artworksByID, artwork)
        
        i+=1    

    return artworksByID


def ArtistNameByID (catalog, artistID):
    
    Artists = catalog["artists"]
    i=1
    
    while i <= lt.size(Artists):
        artist = lt.getElement(Artists, i)
        ID = artist["ConstituentID"]
        
        if ID == artistID:
            name = artist["DisplayName"]
            i=1+lt.size(Artists)

            return name

        i+=1    
        


def freqMedium (Mediums, Artworkslist):

    MediumListReps=lt.newList('ARRAY_LIST')
    size=lt.size(Artworkslist)

    for n in range(1,size+1):
        
        artwork = lt.getElement(Artworkslist, n)
        
        Medium=artwork["Medium"]

        lt.addLast(MediumListReps, Medium)

    freq = lt.newList('ARRAY_LIST')
    
    size2 = lt.size(Mediums)
    size3 = lt.size(MediumListReps)

    for Medium in range(1, 1+size2):
        y=lt.getElement(Mediums, Medium)
        i=0

        for count in range(1, 1+size3):
            x=lt.getElement(MediumListReps, count)

            if y == x:
                i+=1
        
        lt.addLast(freq, i)

    return freq


def MediumInArtworks (artworksByID):
    
    mediums = lt.newList('ARRAY_LIST')
    i=0
    
    while i <= lt.size(artworksByID):
        artwork = lt.getElement(artworksByID, i)
        Medium = artwork["Medium"]
        pos=lt.isPresent(mediums, Medium)

        if pos == 0:
            lt.addLast(mediums, Medium)

        i+=1  
   
    return (mediums)


def MostUsedMedium(freq, Mediums):

    max = 0
    size=lt.size(freq)

    for i in range(1, 1+size):
        f = lt.getElement(freq, i)

        if f > max:
            max = f
        
    pos = lt.isPresent(freq, max)

    MostUsedMedium = lt.getElement(Mediums, pos)

    return MostUsedMedium


def MUMList(MostUsedMedium, Artworkslist):

    MUMList = lt.newList('ARRAY:LIST')
    size = lt.size(Artworkslist)

    for i in range(1, 1+size):
        Artwork = lt.getElement(Artworkslist, i)
        Medium = Artwork["Medium"]

        if Medium == MostUsedMedium:
            lt.addLast(MUMList, Artwork)
            

    return MUMList    

def ArtworksByDepto (catalog, Depto):
    
    artworks = catalog["artworks"]
    artworksByDepto = lt.newList('ARRAY_LIST')
    i=1
    
    while i <= lt.size(artworks):
        artwork = lt.getElement(artworks, i)
        catalogDepto = artwork["Department"]
        
        if Depto in catalogDepto:
            lt.addLast(artworksByDepto, artwork)
        
        i+=1    

    return artworksByDepto


def tamanoObras (artworksByDepto):
    size = lt.size(artworksByDepto)
    dimensionList = lt.newList()

    for i in range(1, 1+size):
        artwork = lt.getElement(artworksByDepto, i)

        circunferencia = artwork["Circumference (cm)"]
        profundidad = artwork["Depth (cm)"]
        diametro = artwork["Diameter (cm)"]
        altura = artwork["Height (cm)"]
        largo = artwork["Length (cm)"]
        ancho = artwork["Width (cm)"]

        dimensiones = 0   
        
        if altura != "":
            altura = float(altura)/100

            if circunferencia != "":
                circunferencia = float(circunferencia)/100
                dimensiones = (3.14159*(circunferencia/(2*3.14159))**2)*altura

            elif diametro != "":
                diametro = float(diametro)/100
                dimensiones = (3.14159*(diametro/(2))**2)*altura

            elif profundidad != "" and ancho != "":
                profundidad = float(profundidad)/100
                ancho = float(ancho)/100
                dimensiones = profundidad*ancho*altura

            elif largo != "" and ancho != "":
                largo = float(largo)/100
                ancho = float(ancho)/100
                dimensiones = profundidad*ancho*altura

            elif profundidad != "":
                profundidad = float(profundidad)/100
                dimensiones = profundidad*altura

            elif largo != "":
                largo = float(largo)/100
                dimensiones = profundidad*altura
            
            elif ancho != "":
                ancho = float(ancho)/100
                dimensiones = ancho*altura


        elif largo != "" and ancho != "":
            largo = float(largo)/100
            ancho = float(ancho)/100
            dimensiones = profundidad*ancho 

        elif circunferencia != "":
            circunferencia = float(circunferencia)/100
            dimensiones = (3.14159*(circunferencia/(2*3.14159))**2)

        elif diametro != "":
            diametro = float(diametro)/100
            dimensiones = (3.14159*(diametro/(2))**2)
        

        lt.addLast(dimensionList, dimensiones)

    return dimensionList


def pesoObras (artworksByDepto): 
    size = lt.size(artworksByDepto)
    pesoObras = lt.newList()

    for i in range(1, 1+size):
        artwork = lt.getElement(artworksByDepto, i)

        peso = artwork["Weight (kg)"]

        lt.addLast(pesoObras, peso)

    return pesoObras


def precioObras (dimensiones, pesoObras):
    size = lt.size(dimensiones)
    precioObras = lt.newList()

    for i in range(1, 1+size):
        
        peso = lt.getElement(pesoObras, i)
        dimension = lt.getElement(dimensiones, i)

        if dimension != 0:
            precio = dimension*72   

        if peso != "":
            peso = float(peso)

            if peso == 0 and dimension == 0:
                precio = 42        
            elif peso >= dimension:
                precio = peso*72
            elif peso < dimension:
                precio = dimension*72

        if peso == "" and dimension == 0:
            precio = 42
        
        lt.addLast(precioObras, precio)
        
    return precioObras

def sumaTotal(lista):
    size = lt.size(lista)
    total = 0
    
    for i in range(1, size+1):
        elemento = lt.getElement(lista, i)

        if elemento != "":
            total=total+float(elemento)
    
    return total
        

# Funciones utilizadas para comparar elementos dentro de una lista

def compareartistyears(year1, year2):
    return (int(year1['BeginDate']) < int(year2['BeginDate']))

def compareartworkyears(year1, year2):
    return (int(year1['Date']) > int(year2['Date']))

# Funciones de ordenamiento

def sortArtist(artists):
    resul=sa.sort(artists, compareartistyears)
    return(resul)
    
    

def sortArtworks(catalog):
    sa.sort(catalog['artworks'], compareartworkyears)
