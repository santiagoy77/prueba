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
    Complexity time O(nt), space O(nt), where n stands for number of videos and t stands for tags in the videos.
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


# Funciones para agregar informacion al catalogo
def add_video(videos, line):
    """
    Auxiliary function to create_videos which adds to videos an arraylist with most parameters and a linked list
    with the information of the tags of the videos. Complexity time O(t), space O(t) where t stands for tags in the
    videos.
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
def element_videos(videos, i, j):
    """
    Complexity time O(1), space O(1).
    Args:
        videos:
        i: index of the video
        j: index of the parameter
    Returns:
    Parameter of the video.
    """
    if j < 16:
        return videos['elements'][i][0]['elements'][j]
    else:
        return 'error'


def parameter_minimum(videos, index_order, index_parameter, parameter):
    """
    Works correctly only if index_parameter is equal to the first index parameter with which index_order was made.
    Args:
        videos: arraylist of videos
        index_order: custom index_order of videos
        index_parameter: index of parameter to be evaluated
        parameter: search parameter
    Returns:
    Index of the minimum element (in the index_order) which contains a certain parameter.
    """
    f = -1
    c = len(index_order) - 1
    m = (c + f) // 2 + (c + f) % 2
    while f != c:
        if element_videos(videos, index_order[m], index_parameter) >= parameter:
            c = m - 1
        else:
            f = m
        m = (c + f) // 2 + (c + f) % 2
    return f + 1


def parameter_maximum(videos, index_order, index_parameter, parameter):
    """
    Works correctly only if index_parameter is equal to the first index parameter with which index_order was made.
    Args:
        videos: arraylist of videos
        index_order: custom index_order of videos
        index_parameter: index of parameter to be evaluated
        parameter: search parameter
    Returns:
    Index of the maximum element (in the index_order) which contains a certain parameter.
    """
    f = 0
    c = len(index_order)
    m = (c + f) // 2
    while f != c:
        if element_videos(videos, index_order[m], index_parameter) <= parameter:
            f= m + 1
        else:
            c = m
        m = (c + f) // 2
    return c - 1


def range_by_parameter(videos, index_order, index_parameter, parameter):
    """
    Works correctly only if index_parameter is equal to the first index parameter with which index_order was made.
    Args:
        videos: arraylist of videos
        index_order: custom index_order of videos
        index_parameter: index of parameter to be evaluated
        parameter: parameter
    Returns:
    Index of the minimum element (in the index_order) which contains a certain parameter.
    """
    f = parameter_minimum(videos, index_order, index_parameter, parameter)
    c = parameter_maximum(videos, index_order, index_parameter, parameter)
    return f, c


def has_tag(videos, i, tag):
    return lt.isPresent(videos['elements'][i][1], tag)


# Funciones utilizadas para comparar elementos dentro de una lista
def base_sort_function(videos, i, parameter_indexes):
    """
    Auxiliary function to createIndexOrder. Complexity time O(p), space O(p), where p stands for number of parameters,
    (p <= 16).
    Args:
        videos: arraylist of videos
        i: index of the video
        parameter_indexes: tuple of indexes of parameters
    Returns:
    A tuple with the values that correspond to the parameter_indexes in the index i of videos.
    """
    return tuple([element_videos(videos, i, x) for x in parameter_indexes if x < 16])


# Funciones de ordenamiento
def create_index_order(videos, order_indexes):
    """
    'Tags' parameter not supported. Complexity time O(nlog(n)p), space O(np), where n stands for number of videos and
    p stands for number of parameters (p <= 16).
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

#usage example
"""
import time
print("Loading vidios", time.asctime(time.gmtime()))
vidios = create_videos(cf.data_dir+'videos-all.csv')
print("Creating order", time.asctime(time.gmtime()))
order = create_index_order(vidios, [15,4,6])
print("Finding range", time.asctime(time.gmtime()))
print(range_by_parameter(vidios, order, 15, 'canada'))
print("Finish", time.asctime(time.gmtime()))
"""