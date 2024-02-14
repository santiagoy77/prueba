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
from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller()
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Listar las últimas N ofertas de trabajo según su país y nivel de experticia")
    print("3- Listar las últimas N ofertas de trabajo por empresa y ciudad")
    print("4- Consultar las ofertas que publicó una empresa durante un periodo especifico de tiempo")
    print("5- Consultar las ofertas que se publicaron en un país durante un periodo de tiempo")
    print("6- Consultar las ofertas que se publicaron en una ciudad durante un periodo de tiempo")
    print("7- Clasificar las N ciudades con mayor número de ofertas de trabajo por experticia entre un rango de fechas")
    print("8- Clasificar los N países con mayor número de ofertas de trabajo por divisa")
    print("9- Identificación de los países con mayor y menor ofertas de trabajo en un rango de fechas")
    print("0- Salir")


def load_data(control, size):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    jobs_size, skills_size, employment_types_size, multilocations_size = (
    controller.load_data(control,
                        size + '-jobs.csv',
                        size + '-skills.csv',
                        size + '-employment_types.csv',
                        size + '-multilocations.csv'))
    return jobs_size, skills_size, employment_types_size, multilocations_size


def print_jobs(control, pos, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    jobs = controller.load_jobs(control, pos, id)
    headers = {'Título de la oferta': [],
               'Calle': [],
               'Ciudad': [],
               'Código de país': [],
               'Texto de dirección': [],
               'Marker icon': [],
               'Tipo de lugar de trabajo': [],
               'Nombre de compañía': [],
               'URL de compañía': [],
               'Tamaño de compañía': [],
               'Nivel de experiencia': [],
               'Publicación': [],
               'Entrevista remota': [],
               'Abierto a contratar ucranianos': [],
               'Id': [],
               'Oferta lanzada': []}
    for job in lt.iterator(jobs):
        headers['Título de la oferta'.append(job['title'])]
        headers['Calle'.append(job['street'])]
        headers['Ciudad'.append(job['city'])]
        headers['Código de país'.append(job['country_code'])]
        headers['Texto de dirección'.append(job['address_text'])]
        headers['Marker icon'.append(job['marker_icon'])]
        headers['Tipo de lugar de trabajo'.append(job['workplace_type'])]
        headers['Nombre de compañía'.append(job['company_name'])]
        headers['URL de compañía'.append(job['company_url'])]
        headers['Tamaño de compañía'.append(job['company_size'])]
        headers['Nivel de experiencia'.append(job['experience_level'])]
        headers['Publicación'.append(job['published_at'])]
        headers['Entrevista remota'.append(job['remote_interview'])]
        headers['Abierto a contratar ucranianos'.append(job['open_to_hire_ukrainians'])]
        headers['Id'.append(job['id'])]
        headers['Oferta lanzada'.append(job['display_offer'])]

    print(tabulate(headers, headers='keys'))

def print_skills(control, pos, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    skills = controller.load_skills(control, pos, id)
    headers = {'Campo': [],
               'Nivel experticia': [],
               'Título de la oferta': []}
    for skill in lt.iterator(skills):
        headers['Campo'.append(skill['field'])]
        headers['Nivel experticia'.append(skill['level'])]
        headers['Empresa que publica'.append(skill['title'])]

    print(tabulate(headers, headers='keys'))

def print_employments_types(control, pos, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    employments_types = controller.load_employments_types(control, pos, id)
    headers = {'Tipo de empleo': [],
               'Título de la oferta': [],
               'Divisa': [],
               'Salario mínimo': [],
               'Salario máximo': []}
    for employment_type in lt.iterator(employments_types):
        headers['Tipo de empleo'.append(employment_type['type'])]
        headers['Título de la oferta'.append(employment_type['title'])]
        headers['Divisa'.append(employment_type['currency'])]
        headers['Salario mínimo'.append(employment_type['min_salary'])]
        headers['Salario máximo'.append(employment_type['max_salary'])]

    print(tabulate(headers, headers='keys'))

def print_multilocations(control, pos, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    multilocations = controller.load_multilocationss(control, pos, id)
    headers = {'Tipo de empleo': [],
               'Título de la oferta': [],
               'Divisa': [],
               'Salario mínimo': [],
               'Salario máximo': []}
    for multilocation in lt.iterator(multilocations):
        headers['Tipo de empleo'.append(multilocation['location'])]
        headers['Título de la oferta'.append(multilocation['city'])]
        headers['Divisa'.append(multilocation['title'])]

    print(tabulate(headers, headers='keys'))

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


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            size = input('Tamaño del archivo CSV: ')
            data = load_data(control, size)
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
