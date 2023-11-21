import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calc.ui', self)  # Загружаем дизайн
        # цифры
        for i in self.buttonGroup_digits.buttons():
            i.clicked.connect(self.add_char)
        # (+,-,*,/)
        for i in self.buttonGroup_binary.buttons():
            i.clicked.connect(self.calc)
        # последнее число или последнее вычисленое выражение
        self.data = ""
        # выражение которое нужно подсчиать
        self.data_eval = ""

    def add_char(self):
        self.data += self.sender().text()


    def calc(self):
        self.data_eval = f"{self.data} {self.sender().text() }"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
