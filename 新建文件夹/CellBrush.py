"""

作者：Szy
日期：2022年03月09日
"""
BRUSH_MODE=16777249
BRUSH_ABLED=False

from Cell import *
#从cell继承，完成brush功能
class CellBrush(Cell):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.setFocusPolicy(Qt.StrongFocus)
        self.grabKeyboard()
    def mouseMoveEvent(self, event:QMouseEvent) -> None:
        if BRUSH_ABLED:
            self.setCellColor(Qt.blue)
            self.update()
    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key()==BRUSH_MODE:
            global BRUSH_ABLED
            BRUSH_ABLED=True
    def keyReleaseEvent(self, event: QKeyEvent) -> None:
        if event.key() == BRUSH_MODE:
            global BRUSH_ABLED
            BRUSH_ABLED = False


