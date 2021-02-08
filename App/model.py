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


# Construccion de modelos
def create_videos(filepath: str):
    """
    Args:
        filepath: path to the file to be read from
    Returns:
        Arraylist that represents videos with a tuple of:
            arraylist with video_id,trending_date,title,channel_title,category_id,publish_time,views,likes,dislikes,comment_count,
                thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed,description,country
            linkedlist with tags
    """
    videos = lt.newList(datastructure='ARRAY_LIST')
    if filepath is not None:
        input_file = csv.DictReader(open(filepath, encoding="utf-8"),
                                    delimiter=',')
        for line in input_file:
            add_video(videos, line)
    return videos


def base_sort_function(videos, i, parameter_indexes):
    """
    Auxiliary function to createIndexOrder.
    Args:
        videos: arraylist of videos
        i: index of the video
        parameter_indexes: tuple of indexes of parameters
    Returns:
    A tuple with the values that correspond to the parameter_indexes in the index i of videos.
    """
    return tuple([videos['elements'][i][0]['elements'][x] for x in parameter_indexes if x < 16])


def create_index_order(videos, order_indexes):
    """
    'Tags' parameter not supported.
    Args:
        videos: arraylist of videos
        order_indexes: list of indexes of parameters
    Returns:
    A list of indexes that indicate an order of videos based on the referenced parameters.
    """
    indexes = [i for i in range(0, len(videos['elements']))]
    sort_key = lambda a: base_sort_function(videos, a, order_indexes)
    indexes.sort(key=sort_key)
    return indexes


# Funciones para agregar informacion al catalogo
def add_video(videos, line):
    """
    Auxiliary function to create_videos which adds to videos an arraylist with most parameters and a linked list
    with the information of the tags of the videos.
    Args:
        videos: arraylist of videos
        line: OrderedDict with information of the videos
    Returns:
        None
    """
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
