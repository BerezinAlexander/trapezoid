# trapezoib
#
# (описание программы)

#import layer

import sys
import logging
from layer import *
from trapeze import *

# логгирование
logging.basicConfig(
    format = '[%(asctime)s][%(levelname)s] %(message)s',
    stream = sys.stdout,
    level  = logging.INFO
)
logger = logging.getLogger("trapezoid")
logger.info("Start programm")

# считывание из файла
logger.info("File reading")
f = open('l6')
text = f.read()
f.close()

# разбор файла
logger.info("File parsing")
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

# разбор файла
layers = {} # создаем пустой словарь
shapeParser(layers, shapesStr) # разбираем файл

# вывод фигур
logger.info("Print shapes")
print(" ")
for ln in shapesStr:
    print(ln)

# нарезка на трапеции
trapezes = []
trapezes = cuttingOnTheTrapeze(layers)

# заголовок файла
buffer = "---- Edges:\n"
for tra in trapezes:
    buffer += tra.getBuf()

logger.info("Write edges in file '12 edge'")
# запись в файл
f = open('12 edge', 'w')
f.write(buffer)
f.close()

# вывод фигур
logger.info("Print cutting shapes")
print(" ")
for key in layers:
    layers[key].printAll()

dicColor = {}
dicColor[1] = "#00aaff"
dicColor[2] = "#ffff00"
dicColor[3] = "#ff557f"
dicColor[4] = "#00aaff"
dicColor[5] = "#ffff00"
dicColor[6] = "#ff557f"

# заголовок файла
buffer = "---- Layers:\n"
for key in layers:
    buffer += "M" + str(key) + " " + dicColor[key] + "\n"

buffer += "\n---- Shapes:\n"
for key in layers:  
    buffer += layers[key].getBuffer()

logger.info("Write shapes in file '12 new'")
# запись в файл
f = open('12 new', 'w')
f.write(buffer)
f.close()





## разбор файла построчно
#li = []
#pos = 0
#ind = text.find('\n')
#while ind != -1:
#    li.append(text[pos:ind])
#    pos = ind + 1
#    ind = text.find('\n', pos)

## построчный вывод файла
#for ln in li:
#    print(ln)

#strline = ""
#li = []
#for ch in text:
#    if ch == '\n': break
#    strline += ch
#li.append(strline)    
#print(strline)

logger.info("Stop programm")