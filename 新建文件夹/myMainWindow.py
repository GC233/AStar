# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_MainWindow import Ui_MainWindow

from CellBrush import *
class QmyMainWindow(QMainWindow):
   def __init__(self, parent=None):

      super().__init__(parent)   #调用父类构造函数，创建窗体
      self.ui=Ui_MainWindow()    #创建UI对象
      self.ui.setupUi(self)      #构造UI界面
      w = self.ui.widget_Grid
      w.setMouseTracking(True)
      self.setMouseTracking(True)
      #self.setCentralWidget(w)
      field = CellField(CellBrush, 20, 20)
      CellView.setView(wgt=w, field=field)

      
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
