# """
#
# 作者：Szy
# 日期：2022年03月08日
# """
import copy
import types

import PyQt5.QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from typing import List
import math
#
# #Cell类对象表示一个单元格，他保存单元格中的数据、文字等信息，并有PaintEvent方法能画出自己
class Cell(QWidget):
    # expandable = pyqtSignal(int, int)
    # clicked = pyqtSignal()
    # ohno = pyqtSignal()

    def __init__(self, row=0, col=0, *args, **kwargs):
        super(Cell, self).__init__(*args, **kwargs)
        #size=80
        #设置widget大小
        #self.setFixedSize(QSize(size, size))
        #cell在显示中的坐标
        self.row = row
        self.col = col
        #颜色(边框和内部颜色)、文字属性，其他属性可以继承该类定制
        self.__innerColor=Qt.gray
        self.__outerColor=Qt.gray
        self.__font=QFont("宋体", 15, QFont.Bold, True)
        self.__text=""
        self.__textColor=Qt.black
        self.__r=None
    def setCellFont(self, font:QFont)->None:
        '''设置Cell文字字体'''
        self.__font=font
    def setCellText(self, text:str)->None:
        '''设置Cell文字'''
        self.__text = text
    def getCellText(self)->str:
        '''获取Cell文字'''
        return self.__text
    def setCellColor(self, color) -> None:
        '''设置Cell颜色，可选值:Qt.XX
            XX:blue,red,yellow....其他见
            https://www.w3.org/TR/SVG11/types.html#ColorKeywords
        '''
        self.__innerColor=color
    def setTextColor(self, color) -> None:
        '''设置Cell颜色，可选值:Qt.XX
            XX:blue,red,yellow....其他见
            https://www.w3.org/TR/SVG11/types.html#ColorKeywords
        '''
        self.__textColor=color
    def paintEvent(self, event) -> None:
        p=QPainter(self)
        #抗锯齿
        p.setRenderHint(QPainter.Antialiasing)
        #图形区域
        self.__r=event.rect()
        '''
        对于其中的painter.drawText()方法，需要说明其中的第一个参数：
        painter.drawText(event.rect(), Qt.AlignCenter, self.text)
        此处的event.rect()指的是主事件的矩形区域，也就是整个主窗口，除此之外，
        可以通过指定x和y来指定绘图区域
        '''
        #获取背景颜色
        #inner=self.palette().color(QPalette.Background)
        #填充矩形
        p.fillRect(self.__r, QBrush(self.__innerColor))
        pen = QPen(self.__outerColor)
        pen.setWidth(1)
        p.setPen(pen)
        p.drawRect(self.__r)
        #写字
        p.setPen(self.__textColor)
        p.setFont(self.__font)
        p.drawText(self.__r, Qt.AlignHCenter | Qt.AlignVCenter, str(self.__text))

#field类，管理widget子类二维数组
class CellField:
    #*args作为变量初始化参数，可以不带
    def __init__(self, cls, row:int=1, col:int=1, *args):
        #生成一个row行col列，值为None的二维数组
        print(args)
        self.__field=[[cls(*args) for i in range(col)] for i in range(row)]
        #self.__field = [[Cell(), Cell()],[Cell(), Cell()]]
        self.field=self.__field

    def putField(self, field):
        """设置__field"""
        self.__field=field
    def getField(self)->List[List[Cell]]:
        """获取__field"""
        return self.__field
    def getItem(self,i, j)->Cell:
        """获取i行j列的元素"""
        #print(type(self.__field[i][j]))
        #return self.__field[i][j]
        #a=self.__field[0][0]
        return self.__field[i][j]
        #return self.__field[0][0]
        #return self.field[i][j]
    def getSize(self)->List[int]:
        '''返回field的[行，列]'''
        if not self.__field:
            return [0, 0]
        else:
            return [len(self.__field), len(self.__field[0])]

    def getDistance(self, p1:List[int], p2:List[int])->float:
        '''计算i1,2行j1,2列两点间距离'''
        dx=abs(p1[1]-p2[1])
        dy=abs(p1[0]-p2[0])
        return math.sqrt(dx*dx+dy*dy)
    def getNeighbour(self, row:int, col:int)->List[Cell]:
        "返回p[row][col]周围<=8个邻居"
        if not self.__field:
            return None
        result=[]
        startCol=col-1
        startRow=row-1
        for i in range(startRow, startRow+3):
            for j in range(startCol, startCol+3):
                #跳过自己和越界访问
                if (i==row and j==col) or i>=len(self.__field) or j>=len(self.__field[0]) or i<0 or j<0:
                    continue
                else:
                    result.append(self.__field[i][j])
        return result

class CellView:
    def setView(wgt:QWidget, field:CellField)->None:
        '''在指定widget中显示field'''
        row, col=field.getSize()
        vb = QVBoxLayout()
        grid = QGridLayout()
        grid.setSpacing(5)
        vb.addLayout(grid)
        wgt.setLayout(vb)
        for i in range(0, row):
            for j in range(0, col):
                grid.addWidget(field.getItem(j, i), j, i)
                a = grid.itemAtPosition(j, i).widget()
                sizePolicy = QSizePolicy(QSizePolicy.Expanding,
                                                 QSizePolicy.Expanding)
                a.setSizePolicy(sizePolicy)
# if __name__ == '__main__':
#     app = QApplication([])
#     window = MainWindow()
#     app.exec_()
