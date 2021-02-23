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
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """
    inicializa el catalogo de video y su informacion
    """
    catalog = {'videos': None,
               'categorias': None,
               'pais':None,
               'tag':None}
    
    catalog['videos'] = lt.newList()
    catalog['categorias'] = lt.newList()
    catalog['pais'] = lt.newList()
    catalog['tag'] =lt.newList()

    
    return catalog

# Funciones para agregar informacion al catalogo

def addvideo(catalog, video):
    # se adiciona el video a la lista de videos 
    # video es un dicc
    lt.addLast(catalog['videos'], video)
    #sacamos las categorias de el dic videos
    categories = video['category_id'].split(',')
    # cada categoria se crea como una lista de 
    # y se. 
    for category in categories:
        addCategory(catalog, category.strip(), video)
        

def addCategory(catalog, category_name, video):
    catcategoria = catalog['categorias']
    poscategoria = lt.isPresent(catcategoria, category_name)
    if poscategoria >0:
        categoria = lt.getElement(catcategoria, poscategoria)
    else:
        categoria = newcategoria(category_name)
        lt.addLast(catcategoria, categoria)
    lt.addLast(categoria['videos'], video)
        
        
        
def newcategoria(category_name):
    categoria = {'categoria': "", "videos": None}
    categoria['categoria'] = category_name
    categoria['videos'] = lt.newList('ARRAY_LIST')
    return categoria
        
    
    
    
    
    
    
    
    
# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento