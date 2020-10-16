from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import os

program_name = "Stock Analizer"
window_width = 500
window_height = 500
window_x = 500
window_y = 100

#Tworzymy klasę dziedziczącą od klasy QMainWindow
class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__() #Rozszerzamy funkcję inicjalizującą
        self.setGeometry(window_x, window_y, window_width, window_height)
        self.setWindowTitle("My Window!")
        self.initUI()

    #Incjalizujemy UI
    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("My first label!")
        self.label.move(50, 50)

        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Click me!")
        self.button.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("You pressed the button")

    def draw_diagram(self, data_x, data_y):
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        self.graphWidget.plot(data_x, data_y)

def main():
    hour = [i for i in range(10, 50, 1)]
    temp = [x**-2 for x in hour]

    app = QApplication(sys.argv)
    win = MyWindow()
    win.draw_diagram(hour, temp)
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
