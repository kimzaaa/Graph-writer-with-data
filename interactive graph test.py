import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Canvas(FigureCanvas):
    def __init__(self,parent):
        fig, self.ax = plt.subplots(figsize=(5,4), dpi = 200)
        super().__init__(fig)
        self.setParent(parent)

        x = ["2024-1-1","2024-1-2","2024-1-3","2024-1-4","2024-1-5"]
        y = [10,30,20,60,50]

        self.ax.plot(x,y)

        self.ax.set(xlabel='Date',ylabel='Ev value',title='Ev value by date graph')
        self.ax.grid()

class AppDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1600,900)

        self.chart = Canvas(self)
        self.chart.move(500,40)

app = QApplication(sys.argv)
demo = AppDemo()
demo.show()
sys.exit(app.exec_())