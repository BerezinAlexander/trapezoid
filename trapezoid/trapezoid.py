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
cuttingOnTheTrapeze(layers)









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