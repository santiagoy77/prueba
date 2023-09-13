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
import time
import csv
csv.field_size_limit(2147483647)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    control = {
        "model" : None
    }
    control["model"] = model.new_data_structs()
    return control

# Funciones para la carga de datos

def load_data(control):
    
    """
    Carga los datos del reto
    """
    filenameR = "football/results-utf8-small.csv"
    filenameG = "football/goalscorers-utf8-small.csv"
    filenameS = "football/shootouts-utf8-small.csv"
    #TODO: Realizar la carga de datos
    dtos = control["model"]
    resultss  = loaddata(dtos,filenameR, "results")
    resultss1  = loaddata(dtos,filenameG , "goalscorers")
    resultss2  = loaddata(dtos , filenameS , "shootouts"  )
    sort(resultss)
    return resultss , resultss1 , resultss2

# Funciones de ordenamiento

def loaddata(dtos , filename, poci):
    file = cf.data_dir + filename
    input_file = csv.DictReader(open(file , encoding='utf-8'))
    for date in input_file:
        model.add_dataR(dtos,date,poci)
    return dtos[poci]

def sizedtos(dtos):
    r1 , r2, r3, = load_data(dtos)
    return model.dtosSize(r1), model.dtosSize(r2) , model.dtosSize(r3)

def primeros(dtos):
    r1 , r2, r3, = load_data(dtos)     
    return model.sublista(r1, 1 , 3) , model.sublista(r2, 1 , 3) , model.sublista(r3, 1 , 3)

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
