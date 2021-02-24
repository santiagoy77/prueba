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
import time
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
        catalog = controller.initCatalog(tipo_lista)
        print("cargando los archivos... Esto puede tardar un poco")
        loadData(catalog)
        if catalog == None:
            print("No ha seleccionado una opcion valida")
        else:
            print("Cargando información de los archivos...")
            print('Videos cargados: ' + str(lt.size(catalog['title'])))

    elif int(inputs[0]) == 2:
        print ("Encontrar buenos videos por categoría y país")
        size = int(input("¿De que tamaño quiere la lista?: "))
        if size > lt.size(catalog['title']):
            print("El numero de muestra seleccionado, excede el tamaño de la cantidad total de elementos que hay")
        else:
            print("Elija el tipo de algoritmo de ordenamiento iterativo con el cual desea ordenar el catalogo de videos por vistas...")
            orden = int(input("Presione 1 para escoger Shellsort, 2 para Selectionsort o 3 para Insertionsort: "))
            (a,b) = controller.sortVideos(catalog,size,orden)
            print("la lista ordenada es",b,"y el tiempo que ha tardado el proceso es:",a,"segundos")
    elif int(inputs[0]) == 3:
        print ("Encontrar video tendencia por categoría")

    elif int(inputs[0]) == 4:
        print('Encontrar videos tendencias por pais')
    
    elif int(inputs[0]) == 5:
        print('Buscar los videos con mas likes')

    else:
        sys.exit(0)
        
sys.exit(0)
