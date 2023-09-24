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

import DISClib as DLIB
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.DataStructures import arraylist as al
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk

assert cf

"""
Se define la estructura de un catálogo de la FIFA. El catálogo tendrá
tres listas, una para los partidos, otra para los goleadores y otra para los penales.
"""

# Construccion del modelo


def new_data_structs_match():
    """
    Inicializa el catálogo de la FIFA. 
    Crea listas vacias para guardar la información de los partidos, goleadores y penales.
    Retorna el catalogo inicializado.

    """
    # creando y configurando el ADT list para almacenar los partidos
    # creando y configurando los atributos que componen un partido

    catalogo = {'partidos': None,
                'goleadores': None,
                'penales': None,
                'date': None,
                'home_team': None,
                'away_team': None,
                'home_score': None,
                'away_score': None,
                'tournment': None,
                'city': None,
                'country': None,
                'neutral': None,
                'own_goal': None,
                'penalty': None,
                'team': None,
                'scorer': None,
                'minute': None,
                'winner': None,
                }

    catalogo['partidos'] = lt.newList(
        'ARRAY_LIST', cmpfunction=compare_partidos)
    catalogo['goleadores'] = lt.newList(
        'ARRAY_LIST', cmpfunction=compare_goleadores)
    catalogo['penales'] = lt.newList(
        'ARRAY_LIST', cmpfunction=compare_penales)

    return catalogo


# Funciones para agregar informacion al modelo

def add_partido(catalogo, partido):
    """
    Función para agregar nuevos partidos a la lista
    """
    # Se adiciona el partido a la lista de partidos

    p = new_partido(partido['date'], partido['home_team'], partido['away_team'],
                    partido['home_score'], partido['away_score'], partido['tournament'],
                    partido['city'], partido['country'], partido['neutral'])

    lt.addLast(catalogo['partidos'], partido)

    return catalogo


def add_goleadores(catalogo, goleador):
    """
    Función para agregar nuevos elementos a la lista
    """
    # Se adiciona el goleador a la lista de goleadores

    g = new_goleador(goleador['date'], goleador['home_team'], goleador['away_team'],
                     goleador['team'], goleador['scorer'], goleador['minute'],
                     goleador['own_goal'], goleador['penalty'])

    lt.addLast(catalogo['goleadores'], goleador)

    return catalogo


def add_penales(catalogo, penales):
    """
    Función para agregar nuevos elementos a la lista
    """
    # Se adiciona la tanda de penales a la lista de penales

    pe = new_penales(penales['date'], penales['home_team'], penales['away_team'],
                     penales['winner'])

    lt.addLast(catalogo['penales'], penales)

    return catalogo

# Funciones para creacion de datos


def new_partido(date, home_team, away_team, home_score, away_score, tournament, city, country, neutral):
    """
    Crea una nueva estructura para modelar los datos
    """
    partido = {'date': "", "home_team": "", 'away_team': "", 'home_score': 0, 'away_score': 0,
               'tournament': "", 'city': "", 'country': "", 'neutral': None}

    partido['date'] = date
    partido['home_team'] = home_team
    partido['away_team'] = away_team
    partido['home_score'] = home_score
    partido['away_score'] = away_score
    partido['tournament'] = tournament
    partido['city'] = city
    partido['country'] = country
    partido['neutral'] = neutral

    return partido

    pass


def new_goleador(date, home_team, away_team, team, scorer, minute, own_goal, penalty):
    """
    Crea una nueva estructura para modelar los datos
    """
    goleador = {'date': "", "home_team": "", 'away_team': "", 'team': "",
                'scorer': "", 'minute': 0, 'own_goal': None, 'penalty': None}

    goleador['date'] = date
    goleador['home_team'] = home_team
    goleador['away_team'] = away_team
    goleador['team'] = team
    goleador['scorer'] = scorer
    goleador['minute'] = minute
    goleador['own_goal'] = own_goal
    goleador['penalty'] = penalty

    return goleador

    pass


def new_penales(date, home_team, away_team, winner):
    """
    Crea una nueva estructura para modelar los datos
    """
    penales = {'date': "", "home_team": "", 'away_team': "", 'winner': ""}

    penales['date'] = date
    penales['home_team'] = home_team
    penales['away_team'] = away_team
    penales['winner'] = winner
    
    return penales

    pass


# Funciones de consulta

def get_1(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    pass

def get_2(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    pass

def get_3(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    pass

def get_4(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    pass



def partidos_size(catalogo):
    """
    Retorna el tamaño de la lista de los partidos
    """
    partidos = catalogo['partidos']
    return lt.size(partidos)


def goleadores_size(catalogo):
    """
    Retorna el tamaño de la lista de los goleadores
    """
    goles = catalogo['goleadores']
    return lt.size(goles)


def penales_size(catalogo):
    """
    Retorna el tamaño de la lista de los penales
    """
    penales = catalogo['penales']
    return lt.size(penales)

# Implementación de requerimientos

def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista


def compare_date(date1, date2):
    """
    Función encargada de comparar dos datos
    """
    if (date1.float == date2.lower()):
        return 0
    elif (date1.lower() > date2.lower()):
        return 1
    return -1

    pass


def compare_score(home_score_1, away_score_1, home_score_2, away_score_2):

    return


def compare_minuto_gol(minute1, minute2):

    return


def compare_nombre_goleador(nombre1, nombre2):

    return


# Funciones de comparación para el ordenamiento


def compare_partidos(partido1, partido2):

    return 


def compare_goleadores(goleador1_, goleador2):

    return


def compare_penales(penales1,penales2):

    return


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
   
    pass

# Funciones de ordenamiento

def sortpartidos(catalogo):
    """
    Función encargada de ordenar la lista con los datos
    """

    merg.sort(catalogo['partidos'], compare_partidos)

    pass


def sortgoleadores(catalogo):
    """
    Función encargada de ordenar la lista con los datos
    """

    merg.sort(catalogo['goleadores'], compare_goleadores)

    pass


def sortpenales(catalogo):
    """
    Función encargada de ordenar la lista con los datos
    """

    merg.sort(catalogo['penales'], compare_goleadores)

    pass
