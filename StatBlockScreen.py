# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StatBlock.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import random
from PyQt5 import QtCore, QtGui, QtWidgets

numRounds = random.randint(1,10000)
numRoundsWon = random.randint(0, numRounds)
numRoundsLost = numRounds - numRoundsWon

def gcd (n,m):
    d = min(n,m)
    while   n %  d  !=   0  or  m  %  d  !=   0:
        d =  d  -  1
    return  d
def reduce (num, den):
    if num == 0:
      return  (0,   1)
    g =  gcd(num,      den)
    return  (num    //  g,   den   //  g)

num = numRoundsWon
den = numRoundsLost
(n,d) = reduce(num, den)
class Ui_MainWindow(object):
    def exitWin(self):
        pass
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(854, 549)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets/Images/icon_2.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QPushButton{\n"
"     padding: .25em;\n"
"     border: 1px solid black;\n"
"     border-radius: 0.4em;\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: rgb(216, 208, 160);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.winPercentageLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.winPercentageLabel.setFont(font)
        self.winPercentageLabel.setObjectName("winPercentageLabel")
        self.gridLayout.addWidget(self.winPercentageLabel, 4, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 5, 0, 1, 1)
        self.numRoundsLostLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.numRoundsLostLabel.setFont(font)
        self.numRoundsLostLabel.setObjectName("numRoundsLostLabel")
        self.gridLayout.addWidget(self.numRoundsLostLabel, 3, 1, 1, 1)
        self.ratioLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.ratioLabel.setFont(font)
        self.ratioLabel.setObjectName("ratioLabel")
        self.gridLayout.addWidget(self.ratioLabel, 5, 1, 1, 1)
        self.numRoundsWonLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.numRoundsWonLabel.setFont(font)
        self.numRoundsWonLabel.setObjectName("numRoundsWonLabel")
        self.gridLayout.addWidget(self.numRoundsWonLabel, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.numRoundsLabel = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.numRoundsLabel.setFont(font)
        self.numRoundsLabel.setObjectName("numRoundsLabel")
        self.gridLayout.addWidget(self.numRoundsLabel, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.frame,clicked = lambda: MainWindow.close())
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(42, 54, 59);\n"
"background-color: rgb(153, 184, 152);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 0, 1, 2)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 854, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Combat Stats"))
        self.label_3.setText(_translate("MainWindow", "# of Rounds Won:"))
        self.winPercentageLabel.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "Win Percentage:"))
        self.label_4.setText(_translate("MainWindow", "# of Rounds Lost:"))
        self.label_10.setText(_translate("MainWindow", "Actual Simulated CR:"))
        self.numRoundsLostLabel.setText(_translate("MainWindow", "TextLabel"))
        self.ratioLabel.setText(_translate("MainWindow", "TextLabel"))
        self.numRoundsWonLabel.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "# of Rounds:"))
        self.numRoundsLabel.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "Results"))
        self.pushButton.setText(_translate("MainWindow", "Continue"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
