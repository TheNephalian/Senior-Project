# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestMod.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from re import S
from PyQt5 import QtCore, QtGui, QtWidgets
from player import *
from testRunScreen import *
from monster_stats import *
import numpy as np
import matplotlib.pyplot as plt
import combat

##GLOBAL VARIABLES##
x = np.array(range(1, 21))

barbarianY = 14.3538 * np.log(1.6285*x)
barbarianCurve, = plt.plot(x,barbarianY)
barbarianXData = barbarianCurve.get_xdata()
barbarianYData = barbarianCurve.get_ydata()

fighterY = 15.3552 * np.log(1.5775*x)
fighterCurve, = plt.plot(x,fighterY)
fighterXData = fighterCurve.get_xdata()
fighterYData = fighterCurve.get_ydata()

rangerY = 13.0185 * np.log(1.4682*x)
rangerCurve, = plt.plot(x,rangerY)
rangerXData = rangerCurve.get_xdata()
rangerYData = rangerCurve.get_ydata()

rogueY = 11.6833 * np.log(1.5341*x)
rogueCurve, = plt.plot(x,rogueY)
rogueXData = rogueCurve.get_xdata()
rogueYData = rogueCurve.get_ydata()

wizardY = 14.6876 * np.log(1.2266*x)
wizardCurve, = plt.plot(x,wizardY)
wizardXData = wizardCurve.get_xdata()
wizardYData = wizardCurve.get_ydata()

# playerObj = new player()


####################
# def runTest(self):
#     self.window = QtWidgets.QDialog()
#     self.ui = Ui_Dialog()
#     self.ui.setupUi(self.window)
#     self.window.show()
#     thing = self.roundSpinBox.value()
#     self.ui.label_4.setText(str(thing))
#         #numRounds = self.roundSpinBox.value()

#     # def data(self):
#     #     thing = self.roundSpinBox.value()
#     #     self.ui.label_2.setText(thing)


class Ui_testModWindow():
    def __init__(self, creature):
        self.test_creature = creature

        #self.test_creature.print_stats()

    def runTest(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
        numOfRounds = self.roundSpinBox.value()
        self.ui.horizontalSlider.setMaximum(numOfRounds)
        self.ui.label_4.setText(str(numOfRounds))
        self.ui.numRounds = numOfRounds

        
        comSim = combat.combatSimulation(self.test_creature)
        comSim.combatSim()
       
        # for i in  range(numOfRounds):
        #     self.ui.horizontalSlider.setValue(i)
        #     self.ui.label_2.setText(str(numOfRounds))
        #     # battle the characters

        #     print(i)
            
        # print("test completed!")
        #numRounds = self.roundSpinBox.value()

    # def data(self):
    #     thing = self.roundSpinBox.value()
    #     self.ui.label_2.setText(thing)
    def setupUi(self, testModWindow):
        testModWindow.setObjectName("testModWindow")
        testModWindow.resize(854, 244)
        self.centralwidget = QtWidgets.QWidget(testModWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setStyleSheet("QPushButton{\n"
"     padding: .25em;\n"
"     border: 1px solid black;\n"
"     border-radius: 0.4em;\n"
"}\n"
"\n"
"QSpinBox{\n"
"    padding: .25em;\n"
"    border: 1px solid rgb(42, 54, 59);\n"
"    border-bottom: 2px solid rgb(232, 74, 95);\n"
"    border-radius: 5px;\n"
"}QComboBox{\n"
"    \n"
"    padding: .25em;\n"
"    border:1px solid rgb(42, 54, 59);\n"
"    border-bottom: 2px Solid rgb(232, 74, 95);\n"
"    border-radius: 5px;\n"
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 834, 181))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)
        self.creatureComboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.creatureComboBox.setObjectName("creatureComboBox")
        self.gridLayout.addWidget(self.creatureComboBox, 1, 0, 1, 1)
        self.enemyComboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.enemyComboBox.setObjectName("enemyComboBox")
        self.enemyComboBox.addItem("")
        self.enemyComboBox.addItem("")
        self.enemyComboBox.addItem("")
        self.enemyComboBox.addItem("")
        self.enemyComboBox.addItem("")
        self.gridLayout.addWidget(self.enemyComboBox, 1, 1, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(20)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 1, 2, 1, 1)
        self.roundSpinBox = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.roundSpinBox.setMinimum(1)
        self.roundSpinBox.setMaximum(1000)
        self.roundSpinBox.setObjectName("roundSpinBox")
        self.gridLayout.addWidget(self.roundSpinBox, 1, 3, 1, 1)
        self.runTestButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents, clicked = lambda: self.runTest())
        self.runTestButton.setStyleSheet("color: rgb(42, 54, 59);\n"
"background-color: rgb(153, 184, 152);")
        self.runTestButton.setObjectName("runTestButton")
        self.gridLayout.addWidget(self.runTestButton, 1, 4, 1, 1)
        self.enemyComboBox_2 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.enemyComboBox_2.setObjectName("enemyComboBox_2")
        self.enemyComboBox_2.addItem("")
        self.enemyComboBox_2.addItem("")
        self.enemyComboBox_2.addItem("")
        self.enemyComboBox_2.addItem("")
        self.enemyComboBox_2.addItem("")
        self.enemyComboBox_2.addItem("")
        self.gridLayout.addWidget(self.enemyComboBox_2, 2, 1, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(20)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout.addWidget(self.spinBox_2, 2, 2, 1, 1)
        self.enemyComboBox_3 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.enemyComboBox_3.setObjectName("enemyComboBox_3")
        self.enemyComboBox_3.addItem("")
        self.enemyComboBox_3.addItem("")
        self.enemyComboBox_3.addItem("")
        self.enemyComboBox_3.addItem("")
        self.enemyComboBox_3.addItem("")
        self.enemyComboBox_3.addItem("")
        self.gridLayout.addWidget(self.enemyComboBox_3, 3, 1, 1, 1)
        self.spinBox_3 = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(20)
        self.spinBox_3.setObjectName("spinBox_3")
        self.gridLayout.addWidget(self.spinBox_3, 3, 2, 1, 1)
        self.enemyComboBox_4 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.enemyComboBox_4.setObjectName("enemyComboBox_4")
        self.enemyComboBox_4.addItem("")
        self.enemyComboBox_4.addItem("")
        self.enemyComboBox_4.addItem("")
        self.enemyComboBox_4.addItem("")
        self.enemyComboBox_4.addItem("")
        self.enemyComboBox_4.addItem("")
        self.gridLayout.addWidget(self.enemyComboBox_4, 4, 1, 1, 1)
        self.spinBox_4 = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_4.setMinimum(1)
        self.spinBox_4.setMaximum(20)
        self.spinBox_4.setObjectName("spinBox_4")
        self.gridLayout.addWidget(self.spinBox_4, 4, 2, 1, 1)
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

        ####
        self.enemyComboBox.currentIndexChanged.connect(self.enemyValChange)

        self.spinBox.valueChanged.connect(self.enemyLevelChange)

    def retranslateUi(self, testModWindow):
        _translate = QtCore.QCoreApplication.translate
        testModWindow.setWindowTitle(_translate("testModWindow", "Battle Modification Screen"))
        self.label.setText(_translate("testModWindow", "Creature"))
        self.label_2.setText(_translate("testModWindow", "Enemy"))
        self.label_4.setText(_translate("testModWindow", "Level"))
        self.label_3.setText(_translate("testModWindow", "# of Rounds"))
        self.enemyComboBox.setItemText(0, _translate("testModWindow", "Barbarian"))
        self.enemyComboBox.setItemText(1, _translate("testModWindow", "Fighter"))
        self.enemyComboBox.setItemText(2, _translate("testModWindow", "Ranger"))
        self.enemyComboBox.setItemText(3, _translate("testModWindow", "Rogue"))
        self.enemyComboBox.setItemText(4, _translate("testModWindow", "Wizard"))
        self.runTestButton.setText(_translate("testModWindow", "Run Test!"))
        self.enemyComboBox_2.setItemText(0, _translate("testModWindow", "-"))
        self.enemyComboBox_2.setItemText(1, _translate("testModWindow", "Barbarian"))
        self.enemyComboBox_2.setItemText(2, _translate("testModWindow", "Fighter"))
        self.enemyComboBox_2.setItemText(3, _translate("testModWindow", "Ranger"))
        self.enemyComboBox_2.setItemText(4, _translate("testModWindow", "Rogue"))
        self.enemyComboBox_2.setItemText(5, _translate("testModWindow", "Wizard"))
        self.enemyComboBox_3.setItemText(0, _translate("testModWindow", "-"))
        self.enemyComboBox_3.setItemText(1, _translate("testModWindow", "Barbarian"))
        self.enemyComboBox_3.setItemText(2, _translate("testModWindow", "Fighter"))
        self.enemyComboBox_3.setItemText(3, _translate("testModWindow", "Ranger"))
        self.enemyComboBox_3.setItemText(4, _translate("testModWindow", "Rogue"))
        self.enemyComboBox_3.setItemText(5, _translate("testModWindow", "Wizard"))
        self.enemyComboBox_4.setItemText(0, _translate("testModWindow", "-"))
        self.enemyComboBox_4.setItemText(1, _translate("testModWindow", "Barbarian"))
        self.enemyComboBox_4.setItemText(2, _translate("testModWindow", "Fighter"))
        self.enemyComboBox_4.setItemText(3, _translate("testModWindow", "Ranger"))
        self.enemyComboBox_4.setItemText(4, _translate("testModWindow", "Rogue"))
        self.enemyComboBox_4.setItemText(5, _translate("testModWindow", "Wizard"))

    def enemyValChange(self,value):
        print("Enemy value changed!")
        print("New Enemy: " , str(self.enemyComboBox.currentText()))
            
    #Notice:
    #I am using made up numbers for the enemy DPR
    #Barbarian level 1: 7, Level 20: 50
    #Fighter Level 1: 7, Level 20: 53
    #Ranger Level 1: 5, Level 20: 44
    #Rogue Level 1: 5, level 20: 40
    #Wizard Level 1: 3, level 20: 44
    
    def enemyLevelChange(self,value):
        if(self.enemyComboBox.currentText() == "Barbarian"):
            print("Enemy: ", self.enemyComboBox.currentText())
            print("Enemy level: ", str(barbarianXData[int(self.spinBox.value())-1]))
            print("Enemy Damage/Round: ", str(np.rint(barbarianYData[self.spinBox.value()-1])))
            

        elif(self.enemyComboBox.currentText() == "Fighter"):
            print("Enemy: ", self.enemyComboBox.currentText())
            print("Enemy level: ", str(fighterXData[int(self.spinBox.value())-1]))
            print("Enemy Damage/Round: ", str(np.rint(fighterYData[self.spinBox.value()-1])))

            # fighterObject.lvl = fighterXData[int(self.spinBox.value())-1]
            # fighterObject.dmg_per_rnd = np.rint(fighterYData[self.spinBox.value()-1])

            # print("Fighter lvl: ",fighterObject.lvl)
            # print("Fighter DPR: ",fighterObject.dmg_per_rnd)

        elif(self.enemyComboBox.currentText() == "Ranger"):
            print("Enemy: ", self.enemyComboBox.currentText())
            print("Enemy level: ", str(rangerXData[int(self.spinBox.value())-1]))
            print("Enemy Damage/Round: ", str(np.rint(rangerYData[self.spinBox.value()-1])))

        elif(self.enemyComboBox.currentText() == "Rogue"):
            print("Enemy: ", self.enemyComboBox.currentText())
            print("Enemy level: ", str(rogueXData[int(self.spinBox.value())-1]))
            print("Enemy Damage/Round: ", str(np.rint(rogueYData[self.spinBox.value()-1])))

        elif(self.enemyComboBox.currentText() == "Wizard"):
            print("Enemy: ", self.enemyComboBox.currentText())
            print("Enemy level: ", str(wizardXData[int(self.spinBox.value())-1]))
            print("Enemy Damage/Round: ", str(np.rint(wizardYData[self.spinBox.value()-1])))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    testModWindow = QtWidgets.QMainWindow()
    ui = Ui_testModWindow()
    ui.setupUi(testModWindow)
    testModWindow.show()
    sys.exit(app.exec_())
