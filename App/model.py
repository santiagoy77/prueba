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
import csv
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa

assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""


# Construccion de modelos
def addVideos(filename: str):
    """
    Crea un arraylist de referencias por vídeo a:
        arraylist con video_id,trending_date,title,channel_title,category_id,publish_time,views,likes,dislikes,comment_count,
            thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description,country
        linkedlist de tags
    """
    videos = lt.newList(datastructure='ARRAY_LIST')
    if filename is not None:
        input_file = csv.DictReader(open(filename, encoding="utf-8"),
                                    delimiter=',')
        for line in input_file:
            addVideo(videos, line)
    return videos


# Funciones para agregar informacion al catalogo
def addVideo(videos, line):
    categories = lt.newList(datastructure='ARRAY_LIST')
    tags = lt.newList()
    for element in line.items():
        if element[0] != 'tags':
            lt.addLast(categories, element[1])
        else:
            tagl = element[1].replace('"', '').split('|')
            for tag in tagl:
                lt.addLast(tags, tag)
    lt.addLast(videos, (categories, tags))
# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
