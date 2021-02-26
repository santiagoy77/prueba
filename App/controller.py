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
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

index_by_id = {
    'video_id': 0,
    'trending date': 1,
    'title': 2,
    'channel_title': 3,
    'category_id': 4,
    'publish_time': 5,
    'views': 6,
    'likes': 7,
    'dislikes': 8,
    'comment_count': 9,
    'thumbnail_link': 10,
    'comments_disabled': 11,
    'ratings_disabled': 12,
    'video_error_or_removed': 13,
    'description': 14,
    'country': 15
}

# Inicialización del Catálogo de libros

# Funciones para la carga de datos

def initCreate_videos():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    videos = model.create_videos(filepath="Data/videos-small.csv")
    return videos

def initLista_tags():
    tags=model.lista_tags("Data/category-id.csv")
    return tags
# Funciones de ordenamiento
def order_by_Views(videos, size, algorithm = 'shell'):
    return model.inefficient_ordering(videos, size, algorithm)

def doSortingTests(videos, flag):
    algorithms = ['shell', 'insertion', 'selection', 'quick', 'merge']
    sizes = [(2**x)*1000 for x in range(0,10)]
    matrix = [[0.0]*5 for x in range(0,10)]
    i = 0
    j = 0
    with open('Data/tests.csv', 'r') as testsfile:
        content = testsfile.readline()
        content = testsfile.readline()
        while content:
            content = content.replace('\n','')
            content = content.split(sep=',')
            for n in content:
                if n:
                    matrix[i][j] = float(n)
                    j += 1
            if (j == 5):
                i+= 1
                j = 0
            content = testsfile.readline()
        testsfile.close()
    while flag[0] and i < 10:
        while flag[0] and j < 5:
            k = 0
            time = 0
            while k < 3 and flag[1]:
                result = model.inefficient_ordering(videos, sizes[i], algorithms[j])
                time += result[0] / 3
                k += 1
            if k == 3:
                matrix[i][j] = time
                print("Algorithm",algorithms[j],"size",sizes[i],"executd in average time", round(time,2), "ms")
                j += 1
        j = 0
        i += 1
    with open('Data/tests.csv', 'w') as testsfile:
        result = 'shell,insertion,selection,quick,merge\n'
        i = 0
        j = 0
        while i < 10:
            while j < 4 and matrix[i][j]:
                result += str(round(matrix[i][j], 2))+','
                j += 1
            if not matrix[i][j]:
                break
            result += str(round(matrix[i][j], 2)) + '\n'
            j = 0
            i += 1
        testsfile.write(result)
        testsfile.close()


# Funciones de consulta sobre el catálogo
