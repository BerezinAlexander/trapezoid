# trapezoib
#
# (описание программы)

#import layer

import sys
import logging

logging.basicConfig(
    format = '[%(asctime)s][%(levelname)s] %(message)s',
    stream = sys.stdout,
    level  = logging.INFO
)

print("$> Start")

logger = logging.getLogger("trapezoid")
logger.info("Print start programm")

# класс фигура
class figure:
    """description of class"""

    def __init__(self, x):
        self.num = x
        self.coord = []

# класс слой
class layer:
    """description of class"""

    def __init__(self, num):
        self.num = num
        self.countFig = 0
        self.fig = []

    def addFig(self):
        self.fig = figure(self.countFig)
        self.countFig += 1

lr = layer(0)
lr.addFig()


f = open('l6')
text = f.read()
f.close()
print(" ")


#print("$> Print text")
#print(text)

##print(text.line[1])
#print(type(text))

# ��������� ������ �� ������
li = []
pos = 0
ind = text.find('\n')
while ind != -1:
    li.append(text[pos:ind])
    pos = ind + 1
    ind = text.find('\n', pos)

# ����� �����
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