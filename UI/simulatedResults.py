# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simulatedResults.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_simulatedWindow(object):
    def setupUi(self, simulatedWindow):
        simulatedWindow.setObjectName("simulatedWindow")
        simulatedWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(simulatedWindow)
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
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 760, 457))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setStyleSheet("background-color: rgba(232, 217, 219,90);\n"
"border-left : 3px solid rgb(232, 74, 95);\n"
"border-right: 3px solid rgb(232, 74, 95);\n"
"")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(42, 54, 59);\n"
"background-color: rgb(153, 184, 152);")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.frame)
        simulatedWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(simulatedWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        simulatedWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(simulatedWindow)
        self.statusbar.setObjectName("statusbar")
        simulatedWindow.setStatusBar(self.statusbar)

        self.retranslateUi(simulatedWindow)
        QtCore.QMetaObject.connectSlotsByName(simulatedWindow)

    def retranslateUi(self, simulatedWindow):
        _translate = QtCore.QCoreApplication.translate
        simulatedWindow.setWindowTitle(_translate("simulatedWindow", "MainWindow"))
        self.label.setText(_translate("simulatedWindow", "Results:"))
        self.label_2.setText(_translate("simulatedWindow", "EXPlanation goes here"))
        self.pushButton.setText(_translate("simulatedWindow", "Continue"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    simulatedWindow = QtWidgets.QMainWindow()
    ui = Ui_simulatedWindow()
    ui.setupUi(simulatedWindow)
    simulatedWindow.show()
    sys.exit(app.exec_())
