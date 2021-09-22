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
from prettytable import PrettyTable
assert cf

"""
La vista se encarga de la interacción con el usuario
Presenta el menú de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    """
    Imprime las opciones del menú.
    """
    print("\nMenú de opciones:\n")
    print("1- Cargar información en el catálogo.")
    print("2- Listar cronológicamente los artistas.")
    print("3- Listar cronológicamente las adquisiciones.")
    print("4- Clasificar las obras de un artista por técnica.")
    print("5- Clasificar las obras por la nacionalidad de sus creadores.")
    print("6- Transportar obras de un departamento.")
    print("7- Proponer una nueva exposición en el museo.")
    print("0- Detener la ejecución del programa.")

def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()

def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

catalog = None

"""
Menú principal
"""
while True:
    error = "Por favor ingrese un número entero entre 0 y 7."
    printMenu()
    try:
        inputs = int(input('Seleccione una opción para continuar: \n'))
    except:
        print(error)
        continue
    if inputs == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        artist=controller.sortArtists_BeginDate(catalog)
        artwork=controller.sortArtworks_DateAcquired(catalog)
        catalog["artists_BeginDate"]=artist[1]
        catalog["artworks_DateAquired"]=artwork[1]
        print('Número de artistas en el catálogo: ',
              str(lt.size(catalog['artists_BeginDate'])))
        print('Número de obras de arte en el catálogo: ',
              str(lt.size(catalog['artworks_DateAquired'])))
        print("Se demoro: ",str(artist[0]))
        print('Últimos tres artistas cargados:\n')
        for i in [-2,-1,0]:
            print(str(lt.getElement(catalog['artists_BeginDate'],i)))
        print("Se demoro: ",str(artwork[0]))
        print('Últimas tres obras de arte cargadas:\n')
        for i in [-2,-1,0]:
            print(str(lt.getElement(catalog['artworks_DateAquired'],i)))

    elif inputs==2:
        anio1=int(input("Digite un año inicial: "))
        anio2=int(input("Digite un año final: "))
        result=controller.rangoArtists(catalog, anio1, anio2)
        print("======================== Req No. 1 Inputs ========================")
        print("Artistas nacidos entre ",str(anio1)," y ",str(anio2)),"."
        print("======================== Req No. 1 Respuesta ========================")
        print("Hay ",str(lt.size(result))," artistas nacidos entre ",
              str(anio1)," y ",str(anio2)),"."
        print('\nPrimeros y últimos tres artistas nacidos en el rango de años:\n')
        answ = PrettyTable(['Nombre','Nacimiento','Fallecimiento'
                            ,'Nacionalidad','Género'])
        for i in [1,2,3,-2,-1,0]:        
            answ.add_row([lt.getElement(result,i)['DisplayName'],
                          lt.getElement(result,i)['BeginDate'],
                          lt.getElement(result,i)['EndDate'],
                          lt.getElement(result,i)['Nationality'],
                          lt.getElement(result,i)['Gender']])
        answ._max_width = {'Nombre':40}
        print(answ)

    elif inputs==3:
        fecha1=input("Ingrese una fecha inicial en formato AAAA-MM-DD: ")
        fecha2=input("Ingrese una fecha final en formato AAAA-MM-DD: ")
        result = controller.rangoArtworks(catalog, fecha1, fecha2)
        num_artists = 5 # TODO: FALTA
        num_purchased = 5 # TODO: Falta
        print("======================== Req No. 1 Inputs ========================")
        print("Obras adquiridas entre ",fecha1," y ",fecha2)
        print("======================== Req No. 1 Respuesta ========================")
        print("El MoMA adquirió ",str(lt.size(result))," obras entre ",fecha1,
              " y ",fecha2," con ",str(num_artists),
              " artistas, de las cuales compró ",str(num_purchased))
        print('\nPrimeras y últimas tres obras adquiridas en el rango de fechas:\n')
        answ = PrettyTable(['Título','Artista(s)','Fecha','Medio',
                            'Dimensiones'])
        for i in [1,2,3,-2,-1,0]:        
            answ.add_row([lt.getElement(result,i)['Title'],
                          lt.getElement(result,i)['ConstituentID'], # TODO: Artista
                          lt.getElement(result,i)['DateAcquired'],
                          lt.getElement(result,i)['Medium'],
                          lt.getElement(result,i)['Dimensions']])
        answ._max_width = {'Título':40,'Artista(s)':40,'Fecha':20,'Medio':40,
                            'Dimensiones':40}
        print(answ)

    elif (inputs>3) and (inputs<8):
        print("Este requerimiento aún no se ha implementado.")
    elif inputs >= 8:
        print(error)
    else:
        sys.exit(0)
sys.exit(0)
