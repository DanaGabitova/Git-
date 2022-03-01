import random
import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Circle(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Git и желтые окружности')
        self.btn = QPushButton(self)
        self.btn.move(125, 150)
        self.btn.resize(60, 40)
        self.flag = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            for i in range(1, random.randint(3, 6)):
                size = random.randint(1, 150)
                qp.begin(self)
                qp.setBrush(QColor(255, 255, 0))
                qp.drawEllipse(random.randint(0, 150),
                               random.randint(0, 150), size, size)
                qp.end()

    def paint(self):
        self.flag = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    ex.show()
    sys.exit(app.exec())
