import random
import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from ui_file import Ui_MainWindow


class Circle(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.flag = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.flag:
            size = random.randint(1, 150)
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(r, g, b))
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
