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


from typing import runtime_checkable
import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import selectionsort as sls
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import shellsort as shl
from DISClib.Algorithms.Sorting import mergesort as mgs
from DISClib.Algorithms.Sorting import quicksort as qks

assert cf


def newCatalog(listType):
    """
    The catalog starts where two empty lists are created, one for the videos and the other for the categories.
    Return the catalog
    """
    catalog = {'videos': None,
               'categories': None,}

    catalog['videos'] = lt.newList(listType, cmpfunction=cmpVideosByViews)
    catalog['categories'] = lt.newList(listType, cmpfunction=None)
    
    return catalog


# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    'The video is added to the video list'
    lt.addLast(catalog['videos'], video)

def addCategory(catalog, category):
    'The category is added to the category list'
    lt.addLast(catalog['categories'], category)

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpVideosByViews(video1, video2):
    'Return True if vid1 < vid2'
    return (float(video1['views']) < float(video2['views']))

def cmpVideosById(video1, video2):
    'Return True if vid1 < vid2'
    return video1['video_id'] <= video2['video_id']

def cmpVideosByTrendingDays(video1, video2):
    'Return True if vid1 > vid2'
    return (float(video1['trending_days']) > float(video2['trending_days']))

def cmpVideosByLikes(video1, video2):
    'Return True if vid1 > vid2'
    return (float(video1['likes']) > float(video2['likes']))


# Funciones de ordenamiento

def selectSortMethod(method):
    if method == 'sls':
        sortType = sls
    elif method == 'ins':
        sortType = ins
    elif method ==  'shl':
        sortType = shl
    elif method == 'mgs':
        sortType = mgs
    elif method == 'qks':
        sortType = qks
    return sortType

def sortVideos(catalog, size, method):
    sortmet = selectSortMethod(method)
    sub_list = lt.subList(catalog['videos'], 0, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    sorted_list = sortmet.sort(sub_list, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list

def sortVideosForCountry(lst, size):
    sortmet = selectSortMethod('mgs')
    sub_list = lt.subList(lst, 0, size)
    sub_list = sub_list.copy()
    sorted_list = sortmet.sort(sub_list, cmpVideosById)
    return sorted_list

def sortVideosbyTrendingDays(lst, size):
    sortmet = selectSortMethod('mgs')
    sub_list = lt.subList(lst, 0, size)
    sub_list = sub_list.copy()
    sorted_list = sortmet.sort(sub_list, cmpVideosByTrendingDays)
    return sorted_list

def sortVideosbyLikes(lst, size):
    sortmet = selectSortMethod('mgs')
    sub_list = lt.subList(lst, 0, size)
    sub_list = sub_list.copy()
    sorted_list = sortmet.sort(sub_list, cmpVideosByLikes)
    return sorted_list

def videosCountry(catalog, country):
    videos = lt.newList('ARRAY_LIST')
    i = 0
    while i < lt.size(catalog['videos']) + 1:
        video = lt.getElement(catalog['videos'], i)
        if video['country'] == country:
            lt.addLast(videos,video)
            i += 1
        else:
            i += 1
    videos = sortVideosForCountry(videos, lt.size(videos))
    return videos

def videosCountryTrendingResumed(lst):
    videosResumed = lt.newList('ARRAY_LIST')
    first_video = lt.getElement(lst,0)
    first_video['trending_days'] = 1
    first_video['likes'] = int(first_video['likes'])
    lt.addLast(videosResumed,first_video)

    lst_index = 1
    videosResumed_index = 0
    while lst_index < lt.size(lst) + 1:
        if lt.getElement(lst,lst_index)['video_id'] == lt.getElement(videosResumed,videosResumed_index)['video_id'] or lt.getElement(lst,lst_index)['title'] == lt.getElement(videosResumed,videosResumed_index)['title']:
            lt.getElement(videosResumed,videosResumed_index)['trending_days'] += 1
            lt.getElement(videosResumed,videosResumed_index)['likes'] = int(lt.getElement(videosResumed,videosResumed_index)['likes']) + abs(int(lt.getElement(lst,lst_index)['likes']) - int(lt.getElement(videosResumed,videosResumed_index)['likes']))
            lst_index += 1
        else:
            lt.getElement(lst,lst_index)['trending_days'] = 1
            lt.getElement(lst,lst_index)['likes'] = int(lt.getElement(lst,lst_index)['likes'])
            lt.addLast(videosResumed,lt.getElement(lst,lst_index))
            lst_index += 1
            videosResumed_index += 1

    trendingvideossorted = sortVideosbyTrendingDays(videosResumed, lt.size(videosResumed)+1)
    return trendingvideossorted

def videosLikesCountryTags(catalog, country,tag):
    videos = lt.newList('ARRAY_LIST')
    i = 0
    while i < lt.size(catalog['videos']) + 1:
        video = lt.getElement(catalog['videos'], i)
        if video['country'] == country:
            lt.addLast(videos,video)
            i += 1
        else:
            i += 1
    videostag = lt.newList('ARRAY_LIST')
    i = 0
    while i < lt.size(videos) + 1:
        videot = lt.getElement(videos, i)
        if tag in videot['tags']:
            lt.addLast(videostag,videot)
            i += 1
        else:
            i += 1
    resumed = videosCountryTrendingResumed(videostag)
    sortedByLikes = sortVideosbyLikes(resumed,lt.size(resumed))
    return sortedByLikes