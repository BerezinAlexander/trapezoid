# класс фигуры
class shape(object):
    """description of class"""

    def __init__(self, coord=[], contour=[]):
        self.origin  = coord
        self.contour = contour

# класс слоя
class layer(object):
    """description of class"""

    def __init__(self, num=0, shapes=[]):
        self.num = num
        self.shapes = shapes

    def addShape(self, coord, contour):
        self.shapes.append(shape(coord, contour))

# создание слоя или добавление фигуры в существующий
def addLayer(layers, num):
    if layers.get(num) == None:
        layers[num] = layer(num, [])
    return layers[num];

# разбор строк
def shapeParser(layers, strings):
    for str in strings:
        pasreStr(layers, str)  

# функция разбора строки с фигурой
def pasreStr(layers, str):
    # получение номера слоя
    begin = str.find("Layer: M")
    if(begin != -1):
        # получение номера слоя
        begin += len("Layer: M")
        end   = str.find(' ', begin)    
        layerNum = int(str[begin: end])
        lr = addLayer(layers, layerNum)
        
        # получение координат origin
        begin = end + 11
        end =  str.find(' ', begin)
        coordX = int(str[begin: end])    
        
        begin = end + 1
        end =  str.find(' ', begin)
        coordY = int(str[begin: end])

        # получение координат контура
        contour = []
        begin = str.find('(', end)
        end   = str.rfind(')', begin)
        parseCoords(contour, str[begin : end])

        # добавление данных в слой
        lr.addShape([coordX, coordY], contour)

#разбор строки координат
def parseCoords(contour, str):
    begin = str.find('(') # находим скобку начала контура
    if(begin != -1):
        begin += 1 # пропускаем скобку
        # разбираем все координаты
        begin = str.find('(', begin)
        while begin != -1:       
            end = str.find(')', begin)
            contour.append(parseCrd(str[begin : end]))
            begin = str.find('(', end)    
    
# разбор одной координаты
def parseCrd(str):
    coordX = 0;
    coordY = 0;
    begin = str.find('(')
    if(begin != -1):
        begin += 2 # пропускаем скобку и пробел
        end = str.find(' ', begin); 
        coordX = int(str[begin: end]) 
        begin = end + 1
        end =  str.find(' ', begin)
        coordY = int(str[begin: end])
    return [coordX, coordY]