# Примитивы

from math import sqrt

class Point(object):
    x = 0
    y = 0

    def __init__(self, crd=[0, 0]):
        self.x = crd[0]
        self.y = crd[1]

    def crd(self, crd):
        self.x = crd[0]
        self.y = crd[1]

    def getList(self):
        return [self.x, self.y]

class Line(object):
    
    xy0 = Point()    
    xy1 = Point()
    coef = []

    def __init__(self, crd=[Point(), Point([1,1])]):
        self.xy0 = crd[0]
        self.xy1 = crd[1]

    # расчет коэффициентов прямой по координатам двух точек
    def equationLine(self):
        EPS = 1e-6
        #если точки совпадают, то по ним нельзя построить прямую
        if (self.xy0.x == self.xy1.x & self.xy0.y == self.xy1.y):
            return

        # получение коэффициентов прямой по координатам двух точек
        a = self.xy0.y - self.xy1.y
        b = self.xy1.x - self.xy0.x
        c = -1 * (self.xy0.y - self.xy1.y) * self.xy0.x - (self.xy1.x - self.xy0.x) * self.xy0.y
        # нормировка прямой
        z = sqrt(a * a + b * b)
        a /= z
        b /= z
        c /= z
        if ((a < -EPS) | ((abs(a) < EPS) & (b < -EPS))):
            a *= -1
            b *= -1
            c *= -1
        self.coef = [a, b, c]

    # расчет определителя
    def det(x11, x12, x21, x22):
        return x11 * x22 - x12 * x21

    # нахождение общей точки текощей линии с линией line
    def commonPoint(self, line):
        # [0]       - прямые параллельны и не пересекаются
        # [1, res]  - прямые пересекаются в одной точке, res - координаты пересечения
        # [2]       - прямые совпадают и имеет бесконечно точек пересечения
        EPS = 1e-6
        denom = Line.det(self.coef[0], self.coef[1], line.coef[0], line.coef[1])

        if (abs(denom) < EPS):
            # прямые совпадают и имеет бесконечно точек пересечения
            if (self.coef[2] == line.coef[2]):
                return [2]
            # прямые параллельны и не пересекаются
            return [0]
        # прямые пересекаются в одной точке, вычисляем координаты
        res = Point()
        res.x = int(Line.det(-self.coef[2],  self.coef[1], -line.coef[2],  line.coef[1]) / denom)
        res.y = int(Line.det( self.coef[0], -self.coef[2],  line.coef[0], -line.coef[2]) / denom)
        return [1, res]

    