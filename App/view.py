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
    """
    Imprime las opciones del menú.
    """
    print("Bienvenido")
    print("1- Cargar información en el catálogo.")
    print("2- Listar cronológicamente los artistas.")
    print("3- Listar cronológicamente las adquisiciones.")
    print("4- Clasificar las obras de un artista por técnica.")
    print("5- Clasificar las obras por la nacionalidad de sus creadores.")
    print("6- Transportar obras de un departamento.")
    print("7- Proponer una nueva exposición en el museo.")
    print("0- Detener la ejecución del programa.")

def initCatalog(lista: int):
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog(lista)


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

catalog = None

"""
Menu principal
"""
while True:
    error = "Por favor ingrese un número entero entre 0 y 7."
    printMenu()
    try:
        inputs = int(input('Seleccione una opción para continuar\n'))
    except:
        print(error)
        continue
    if inputs == 1:
        print("Cargando información de los archivos ....")
        lista=int(input("Digite 1 si quiere crear un array list o 0 si quiere crear un linked list: "))
        catalog = initCatalog(lista)
        loadData(catalog)
        print('Número de artistas en el catálogo: ' + str(lt.size(catalog['artists'])))
        print('Número de obras de arte en el catálogo: ' + str(lt.size(catalog['artworks'])))
        print('Últimos tres artistas cargados:\n')
        for i in [-3,-2,-1]:
            print(str(lt.getElement(catalog['artists'],i)))
        print('Últimas tres obras de arte cargadas:\n')
        for i in [-3,-2,-1]:
            print(str(lt.getElement(catalog['artworks'],i)))
    elif (inputs>1) and (inputs<8):
        print("Este requerimiento aún no se ha implementado.")
    elif inputs >= 8:
        print(error)
    else:
        sys.exit(0)
sys.exit(0)
