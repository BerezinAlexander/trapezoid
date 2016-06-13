class shape(object):
    """description of class"""

    def __init__(self, coord=0, contour=[]):
        self.origin = coord
        self.contur = contour

class layer(object):
    """description of class"""
    
    def __init__(self, num):
        self.num = num

    def addShape(self, coord, contour):
        self.shapes = shape(coord, contour)

# функция разбора строки с фигурой
def pasreStr(str):
    # получение номера слоя
    begin = str.find("Layer: M") + len("Layer: M")
    end   = str.find(' ', begin)    
    layerNum = int(str[begin: end])
    # получение координат origin
    begin = end + 11
    end =  str.find(' ', begin)
    coordX = int(str[begin: end])    
    begin = end + 1
    end =  str.find(' ', begin)
    coordY = int(str[begin: end])
    # получение координат контура
    contour = []

def shapeParser(strings):
    for str in strings:
        pasreStr(str)  