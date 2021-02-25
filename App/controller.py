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


def initCatalog(list_type):
    catalog = model.newCatalog(list_type)
    return catalog

def loadData(catalog):
    loadVideos(catalog)
#    loadTags(catalog)


def loadVideos(catalog):
    videosfile = cf.data_dir + 'Videos/videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)

def sortVideos(catalog,list_num, list_alg):
    lst = model.newSList(catalog["videos"],0,int(list_num)-1)
    sList = model.sort(lst,list_alg)
    
    return sList

#def loadTags(catalog):
#   tagsfile = cf.data_dir + 'Videos/category-id.csv'
#    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
#    for tag in input_file:
#        model.addTag(catalog, tag)



# Inicialización del Catálogo de libros

# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
