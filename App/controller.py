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
from DISClib.ADT import list as lt


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo del museo

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtists(catalog)
    loadArtworks(catalog)
    

def loadArtists(catalog):
    """
    Carga los artistas del archivo. 
    """
    artistsfile = cf.data_dir + 'Datos/Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)
    
def loadArtworks(catalog):
    """
    Carga las obras del archivo. 
    """
    artworksfile = cf.data_dir + 'Datos/Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)

# Funciones de ordenamiento

def sortArtists(catalog):
    
    model.sortArtist(catalog)

def sortArtworks(catalog):
    
    model.sortArtworks(catalog)

# Funciones de consulta sobre el catálogo

def getArtistsbyYear(catalog, year1, year2):
    """
    Retorna los artistas entre los años dados
    """
    ArtistbyYear = model.getArtistsbyYear(catalog, year1, year2)
    Artistsort =sortArtists(ArtistbyYear)
    return(Artistsort)


def getArtworksbyDate(catalog, date1, date2):
    """
    Retorna las obras entre las fechas dadas
    """
    ArtworksbyYear = model.getArtistsbyYear(catalog, date1, date2)
    Artworksort =sortArtists(ArtworksbyYear)
    return(Artworksort)

def PurchaseArtworks(obras):
    """
    Retorna las obras adquiridas por compra
    """
    purchased = model.PurchaseArtworks(obras)
    print (purchased)

def ArtworksByArtist(catalog, artistname):

    artistID = model.ArtistID (catalog, artistname)
    artworkslist = model.ArtworksByID (catalog, artistID)
    
    return artworkslist 


def MediumInArtwork(artworksByID):
    
    mediums = model.MediumInArtworks(artworksByID)

    return mediums


def FreqMediums(mediums, Artworkslist):

    freq = model.freqMedium (mediums, Artworkslist)

    return freq


def MostUsedMedium(freq, Mediums):

    MostUsedMedium=model.MostUsedMedium(freq, Mediums)

    return MostUsedMedium


def MUMList(MostUsedMedium, Artworkslist):
    MUMList = model.MUMList(MostUsedMedium, Artworkslist)

    return MUMList



def printMUMList(catalog, MUMList):
    i = 1
    size = lt.size(MUMList)

    while i <= size:
        artwork = lt.getElement(MUMList, i)

        print('Titulo: ' + artwork['Title'])
        print(" ")
        print('Artista(s): ')

        CA = artwork["ConstituentID"]
        CA2=CA.lstrip("[")
        CA3 = CA2.rstrip("]")
        coAutors = CA3.split(", ")
        
        j=0

        for A in coAutors:
            autorID = coAutors[j]
            ArtistName = model.ArtistNameByID (catalog, autorID)

            print(ArtistName)

            j+=1

        print(" ")
        print('Fecha de creación: ' + artwork['Date'])
        print(" ")
        print('Técnica(s) usada(s): ' + artwork['Medium'])
        print(" ")
        print("Dimensiones: " + artwork["Dimensions"])
        print(" ")

        i+=1