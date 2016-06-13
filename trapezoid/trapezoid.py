# trapezoib
#
# (описание программы)

#import layer

import sys
import logging
from layer import *

logging.basicConfig(
    format = '[%(asctime)s][%(levelname)s] %(message)s',
    stream = sys.stdout,
    level  = logging.INFO
)

print("$> Start")

logger = logging.getLogger("trapezoid")
logger.info("Print start programm")

## класс фигура
#class figure:
#    """description of class"""

#    def __init__(self, x):
#        self.num = x
#        self.coord = []

## класс слой
#class layer:
#    """description of class"""

#    def __init__(self, num):
#        self.num = num
#        self.countFig = 0
#        self.fig = []

#    def addFig(self):
#        self.fig = figure(self.countFig)
#        self.countFig += 1

layers = {}

def addLayer(num):
    if layers.get(num) == None:
        layers[num] = layer(num)
    return layers[num];

#lr = addLayer(0)
#lr.addShape((31, 23), [(1, 2), (3, 4), (5, 6)])



f = open('l6')
text = f.read()
f.close()
print(" ")


#print("$> Print text")
#print(text)

##print(text.line[1])
#print(type(text))

# разбор файла
shapesStr = [] # строки фигур
end = text.find("---- Shapes:") # находим строку "---- Shapes:"
# заполняем лист фигур
while end != -1:
    begin = end
    # находим начало и конец след строки
    begin = text.find('\n', begin) + 1
    end   = text.find('\n', begin)
    # добавляем строку в список фигур
    shapesStr.append(text[begin: end])      

shapeParser(shapesStr)


# вывод фигур
print(" ")
for ln in shapesStr:
    print(ln)
print(" ")

# разбор файла построчно
li = []
pos = 0
ind = text.find('\n')
while ind != -1:
    li.append(text[pos:ind])
    pos = ind + 1
    ind = text.find('\n', pos)

# построчный вывод файла
for ln in li:
    print(ln)

#strline = ""
#li = []
#for ch in text:
#    if ch == '\n': break
#    strline += ch
#li.append(strline)    
#print(strline)

print(" ")
print("$> Exit")