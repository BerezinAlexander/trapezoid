from layer import *
from math import sqrt

# класс отрезок (грань)
class edge(object):
    isOpen   = False    # Открывающая или закрывающая
    first    = []   # Первая координата
    second   = []   # Вторая координата
    slope    = 0.0      # Тангенс угла наклона прямой
    
    def __init__(self, isop, fir, sec, slo):
        isOpen   = isop
        first    = fir
        second   = sec
        slope    = slo

# класс трапеция
class trapeze(object):
    layerNum = 0    # Номер слоя 
    edges = []      # отрезки
    
    def __init__(self):
        edges = []

    def addEdge(edge):
        edges.append(edge)

# нарезка слоев на трапеции
def cuttingOnTheTrapeze(layers):
    for key in layers:
        for she in layers[key].shapes:
            cuttingShape(she)

# нарезка фигуры на трапеции
def cuttingShape(she):
    # shape содержит координату оригинала и контур
    
    # найдем оси разрезов, т е все координаты X точек
    axis = []
    for crd in she.contour:
        axis.append(crd[0])
    axis = list(set(axis)) # удаляем дубликаты
    axis.sort()
    
    # проходим по осям разрезов
    i = 0
    for ax in axis:
        edges = [] # создаем список отрезков
        # проходим по контуру
        coords = [] # координаты отрезков
        for crd in she.contour:
            # если ось совпала с координатой X отрезка, то
            result = []
            if(ax == crd[0]):
                # сохраняем эту координату
                xy = [] # координаты отрезка
                xy.append([ax, crd[1]])
                # ищем индекс след координаты в контуре
                index = she.contour.index(xy[0]) + 1
                if index > len(she.contour) - 1 :
                    index = 0
                # сохраняем координату
                xy.append(she.contour[index])
                # расчет точки пересечения c осью
                if i < len(axis) - 1:
                    res = calcPoint([xy[0], xy[1]],[[axis[i+1], -200], [axis[i+1], 200]]) 
                    if res[0] == 1:
                        # точка пересечения есть
                        result = res[1]    
                adf = 0
                
            
        i += 1          
        


    asd = 0

# расчет точки пересечения
def calcPoint(line1, line2):
    EPS = 1e-6
    # расчет коэффициентов прямой по координатам двух точек
    def equationLine(crd1, crd2):
        #если точки совпадают, то по ним нельзя построить прямую
        if (crd1[0] == crd2[0] & crd1[1] == crd2[1]):
            return

        # получение коэффициентов прямой по координатам двух точек
        a = crd1[1] - crd2[1]
        b = crd2[0] - crd1[0]
        c = -1 * (crd1[1] - crd2[1]) * crd1[0] - (crd2[0] - crd1[0]) * crd1[1]
        # нормировка прямой
        z = sqrt(a * a + b * b)
        a /= z
        b /= z
        c /= z
        if ((a < -EPS) | ((abs(a) < EPS) & (b < -EPS))):
            a *= -1
            b *= -1
            c *= -1
        return [a, b, c]

    # расчет определителя
    def det(x11, x12, x21, x22):
        return x11 * x22 - x12 * x21
    
    coef = []
    coef.append(equationLine(line1[0], line1[1]))
    coef.append(equationLine(line2[0], line2[1]))
 
    denom = det(coef[0][0], coef[0][1], coef[1][0], coef[1][1])

    if (abs(denom) < EPS):
        # прямые совпадают и имеет бесконечно точек пересечения
        if (coef[0][2] == coef[1][2]):
            return [2]
        # прямые параллельны и не пересекаются
        return [0]
    # прямые пересекаются в одной точке, вычисляем координаты
    res = []
    res.append(det(-coef[0][2], coef[0][1], -coef[1][2], coef[1][1]) / denom)
    res.append(det(coef[0][0], -coef[0][2], coef[1][0], -coef[1][2]) / denom)
    return [1, res]