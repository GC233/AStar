"""

作者：Szy
日期：2022年03月11日
"""
from Cell import *
OBSTACLEBRUSH_MODE=16777249
OBSTACLEBRUSH_ABLED=False
#从cell继承，完成brush和Bfs功能
class CellBfs(Cell):
    class CellAttribute:
        OBSTACLE=0
        NOATTR = 1
        STARTPOINT=2
        ENDPOINT=3

        ColorDict={OBSTACLE:Qt.black, STARTPOINT:Qt.blue,
                   ENDPOINT:Qt.red, NOATTR:Qt.gray}
    def __init__(self, row=0, col=0):
        super().__init__(row=row, col=col)
        self.setMouseTracking(True)
        self.setFocusPolicy(Qt.StrongFocus)
        self.grabKeyboard()
        #self.obstacle=False
        self.cellAttr=CellBfs.CellAttribute.NOATTR

    def setCellAttr(self, attr):
        self.cellAttr=attr
        self.setCellColor(CellBfs.CellAttribute.ColorDict[attr])
    def mouseMoveEvent(self, event:QMouseEvent) -> None:
        if OBSTACLEBRUSH_ABLED:
            self.setCellAttr(CellBfs.CellAttribute.OBSTACLE)
            self.update()
    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key()==OBSTACLEBRUSH_MODE:
            global OBSTACLEBRUSH_ABLED
            OBSTACLEBRUSH_ABLED=True
    def keyReleaseEvent(self, event: QKeyEvent) -> None:
        if event.key() == OBSTACLEBRUSH_MODE:
            global OBSTACLEBRUSH_ABLED
            OBSTACLEBRUSH_ABLED = False
    def mousePressEvent(self, event: QMouseEvent) -> None:
        if self.cellAttr==self.CellAttribute.ENDPOINT:
            self.setCellAttr(self.CellAttribute.OBSTACLE)
        else:
            self.setCellAttr(self.cellAttr+1)
        self.update()