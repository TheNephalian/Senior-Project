from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from testing import *
from creatureCR import *

'''Testing of functions'''
function_test()

print(cal_crtr_CR(100, 15, 19, False, 18, 250))

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(320,160,1280,720)
    win.setWindowTitle("2022 Senior project")

    win.show()
    sys.exit(app.exec_())
window()