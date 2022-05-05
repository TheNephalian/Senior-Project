# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestMod.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_testModWindow(object):
    def setupUi(self, testModWindow):
        testModWindow.setObjectName("testModWindow")
        testModWindow.resize(854, 247)
        self.centralwidget = QtWidgets.QWidget(testModWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.scrollArea.setFont(font)
        self.scrollArea.setStyleSheet("QPushButton{\n"
"    color: rgb(0, 0, 0);\n"
"     padding: .25em;\n"
"     border: 1px solid black;\n"
"     border-radius: 0.4em;\n"
"}\n"
"QSpinBox{\n"
"    padding: .25em;\n"
"    border: 1px solid rgb(42, 54, 59);\n"
"    border-bottom: 2px solid rgb(232, 74, 95);\n"
"    border-radius: 5px;\n"
"}\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right; \n"
"    image: url(/Users/theor/Documents/School Work/Spring 2022/Senior-Project/Assets/Images/thinUpArrow.png);\n"
"    width: 18px;\n"
"    height: 18px;\n"
"}\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right; \n"
"    image: url(/Users/theor/Documents/School Work/Spring 2022/Senior-Project/Assets/Images/thinDownArrow.png);\n"
"    width: 18px;\n"
"    height: 18px;\n"
"}\n"
"QComboBox{\n"
"    \n"
"    padding: .25em;\n"
"    border:1px solid rgb(42, 54, 59);\n"
"    border-bottom: 2px Solid rgb(232, 74, 95);\n"
"    border-radius: 5px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: url(/Users/theor/Documents/School Work/Spring 2022/Senior-Project/Assets/Images/thinDownArrow.png);\n"
"    width:16px;\n"
"    height:16px\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: rgb(42, 54, 59);\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 834, 184))
        self.scrollAreaWidgetContents.setStyleSheet("background-color: rgb(216, 208, 160);")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.enemyComboBox_4 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.enemyComboBox_4.setFont(font)
        self.enemyComboBox_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.enemyComboBox_4.setObjectName("enemyComboBox_4")
        self.enemyComboBox_4.addItem("")
        self.enemyComboBox_4.addItem("")
        self.enemyComboBox_4.addItem("")
        self.enemyComboBox_4.addItem("")
        self.enemyComboBox_4.addItem("")
        self.gridLayout.addWidget(self.enemyComboBox_4, 5, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 3, 1, 2)
        self.spinBox_3 = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.spinBox_3.setFont(font)
        self.spinBox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(20)
        self.spinBox_3.setObjectName("spinBox_3")
        self.gridLayout.addWidget(self.spinBox_3, 4, 2, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.spinBox.setFont(font)
        self.spinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(20)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 2, 2, 1, 1)
        self.roundSpinBox = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.roundSpinBox.setFont(font)
        self.roundSpinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.roundSpinBox.setMinimum(1)
        self.roundSpinBox.setObjectName("roundSpinBox")
        self.gridLayout.addWidget(self.roundSpinBox, 2, 3, 1, 1)
        self.runTestButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.runTestButton.setFont(font)
        self.runTestButton.setStyleSheet("color: rgb(42, 54, 59);\n"
"background-color: rgb(153, 184, 152);")
        self.runTestButton.setObjectName("runTestButton")
        self.gridLayout.addWidget(self.runTestButton, 2, 4, 1, 1)
        self.creatureComboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.creatureComboBox.setFont(font)
        self.creatureComboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.creatureComboBox.setObjectName("creatureComboBox")
        self.gridLayout.addWidget(self.creatureComboBox, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton:disabled {\n"
"                        background-color: gray;\n"
"            }\n"
"QPushButton:enabled{\n"
"    background-color: rgb(204, 204, 204);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 3, 1, 2)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 3, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)
        self.enemyComboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.enemyComboBox.setFont(font)
        self.enemyComboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.enemyComboBox.setObjectName("enemyComboBox")
        self.enemyComboBox.addItem("")
        self.enemyComboBox.addItem("")
        self.enemyComboBox.addItem("")
        self.enemyComboBox.addItem("")
        self.gridLayout.addWidget(self.enemyComboBox, 2, 1, 1, 1)
        self.spinBox_4 = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.spinBox_4.setFont(font)
        self.spinBox_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox_4.setMinimum(1)
        self.spinBox_4.setMaximum(20)
        self.spinBox_4.setObjectName("spinBox_4")
        self.gridLayout.addWidget(self.spinBox_4, 5, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.enemyComboBox_2 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.enemyComboBox_2.setFont(font)
        self.enemyComboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.enemyComboBox_2.setObjectName("enemyComboBox_2")
        self.enemyComboBox_2.addItem("")
        self.enemyComboBox_2.addItem("")
        self.enemyComboBox_2.addItem("")
        self.enemyComboBox_2.addItem("")
        self.enemyComboBox_2.addItem("")
        self.gridLayout.addWidget(self.enemyComboBox_2, 3, 1, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.spinBox_2.setFont(font)
        self.spinBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(20)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout.addWidget(self.spinBox_2, 3, 2, 1, 1)
        self.enemyComboBox_3 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.enemyComboBox_3.setFont(font)
        self.enemyComboBox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.enemyComboBox_3.setObjectName("enemyComboBox_3")
        self.enemyComboBox_3.addItem("")
        self.enemyComboBox_3.addItem("")
        self.enemyComboBox_3.addItem("")
        self.enemyComboBox_3.addItem("")
        self.enemyComboBox_3.addItem("")
        self.gridLayout.addWidget(self.enemyComboBox_3, 4, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 5)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        testModWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(testModWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 854, 22))
        self.menubar.setObjectName("menubar")
        testModWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(testModWindow)
        self.statusbar.setObjectName("statusbar")
        testModWindow.setStatusBar(self.statusbar)

        self.retranslateUi(testModWindow)
        QtCore.QMetaObject.connectSlotsByName(testModWindow)

    def retranslateUi(self, testModWindow):
        _translate = QtCore.QCoreApplication.translate
        testModWindow.setWindowTitle(_translate("testModWindow", "MainWindow"))
        self.enemyComboBox_4.setItemText(0, _translate("testModWindow", "-"))
        self.enemyComboBox_4.setItemText(1, _translate("testModWindow", "Fighter"))
        self.enemyComboBox_4.setItemText(2, _translate("testModWindow", "Ranger"))
        self.enemyComboBox_4.setItemText(3, _translate("testModWindow", "Rogue"))
        self.enemyComboBox_4.setItemText(4, _translate("testModWindow", "Wizard"))
        self.label_4.setText(_translate("testModWindow", "Level"))
        self.label.setText(_translate("testModWindow", "Creature"))
        self.label_5.setText(_translate("testModWindow", "Genorate Simulated CR"))
        self.runTestButton.setText(_translate("testModWindow", "Run Test!"))
        self.pushButton.setText(_translate("testModWindow", "Genorate"))
        self.label_3.setText(_translate("testModWindow", "# of Rounds"))
        self.enemyComboBox.setItemText(0, _translate("testModWindow", "Fighter"))
        self.enemyComboBox.setItemText(1, _translate("testModWindow", "Ranger"))
        self.enemyComboBox.setItemText(2, _translate("testModWindow", "Rogue"))
        self.enemyComboBox.setItemText(3, _translate("testModWindow", "Wizard"))
        self.label_2.setText(_translate("testModWindow", "Enemy"))
        self.enemyComboBox_2.setItemText(0, _translate("testModWindow", "-"))
        self.enemyComboBox_2.setItemText(1, _translate("testModWindow", "Fighter"))
        self.enemyComboBox_2.setItemText(2, _translate("testModWindow", "Ranger"))
        self.enemyComboBox_2.setItemText(3, _translate("testModWindow", "Rogue"))
        self.enemyComboBox_2.setItemText(4, _translate("testModWindow", "Wizard"))
        self.enemyComboBox_3.setItemText(0, _translate("testModWindow", "-"))
        self.enemyComboBox_3.setItemText(1, _translate("testModWindow", "Fighter"))
        self.enemyComboBox_3.setItemText(2, _translate("testModWindow", "Ranger"))
        self.enemyComboBox_3.setItemText(3, _translate("testModWindow", "Rogue"))
        self.enemyComboBox_3.setItemText(4, _translate("testModWindow", "Wizard"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    testModWindow = QtWidgets.QMainWindow()
    ui = Ui_testModWindow()
    ui.setupUi(testModWindow)
    testModWindow.show()
    sys.exit(app.exec_())
