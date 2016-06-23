from layer import *
from math import sqrt
from primitives import *

# класс отрезок (грань)
class edge(object):
    isOpen   = False    # Открывающая или закрывающая
    first    = []   # Первая координата
    second   = []   # Вторая координата
    slope    = 0.0      # Тангенс угла наклона прямой
    
    def __init__(self, isop, fir, sec, slo):
        self.isOpen   = isop
        self.first    = fir
        self.second   = sec
        self.slope    = slo

# класс трапеция
class trapeze(object):
    layerNum = 0    # Номер слоя 
    edges = []      # отрезки
    
    def __init__(self, num=0):
        self.layerNum = num
        self.edges = []

    def addEdge(self, edge):
        self.edges.append(edge)

    def getBuf(self):
        buf = ""
        
        for ed in self.edges:
            buf += "Edge: M" + str(self.layerNum) + " "
            buf += str(ed.isOpen) + " " + str(ed.first) + " " + str(ed.second) + " " + str(ed.slope) + "\n"
        return buf

# нарезка слоев на трапеции
def cuttingOnTheTrapeze(layers):
    trapezes = []
    for key in layers:
        for she in layers[key].shapes:
            tra = trapeze(key)
            edges = [] # создаем список отрезков
            cuttingShape(she, edges)
            tra.edges = edges
            trapezes.append(tra)
    return trapezes

# нарезка фигуры на трапеции
def cuttingShape(she, edges):
    # shape содержит координату оригинала и контур
    
    # найдем оси разрезов, т е все координаты X точек
    axis = []
    for crd in she.contour:
        axis.append(crd[0])
    axis = list(set(axis)) # удаляем дубликаты
    axis.sort()    
    
    i = 0
    # проходим по осям разрезов
    for ax in axis:
        isOpen = False        

        j = 0
        # проходим по контуру
        for crd in she.contour: 
            # если ось совпала с координатой X отрезка, то
            if(ax == crd[0]):              
                if(j >= len(she.contour) - 1): 
                    j = -1
                if(she.contour[j+1][0] > ax):
                    tan = tang(crd, she.contour[j+1])
                    cuttingEdge(she.contour, crd, axis, ax, i, True)
                    edges.append(edge(isOpen, crd, she.contour[j+1], tan))
                    isOpen = not isOpen
                if(j == 0):
                    j = len(she.contour)
                    if(she.contour[j-1][0] > ax):
                        tan = tang(crd, she.contour[j-1])
                        cuttingEdge(she.contour, crd, axis, ax, i, False)
                        edges.append(edge(isOpen, crd, she.contour[j-1], tan))
                        isOpen = not isOpen
                    j = 0
            j += 1               
        i += 1          
        
    # после нарезки на трапеции создаем классы трапеций
    

    asd = 0

def tang(crd1, crd2):
    return (crd2[1] - crd1[1]) / (crd2[0] - crd1[0])

# разбиение отрезка и вставка в контур
def cuttingEdge(contour, crd, axis, ax, i, isRight):
    result = Point() # точка пересечения отрезка с осью
    line = Line()
    #xy = [] # координаты отрезка
                
    # сохраняем эту координату
    line.xy0.crd([ax, crd[1]])
    #xy.append([ax, crd[1]])
                
    # ищем индекс след координаты в контуре
    index = contour.index(line.xy0.getList())
    if isRight:
        if index == len(contour) - 1 :
            index = 0
        else:
            index += 1
    else:
        if index == 0:
            index = len(contour) - 1
        else:
            index -= 1
    # сохраняем координату
    line.xy1.crd(contour[index])
    line.equationLine()
    #xy.append(she.contour[index])

    if not isRight: 
        if index == len(contour) - 1: 
            index = 0 
        else: 
            index += 1

    # расчет точки пересечения c осью  
    if i < len(axis) - 1:
        if line.xy1.x > axis[i+1]:
            axle = Line([Point([axis[i+1], -300]), Point([axis[i+1], 200])])
            axle.equationLine();
            res = line.commonPoint(axle)
            if res[0] == 1:
                # точка пересечения есть
                result = res[1]    
                
                contour.insert(index, result.getList())


## расчет точки пересечения
#def calcPoint(line1, line2):
#    EPS = 1e-6
#    # расчет коэффициентов прямой по координатам двух точек
#    def equationLine(crd1, crd2):
#        #если точки совпадают, то по ним нельзя построить прямую
#        if (crd1[0] == crd2[0] & crd1[1] == crd2[1]):
#            return

#        # получение коэффициентов прямой по координатам двух точек
#        a = crd1[1] - crd2[1]
#        b = crd2[0] - crd1[0]
#        c = -1 * (crd1[1] - crd2[1]) * crd1[0] - (crd2[0] - crd1[0]) * crd1[1]
#        # нормировка прямой
#        z = sqrt(a * a + b * b)
#        a /= z
#        b /= z
#        c /= z
#        if ((a < -EPS) | ((abs(a) < EPS) & (b < -EPS))):
#            a *= -1
#            b *= -1
#            c *= -1
#        return [a, b, c]

#    # расчет определителя
#    def det(x11, x12, x21, x22):
#        return x11 * x22 - x12 * x21
    
#    coef = []
#    coef.append(equationLine(line1[0], line1[1]))
#    coef.append(equationLine(line2[0], line2[1]))
 
#    denom = det(coef[0][0], coef[0][1], coef[1][0], coef[1][1])

#    if (abs(denom) < EPS):
#        # прямые совпадают и имеет бесконечно точек пересечения
#        if (coef[0][2] == coef[1][2]):
#            return [2]
#        # прямые параллельны и не пересекаются
#        return [0]
#    # прямые пересекаются в одной точке, вычисляем координаты
#    res = []
#    res.append(det(-coef[0][2], coef[0][1], -coef[1][2], coef[1][1]) / denom)
#    res.append(det(coef[0][0], -coef[0][2], coef[1][0], -coef[1][2]) / denom)
#    return [1, res]