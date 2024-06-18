import config as cf
import sys
import controller
from tabulate import tabulate
import traceback

def new_controller():
    """
    Se crea una instancia del controlador
    """
    return controller.new_controller()

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("0- Salir")

def load_data(control):
    """
    Carga los datos
    """
    try:
        control = controller.new_controller()
        filename = 'Salida_agregados_renta_juridicos_AG_large.csv'
        controller.load_data(control, filename)
        total_rows = controller.data_size(control)
        print(f"Total de filas cargadas: {total_rows}")
        for year in controller.get_years(control):
            print(f"Año: {year}")
            data = controller.get_year_data(control, year)
            if data:
                print(tabulate(data, headers=["Año", "Código actividad económica", "Nombre actividad económica", "Código sector económico", "Nombre sector económico", "Código subsector económico", "Nombre subsector económico", "Total ingresos netos", "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor"], tablefmt="grid"))
    except Exception as e:
        print("Error al cargar los datos:", e)
        traceback.print_exc()

def print_req_1(control):
    """
    Función que imprime la solución del Requerimiento 1 en consola
    """
    try:
        result = controller.req_1(control)
        print(tabulate(result, headers=["Año", "Código actividad económica", "Nombre actividad económica", "Código sector económico", "Nombre sector económico", "Código subsector económico", "Nombre subsector económico", "Total ingresos netos", "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor"], tablefmt="grid"))
    except Exception as e:
        print("Error al ejecutar el requerimiento 1:", e)
        traceback.print_exc()

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
            load_data(control)
        elif int(inputs) == 2:
            print_req_1(control)
        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
