import sys
import random

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class Cirles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        try:
            qp.setPen(QColor(255, 255, 0))
            qp.setBrush(QColor(255, 255, 0))
            x = random.randint(0, 790)
            y = random.randint(0, 590)
            radius = random.randint(10, 100)
            if x + radius > 800:
                x -= radius
            if y + radius > 600:
                y -= radius
            print(x, y, radius)
            qp.drawEllipse(self, x, y, radius, radius)
        except Exception as e:
            print(e)

if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = Cirles()
        ex.show()
        sys.exit(app.exec_())
