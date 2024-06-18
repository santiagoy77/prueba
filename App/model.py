import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import mergesort as merg
import csv

def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data_structs = {
        "data": lt.newList("SINGLE_LINKED", compare),
        "years": {}
    }
    return data_structs

def add_data(data_structs, row):
    """
    Función para agregar nuevos elementos a la lista
    """
    lt.addLast(data_structs["data"], row)
    year = row["Año"]
    if year not in data_structs["years"]:
        data_structs["years"][year] = lt.newList("SINGLE_LINKED", compare)
    lt.addLast(data_structs["years"][year], row)

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    data = data_structs["data"]
    for elem in lt.iterator(data):
        if elem["id"] == id:
            return elem
    return None

def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    return lt.size(data_structs["data"])

def get_years(data_structs):
    """
    Retorna los años disponibles en los datos
    """
    return list(data_structs["years"].keys())

def get_year_data(data_structs, year):
    """
    Retorna los datos de un año específico
    """
    if year in data_structs["years"]:
        year_data = data_structs["years"][year]
        sorted_year_data = merg.sort(year_data, sort_criteria)
        first_3 = lt.subList(sorted_year_data, 1, 3)
        last_3 = lt.subList(sorted_year_data, lt.size(sorted_year_data) - 2, 3)
        return first_3 + last_3
    return None

def sort_criteria(data_1, data_2):
    """
    Criterio de ordenamiento por Año y Código actividad económica
    """
    if data_1["Año"] != data_2["Año"]:
        return data_1["Año"] < data_2["Año"]
    return data_1["Código actividad económica"] < data_2["Código actividad económica"]

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    return data_1 == data_2
