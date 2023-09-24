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
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu


assert cf

# from tabulate import tabulate

# import traceback

default_limit = 1000
sys.setrecursionlimit(default_limit*10)


"""
La vista se encarga de la interacción con el usuario.

Presenta el menu de opciones y por cada seleccion se hace la solicitud al controlador para ejecutar la
operación solicitada.
"""


def newController():
    """
    Se crea una instancia del controlador
    """
    control = controller.new_controller()
    return control


def print_menu_usuario():
    
    """
    Menú de selección de usuario
    """
    
    print("Bienvenido!")
    print("Estás a un paso de adentrarte a la historia de las competiciones organizadas por la FIFA.")
    print("Para gozar de una mejor experiencia, por favor indica tú tipo de usuario:")
    
    print ("1- Soy Estudiante")
    print ("2- Soy parte del Equípo Docente")
    
def print_menu_Estudiante(): 
    
    """
    Menú de Estudiante
    """
    
    print("Bienvenido Colega")
    
    print("1- Cargar la información de las competiciones")
    
    print("2- Análisis de los ultimos partidos de algún equipo")
    print("3- Análisis de los primeros goles anotados por un jugador")
    print("4- Análisis de los partidos disputados por un equipo en un tiempo específico")
    print("5- Análisis de la información de los torneos")
    print("6- Análisis de la capacidad goleadora de un jugador específico")
    print("7- Análisis de los mejores equipos de los torneos")
    print("8- Análisis de los mejores goleadores de los torneos")
    print("9- Análisis del desempeño historico entre selecciones")
    
    print("0- Salir")    
    
def print_menu_Docente(): 
    
    """
    Menú del equípo docente
    """
    
    print("Bienvenid@(s) Daniel, Miguel y/o Alejandra ")    
    
    print("1- Cargar la información de las competiciones")
    
    print("2- Análisis de los ultimos partidos de algún equipo")
    print("3- Análisis de los primeros goles anotados por un jugador")
    print("4- Análisis de los partidos disputados por un equipo en un tiempo específico")
    print("5- Análisis de la información de los torneos")
    print("6- Análisis de la capacidad goleadora de un jugador específico")
    print("7- Análisis de los mejores equipos de los torneos")
    print("8- Análisis de los mejores goleadores de los torneos")
    print("9- Análisis del desempeño historico entre selecciones")
    
    print("0- Salir")


def loadData1(control, tamaño):
    """
    Solicita al controlador que cargue los datos en el modelo de los goles.
    """
    results = controller.load_data(control,tamaño)[0]
   
    return results

def loadData2(control,tamaño):
    """
    Solicita al controlador que cargue los datos en el modelo, la carga de los partidos.
    """
    goalscorers = controller.load_data(control, tamaño)[1]
    return goalscorers

def loadData3(control,tamaño):
    """
    Solicita al controlador que cargue los datos en el modelo, la carga de los penales.
    """
    shootouts = controller.load_data(control, tamaño)[2]
    return shootouts


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass

def escoger_tamaño(tamaño):
    
    if str(tamaño) == "a":
        tamaño_escogido = tamaño
    elif str(tamaño) == "b":
        tamaño_escogido = tamaño
    else:
        print("Opción errónea, vuelva a elegir.\n")
        sys.exit(0) 

    return tamaño_escogido

def escoger_tipo(tipo):
    
    if str(tipo) == "a":
        tipo_escogido = tipo
    elif str(tipo) == "b":
        tipo_escogido = tipo
    else:
        print("Opción errónea, vuelva a elegir.\n")
        sys.exit(0) 
            
    return tipo_escogido

# Se crea el controlador asociado a la vista
control = newController()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    
    #ciclo del menu
    while working:
        
        print_menu_usuario()
        inputs = input('Seleccione una opción para continuar\n')
        
        if int(inputs) == 1:
            
            print_menu_Estudiante()
            inputs = input('Seleccione una opción para continuar\n')
             
            if int(inputs) == 1:
                print("Cargando información de los archivos ....\n")
                data = loadData1(control, tamaño= 'small'),loadData2(control,tamaño='small'), loadData3(control, tamaño ='small')
                print('se han cargandos los siguientes datos: ')
                
                print(data[0],'Resultados de los partidos.')
                print(data[1],'Goleadores.')
                print(data[2],'Goles anotados desde el punto de penal.')
                
            elif int(inputs) == 2:
                print_req_1(control)
            
            elif int(inputs) == 3: 
                print_req_2(control)
            elif int(inputs) == 4:
                print_req_3(control)
                
            elif int(inputs) == 5:
                print_req_4(control)
            
            elif int(inputs) == 6: 
                print_req_5(control)
            
            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                print_req_7(control)
                
            elif int(inputs) == 9:
                print_req_8(control)
                
            elif int(inputs) == 0: 
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
                sys.exit(0)     
                                  
        elif int(inputs) == 2:
            
            print_menu_Docente()
            inputs = input('Seleccione una opción para continuar\n')
            
            if int(inputs) == 1:
                print('¿Qué tipo de lista quiere que implemente el programa?\n'+'a. ArrayList\n' + 'b. SingleLinked\n')
                tipo = input('Seleccione una opción para continuar\n')
                tipo_escogido = escoger_tipo(tipo)
                print('¿Qué cantidad de datos desea cargar?\n'+
                      'a. large\n' + 'b. small\n')
                tamaño = input('Seleccione una opción para continuar\n')
                tamaño_escogido = escoger_tamaño(tamaño)
                print("Cargando información de los archivos ....\n")
                data = loadData1(control,tamaño_escogido),loadData2(control, tamaño_escogido),loadData3(control,tamaño_escogido)
                print('se han cargandos los siguientes datos: ')
                print(data[0],'Resultados de los partidos.')
                print(data[1],'Goleadores.')
                print(data[2],'Goles anotados desde el punto de penal.')
                
            elif int(inputs) == 2:
                print_req_1(control)
            
            elif int(inputs) == 3: 
                print_req_2(control)
            
            elif int(inputs) == 4:
                print_req_3(control)
                
            elif int(inputs) == 5:
                print_req_4(control)
            
            elif int(inputs) == 6: 
                print_req_5(control)
            
            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                print_req_7(control)
                
            elif int(inputs) == 9:
                print_req_8(control)
                
            elif int(inputs) == 0: 
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
                sys.exit(0)                
                
        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
            
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)


