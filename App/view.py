"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Encontrar buenos videos por categoría y país")
    print("3- Encontrar video tendencia por categoría")
    print("4- Encontrar video tendencia por país")
    print("5- Buscar los videos con más Likes")
    print("0- Salir")
    
catalog = None

# trabajando
def initCatalog(tipo_lista):
    """
    Inicializa el catalogo de videos
    """
    if tipo_lista == 1:
        return controller.initCatalogArray()
    elif tipo_lista == 2:
        return controller.initCatalogSingle()
    else:
        return None
    


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

"""
def printAuthorData(author):
    if author:
        print('Autor encontrado: ' + author['name'])
        print('Promedio: ' + str(author['average_rating']))
        print('Total de libros: ' + str(lt.size(author['books'])))
        for book in lt.iterator(author['books']):
            print('Titulo: ' + book['title'] + '  ISBN: ' + book['isbn'])
    else:
        print('No se encontro el autor')


def printBestBooks(books):
    size = lt.size(books)
    if size:
        print(' Estos son los mejores libros: ')
        for book in lt.iterator(books):
            print('Titulo: ' + book['title'] + '  ISBN: ' +
                  book['isbn'] + ' Rating: ' + book['average_rating'])
    else:
        print('No se encontraron libros')

catalog = None
"""

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        tipo_lista = int(input("Elija el tipo de lista que quiere crear (Presione 1 para ARRAY_LIST o 2 para SINGLE_LINKED): "))
        catalog = initCatalog(tipo_lista)
        if catalog == None:
            print("No ha seleccionado una opcion valida")
        else:
            print("Cargando información de los archivos...")
            loadData(catalog)
            print('Videos cargados: ' + str(lt.size(catalog['title'])))
            print('Canales cargados: ' + str(lt.size(catalog['channel_title'])))
            for keys in catalog['channel_title']:
                print(keys)

    elif int(inputs[0]) == 2:
        print ("Encontrar buenos videos por categoría y país")

    elif int(inputs[0]) == 3:
        print ("Encontrar video tendencia por categoría")

    elif int(inputs[0]) == 4:
        print('Encontrar videos tendencias por pais')
    
    elif int(inputs[0]) == 5:
        print('Buscar los videos con mas likes')

    else:
        sys.exit(0)
        
sys.exit(0)
