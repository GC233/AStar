# -*- coding: utf-8 -*-

import sys
from ui_MainWindow import Ui_MainWindow
from math import *
from CellBfs import *
class QmyMainWindow(QMainWindow):
   GREEDMODE=0
   ASTARMODE=1
   def __init__(self, parent=None):

      super().__init__(parent)   #调用父类构造函数，创建窗体
      self.ui=Ui_MainWindow()    #创建UI对象
      self.ui.setupUi(self)      #构造UI界面
      w = self.ui.widget_Grid
      w.setMouseTracking(True)
      self.setMouseTracking(True)
      #self.setCentralWidget(w)

      self.field = CellField(CellBfs, 15, 15)
      CellView.setView(wgt=w, field=self.field)

      self.AstarProportion=0
      #self.solveMaze()
   def saveMap(self):
      row, col = self.field.getSize()
      for i in range(row):
         for j in range(col):
            pass
         pass
   def on_doubleSpinBox_valueChanged(self, v):
      self.AstarProportion=v
   @pyqtSlot()
   def on_pushButton_AStarCal_clicked(self):
      print(1)
      self.solveMaze(QmyMainWindow.ASTARMODE)
   @pyqtSlot()
   def on_pushButton_GreedCal_clicked(self):
      self.solveMaze(QmyMainWindow.GREEDMODE)
   @pyqtSlot()
   def on_pushButton_ResetMap_clicked(self):
      row,col=self.field.getSize()
      for i in range(row):
         for j in range(col):
            item=self.field.getItem(i, j)
            item.setCellAttr(CellBfs.CellAttribute.NOATTR)
            item.setCellText("")
            item.update()
   def solveMaze(self, mode):
      #运行BFS算法
      row,col=self.field.getSize()
      for i in range(row):
         for j in range(col):
            item=self.field.getItem(i, j)
            item.row=i
            item.col = j
            #重置有黄色和字的方格
            if item.getCellText():
               item.setCellText("")
               item.setCellColor(Qt.gray)
      #找出起点和终点
      startPoint =[]
      endPoint =[]
      for i in range(row):
         for j in range(col):
            if self.field.getItem(i, j).cellAttr==CellBfs.CellAttribute.STARTPOINT:
               startPoint=[i, j, 0]
            elif self.field.getItem(i, j).cellAttr==CellBfs.CellAttribute.ENDPOINT:
               endPoint=[i, j]
            if endPoint and startPoint:
               break
      #设置距离value值
      startPoint.append(sqrt((startPoint[0]-endPoint[0])**2+(startPoint[1]-endPoint[1])**2))
      self.field.getItem(startPoint[0],startPoint[1]).setCellAttr(CellBfs.CellAttribute.STARTPOINT)
      self.field.getItem(endPoint[0], endPoint[1]).setCellAttr(CellBfs.CellAttribute.ENDPOINT)
      value = [[None for j in range(col)] for i in range(row)]
      Queue = []  # 队列
      Queue.append(startPoint)
      resultQueue = []  # 存储出队的元素
      while Queue:
         item = Queue.pop(0)  # 队头出队
         resultQueue.append(item.copy())
         value[item[0]][item[1]] = item[2]
         self.field.getItem(item[0], item[1]).setCellText("{:.2f}".format(item[2]))
         #到地方直接结束
         if item[0:2]==endPoint:
            #print("abc")
            break
         # result=maze.getNeighbour(item[0], item[1])
         result = self.field.getNeighbour(item[0], item[1])
         for each in result:
            if each.cellAttr==CellBfs.CellAttribute.OBSTACLE:
               continue
            #判断角点
            di=each.row-item[0]
            dj=each.col-item[1]
            if di and dj:
               n1=self.field.getItem(item[0], each.col).cellAttr
               n2=self.field.getItem(each.row, item[1]).cellAttr
               if n1==CellBfs.CellAttribute.OBSTACLE or n2==CellBfs.CellAttribute.OBSTACLE:
                  continue
            # point=[i, j, distance]
            #更新[row, col, distance, value]
            point = [each.row, each.col, sqrt((each.row - item[0]) ** 2 + (each.col - item[1]) ** 2) + item[2],
                     sqrt((each.row - endPoint[0]) ** 2 + (each.col - endPoint[1]) ** 2)]
            #print(point)
            flg = True
            # 检测如果该坐标既不在结果中，也不在当前队列中，就加入队列
            for each2 in resultQueue:
               if point[0:2] == each2[0:2]:
                  #更新最小值
                  each2[2]=min(point[2],each2[2])
                  flg = False
                  break
            for each3 in Queue:
               if point[0:2] == each3[0:2]:
                  each3[2] = min(point[2], each3[2])
                  flg = False
                  break
            if flg:
               Queue.append(point.copy())
         if mode==QmyMainWindow.GREEDMODE:
            Queue=sorted(Queue, key=lambda i:i[3]).copy()
         elif mode==QmyMainWindow.ASTARMODE:
            Queue = sorted(Queue, key=lambda i:i[3]*(1-self.AstarProportion)+i[2]*self.AstarProportion).copy()
         print(Queue)
      self.ui.widget_Grid.update()
      # for each in value:
      #    print(each)
      #保存地图，测试用
      # f=open("./map.txt", "a")
      # for each in value:
      #    for each1 in each:
      #       if each1:
      #          print(" {:.3} ".format(each1))
      #          f.write(" {:.3} ".format(each1))
      #       else:
      #          f.write(" NON ")
      #    f.write("\n")
      # f.write("\n")
      # f.close()
      #逆推法寻路
      pace = []
      road = endPoint

      # for each in value:
      #    pass
         #print(each)
      while road != startPoint[0:2]:
         # 获取邻居
         #print(road)
         distance = 1000
         result = self.field.getNeighbour(road[0], road[1])
         lastDis = 0
         last_Pace=[]
         #访问该方格所有邻居，以寻求最优路径
         for each in result:
            if each.cellAttr==CellBfs.CellAttribute.OBSTACLE or each.getCellText()=="":
               continue
            di=each.row-road[0]
            dj=each.col-road[1]
            if di and dj:
               n1=self.field.getItem(road[0], each.col).cellAttr
               n2=self.field.getItem(each.row, road[1]).cellAttr
               if n1==CellBfs.CellAttribute.OBSTACLE or n2==CellBfs.CellAttribute.OBSTACLE:
                  continue
            # 在reusltQueue中找到each点对应坐标所对应的路程
            for each1 in resultQueue:
               # 取得对应点距当前点的距离
               if each.row == each1[0] and each.col == each1[1]:
                  lastDis = each1[2]
            if distance > lastDis:
               distance = lastDis
               last_Pace = [each.row, each.col]
         road = last_Pace
         pace.append(last_Pace)
         if road!=startPoint[0:2]:
            self.field.getItem(road[0], road[1]).setCellColor(Qt.yellow)
      print(pace)
      self.ui.widget_Grid.update()
##  ==============自定义功能函数========================


##  ==============event处理函数==========================
        
        
##  ==========由connectSlotsByName()自动连接的槽函数============        

        
##  =============自定义槽函数===============================        

   
##  ============窗体测试程序 ================================
if  __name__ == "__main__":        #用于当前窗体测试
   '''
   生成Cell(继承widget)类的要求：必须先调用QApplication(sys.argv) 这句话
   '''
   app = QApplication(sys.argv)    #创建GUI应用程序
   form=QmyMainWindow()            #创建窗体
   form.show()
   sys.exit(app.exec_())
