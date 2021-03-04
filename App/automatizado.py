# TODO BORRAR

"""
def mainfunction():
    # principal original xd
    catalog = initCatalog(0)
    loadData(catalog)
    exceldoc = openpyxl.load_workbook("D:/Uniandes/Clases/Semestre 2 2021 I/EDA/Lab/Reto1-G10/datos.xlsx")
    sheet = exceldoc['Datos Lab4-5']
    
    exceeded = False
    i = 2
    size = 1000
    while not exceeded and size <= 375492 and i < 12:
        print("quick 0")
        print(size)
        counter = 0
        resultlist = []
        while counter < 3 and not exceeded:
            cellquick = "E" + str(i)
            resultquick = firstReq(catalog, size, 0)
            timequick = resultquick[1]
            if timequick > 900000:
                exceeded = True
                break
            else:
                resultlist.append(timequick)
            counter += 1
        value = sum(resultlist)/3
        sheet[cellquick] = value

        size *= 2
        i += 1

    exceeded = False
    i = 2
    size = 1000
    while not exceeded and size <= 375492 and i < 12:
        print("merge 0")
        print(size)
        counter = 0
        resultlist = []
        while counter < 3 and not exceeded:
            cellmerge = "F" + str(i)
            resultmerge = firstReq(catalog, size, 1)
            timemerge = resultmerge[1]
            if timemerge > 900000:
                exceeded = True
                break
            else:
                resultlist.append(timemerge)
            counter += 1
        value = sum(resultlist)/3
        sheet[cellmerge] = value

        size *= 2
        i += 1

    catalog = initCatalog(1)
    loadData(catalog)
    
    exceeded = False
    i = 15
    size = 1000
    while not exceeded and size <= 375492 and i < 25:
        print("quick 1")
        print(size)
        counter = 0
        resultlist = []
        while counter < 3 and not exceeded:
            cellquick = "E" + str(i)
            resultquick = firstReq(catalog, size, 0)
            timequick = resultquick[1]
            if timequick > 900000:
                exceeded = True
                break
            else:
                resultlist.append(timequick)
            counter += 1
        value = sum(resultlist)/3
        sheet[cellquick] = value

        size *= 2
        i += 1

    exceeded = False
    i = 15
    size = 1000
    while not exceeded and size <= 375492 and i < 25:
        print("merge 1")
        print(size)
        counter = 0
        resultlist = []
        while counter < 3 and not exceeded:
            cellmerge = "F" + str(i)
            resultmerge = firstReq(catalog, size, 1)
            timemerge = resultmerge[1]
            if timemerge > 900000:
                exceeded = True
                break
            else:
                resultlist.append(timemerge)
            counter += 1
        value = sum(resultlist)/3
        sheet[cellmerge] = value

        size *= 2
        i += 1
    
    exceldoc.save("D:/Uniandes/Clases/Semestre 2 2021 I/EDA/Lab/Reto1-G10/datos.xlsx")
"""


def mainfunction():
    # para que haga el ultimo con 375492
    catalog = initCatalog(0)
    loadData(catalog)
    exceldoc = openpyxl.load_workbook("D:/Uniandes/Clases/Semestre 2 2021 I/EDA/Lab/Reto1-G10/datos.xlsx")
    sheet = exceldoc['Datos Lab4-5']
    """
    exceeded = False
    i = 11
    size = 375492
    while not exceeded and size <= 375492 and i < 12:
        print("quick 0")
        print(size)
        counter = 0
        resultlist = []
        while counter < 3 and not exceeded:
            cellquick = "E" + str(i)
            resultquick = firstReq(catalog, size, 0)
            timequick = resultquick[1]
            if timequick > 900000:
                exceeded = True
                break
            else:
                resultlist.append(timequick)
            counter += 1
        value = sum(resultlist)/3
        sheet[cellquick] = value

        size *= 2
        i += 1

    exceeded = False
    i = 11
    size = 375492
    while not exceeded and size <= 375492 and i < 12:
        print("merge 0")
        print(size)
        counter = 0
        resultlist = []
        while counter < 3 and not exceeded:
            cellmerge = "F" + str(i)
            resultmerge = firstReq(catalog, size, 1)
            timemerge = resultmerge[1]
            if timemerge > 900000:
                exceeded = True
                break
            else:
                resultlist.append(timemerge)
            counter += 1
        value = sum(resultlist)/3
        sheet[cellmerge] = value

        size *= 2
        i += 1
    """
    """
    catalog = initCatalog(1)
    loadData(catalog)

    exceeded = False
    i = 15
    size = 1000
    while not exceeded and size <= 375492 and i < 25:
        print("merge 1")
        print(size)
        counter = 0
        resultlist = []
        while counter < 3 and not exceeded:
            cellmerge = "F" + str(i)
            resultmerge = firstReq(catalog, size, 1)
            timemerge = resultmerge[1]
            if timemerge > 900000:
                exceeded = True
                break
            else:
                resultlist.append(timemerge)
            counter += 1
        value = sum(resultlist)/3
        sheet[cellmerge] = value

        size *= 2
        i += 1
    
    exceldoc.save("D:/Uniandes/Clases/Semestre 2 2021 I/EDA/Lab/Reto1-G10/datos.xlsx")


"""
def mainfunction():

    #para los otros algoritmos
    catalog = initCatalog(0)
    loadData(catalog)
    exceldoc = openpyxl.load_workbook("D:/Uniandes/Clases/Semestre 2 2021 I/EDA/Lab/Reto1-G10/datos.xlsx")
    sheet = exceldoc['Datos Lab4-5']
    
    exceeded = False
    i = 2
    size = 1000
    while not exceeded and size <= 375492 and i < 12:
        print("ins 0")
        print(size)
        counter = 0
        resultlist = []
        while counter < 3 and not exceeded:
            cellins = "B" + str(i)
            resultins = firstReq(catalog, size, 1)
            timeins = resultins[1]
            if timeins > 900000:
                exceeded = True
                break
            else:
                resultlist.append(timeins)
            counter += 1
        value = sum(resultlist)/3
        sheet[cellins] = value

        size *= 2
        i += 1

    exceeded = False
    i = 2
    size = 1000
    while not exceeded and size <= 375492 and i < 12:
        print("shell 0")
        print(size)
        counter = 0
        resultlist = []
        while counter < 3 and not exceeded:
            cellshell = "D" + str(i)
            resultshell = firstReq(catalog, size, 2)
            timeshell = resultshell[1]
            if timeshell > 900000:
                exceeded = True
                break
            else:
                resultlist.append(timeshell)
            counter += 1
        value = sum(resultlist)/3
        sheet[cellshell] = value

        size *= 2
        i += 1

    exceeded = False
    i = 2
    size = 1000
    while not exceeded and size <= 375492 and i < 12:
        print("sel 0")
        print(size)
        counter = 0
        resultlist = []
        while counter < 3 and not exceeded:
            cellsel = "C" + str(i)
            resultsel = firstReq(catalog, size, 0)
            timesel = resultsel[1]
            if timesel > 900000:
                exceeded = True
                break
            else:
                resultlist.append(timesel)
            counter += 1
        value = sum(resultlist)/3
        sheet[cellsel] = value

        size *= 2
        i += 1

        catalog = initCatalog(0)

    # TABLA 2

    exceeded = False
    i = 15
    size = 1000
    while not exceeded and size <= 375492 and i < 25:
        print("ins 1")
        print(size)
        counter = 0
        resultlist = []
        while counter < 3 and not exceeded:
            cellins = "B" + str(i)
            resultins = firstReq(catalog, size, 1)
            timeins = resultins[1]
            if timeins > 900000:
                exceeded = True
                break
            else:
                resultlist.append(timeins)
            counter += 1
        value = sum(resultlist)/3
        sheet[cellins] = value

        size *= 2
        i += 1

    exceeded = False
    i = 15
    size = 1000
    while not exceeded and size <= 375492 and i < 25:
        print("shell 0")
        print(size)
        counter = 0
        resultlist = []
        while counter < 3 and not exceeded:
            cellshell = "D" + str(i)
            resultshell = firstReq(catalog, size, 2)
            timeshell = resultshell[1]
            if timeshell > 900000:
                exceeded = True
                break
            else:
                resultlist.append(timeshell)
            counter += 1
        value = sum(resultlist)/3
        sheet[cellshell] = value

        size *= 2
        i += 1

    exceeded = False
    i = 15
    size = 1000
    while not exceeded and size <= 375492 and i < 25:
        print("sel 0")
        print(size)
        counter = 0
        resultlist = []
        while counter < 3 and not exceeded:
            cellsel = "C" + str(i)
            resultsel = firstReq(catalog, size, 0)
            timesel = resultsel[1]
            if timesel > 900000:
                exceeded = True
                break
            else:
                resultlist.append(timesel)
            counter += 1
        value = sum(resultlist)/3
        sheet[cellsel] = value

        size *= 2
        i += 1
    
    exceldoc.save("D:/Uniandes/Clases/Semestre 2 2021 I/EDA/Lab/Reto1-G10/datos.xlsx")


mainfunction()