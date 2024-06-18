import config as cf
import model
import csv

def new_controller():
    """
    Crea una instancia del modelo
    """
    control = {
        "model": model.new_data_structs()
    }
    return control

def load_data(control, filename):
    """
    Carga los datos del reto
    """
    data_structs = control["model"]
    filepath = cf.data_dir + filename
    with open(filepath, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            model.add_data(data_structs, row)
    return data_structs

def data_size(control):
    """
    Retorna el tamaño de la lista de datos
    """
    return model.data_size(control["model"])

def get_years(control):
    """
    Retorna los años disponibles en los datos
    """
    return model.get_years(control["model"])

def get_year_data(control, year):
    """
    Retorna los datos de un año específico
    """
    return model.get_year_data(control["model"], year)

def req_1(control):
    """
    Retorna el resultado del requerimiento 1
    """
    return model.req_1(control["model"])
