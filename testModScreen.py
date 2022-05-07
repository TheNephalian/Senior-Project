# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestMod.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from re import S
from types import new_class
from PyQt5 import QtCore, QtGui, QtWidgets
from dummyPlayers import dummyFighter, dummyRanger, dummyRogue, dummyWizard
from player import *
from testRunScreen import *
from monster_stats import *
import numpy as np
import matplotlib.pyplot as plt
import combat
from testRunScreen import testRunDialog
import compare


##GLOBAL VARIABLES##
x = np.array(range(1, 21))

barbarianY = 14.3538 * np.log(1.6285*x)
barbarianCurve, = plt.plot(x, barbarianY)
barbarianXData = barbarianCurve.get_xdata()
barbarianYData = barbarianCurve.get_ydata()


fighterY = 15.3552 * np.log(1.5775*x)
fighterHpY = 50.405 * np.log(1.2194*x)
fighterCurve, = plt.plot(x, fighterY)
fighterHpCurve, = plt.plot(x, fighterHpY)
fighterXData = fighterCurve.get_xdata()
fighterYData = fighterCurve.get_ydata()
fighterHpYdata = fighterHpCurve.get_ydata()

rangerY = 13.0185 * np.log(1.4682*x)
rangerHpY = 50.405 * np.log(1.2194*x)
rangerCurve, = plt.plot(x, rangerY)
rangerHpCurve, = plt.plot(x,rangerHpY)
rangerXData = rangerCurve.get_xdata()
rangerYData = rangerCurve.get_ydata()
rangerHpYData = rangerHpCurve.get_ydata()

rogueY = 11.6833 * np.log(1.5341*x)
rogueHpY = 38.3879 * np.log(1.2317*x)
rogueCurve, = plt.plot(x, rogueY)
rogueHpCurve, = plt.plot(x,rogueHpY)
rogueXData = rogueCurve.get_xdata()
rogueYData = rogueCurve.get_ydata()
rogueHpYData = rogueHpCurve.get_ydata()

wizardY = 14.6876 * np.log(1.2266*x)
wizardHpY = 38.3879 * np.log(1.2317*x)
wizardCurve, = plt.plot(x, wizardY)
wizardHpCurve, = plt.plot(x, wizardHpY)
wizardXData = wizardCurve.get_xdata()
wizardYData = wizardCurve.get_ydata()
wizardHpYData = wizardHpCurve.get_ydata()

####################


class Ui_testModWindow(creature):
    def __init__(self, creature):
        self.test_creature = creature
        self.players = []

    #     #self.test_creature.print_stats()

    def runTest(self):
        self.window = QtWidgets.QDialog()
        self.ui = testRunDialog()
        self.ui.setupUi(self.window)
        self.window.show()
        numOfRounds = self.roundSpinBox.value()
        self.ui.progressBar.setMaximum(numOfRounds)
        # self.ui.label_4.setText(str(numOfRounds))
        self.ui.numRounds = numOfRounds

        if(self.enemyComboBox.currentText() == "Fighter"):
            player1 = dummyFighter.Fighter()
            player1.lvl_change(self.spinBox.value())
            player1.dpr_change(np.rint(fighterYData[self.spinBox.value()-1]))
            player1.hp_change(np.rint(fighterHpYdata[self.spinBox.value()-1]))
            self.players.append(player1)

        elif(self.enemyComboBox.currentText() == "Ranger"):
            player1 = dummyRanger.Ranger()
            player1.lvl_change(self.spinBox.value())
            player1.dpr_change(np.rint(rangerYData[self.spinBox.value()-1]))
            player1.hp_change(np.rint(rangerHpYData[self.spinBox.value()-1]))
            self.players.append(player1)

        elif(self.enemyComboBox.currentText() == "Rogue"):
            player1 = dummyRogue.Rogue()
            player1.lvl_change(self.spinBox.value())
            player1.dpr_change(np.rint(rogueYData[self.spinBox.value()-1]))
            player1.hp_change(np.rint(rogueHpYData[self.spinBox.value()-1]))
            self.players.append(player1)

        elif(self.enemyComboBox.currentText() == "Wizard"):
            player1 = dummyWizard.Wizard()
            player1.lvl_change(self.spinBox.value())
            player1.dpr_change(np.rint(rogueYData[self.spinBox.value()-1]))
            player1.hp_change(np.rint(wizardHpYData[self.spinBox.value()-1]))
            self.players.append(player1)

        print("ATTENTION: Player 1 : ", player1.name, "Level:", str(player1.lvl), "DPR:", str(player1.dmg_per_rnd),"HP:", str(player1.hp))

        if(self.enemyComboBox_2.currentText() != "-"):
            if(self.enemyComboBox_2.currentText() == "Fighter"):
                player2 = dummyFighter.Fighter()
                player2.lvl_change(self.spinBox_2.value())
                player2.dpr_change(np.rint(rogueYData[self.spinBox_2.value()-1]))
                player2.hp_change(np.rint(fighterHpYdata[self.spinBox_2.value()-1]))
                self.players.append(player2)

            elif(self.enemyComboBox_2.currentText() == "Ranger"):
                player2 = dummyRanger.Ranger()
                player2.lvl_change(self.spinBox_2.value())
                player2.dpr_change(np.rint(rangerYData[self.spinBox_2.value()-1]))
                player2.hp_change(np.rint(rangerHpYData[self.spinBox.value()-1]))
                self.players.append(player2)

            elif(self.enemyComboBox_2.currentText() == "Rogue"):
                player2 = dummyRogue.Rogue()
                player2.lvl_change(self.spinBox_2.value())
                player2.dpr_change(np.rint(rogueYData[self.spinBox_2.value()-1]))
                player2.hp_change(np.rint(rogueHpYData[self.spinBox_2.value()-1]))
                self.players.append(player2)

            elif(self.enemyComboBox_2.currentText() == "Wizard"):
                player2 = dummyWizard.Wizard()
                player2.lvl_change(self.spinBox_2.value())
                player2.dpr_change(np.rint(wizardYData[self.spinBox_2.value()-1]))
                player2.hp_change(np.rint(wizardHpYData[self.spinBox_2.value()-1]))
                self.players.append(player2)

            print("ATTENTION: Player 2 : ", player2.name, "Level:", str(player2.lvl), "DPR:", str(player2.dmg_per_rnd),"HP:", str(player2.hp))

        else:
            print("player 2 is blank")

        if(self.enemyComboBox_3.currentText() != "-"):
            if(self.enemyComboBox_3.currentText() == "Fighter"):
                player3 = dummyFighter.Fighter()
                player3.lvl_change(self.spinBox_3.value())
                player3.dpr_change(np.rint(fighterYData[self.spinBox_3.value()-1]))
                player3.hp_change(np.rint(fighterHpYdata[self.spinBox_3.value()-1]))
                self.players.append(player3)

            elif(self.enemyComboBox_3.currentText() == "Ranger"):
                player3 = dummyRanger.Ranger()
                player3.lvl_change(self.spinBox_3.value())
                player3.dpr_change(np.rint(rangerYData[self.spinBox_3.value()-1]))
                player3.hp_change(np.rint(rangerHpYData[self.spinBox_3.value()-1]))
                self.players.append(player3)

            elif(self.enemyComboBox_3.currentText() == "Rogue"):
                player3 = dummyRogue.Rogue()
                player3.lvl_change(self.spinBox_3.value())
                player3.dpr_change(np.rint(rogueYData[self.spinBox_3.value()-1]))
                player3.hp_change(np.rint(rogueHpYData[self.spinBox_3.value()-1]))
                self.players.append(player3)

            elif(self.enemyComboBox_3.currentText() == "Wizard"):
                player3 = dummyWizard.Wizard()
                player3.lvl_change(self.spinBox_3.value())
                player3.dpr_change(np.rint(wizardYData[self.spinBox_3.value()-1]))
                player3.hp_change(np.rint(wizardHpYData[self.spinBox_3.value()-1]))
                self.players.append(player3)

            print("ATTENTION: Player 3 : ", player3.name, "Level:", str(player3.lvl), "DPR:", str(player3.dmg_per_rnd),"HP:", str(player3.hp))

        else:
            print("Player 3 is Blank")

        if(self.enemyComboBox_4.currentText() != "-"):
            if(self.enemyComboBox_4.currentText() == "Fighter"):
                player4 = dummyFighter.Fighter()
                player4.lvl_change(self.spinBox_4.value())
                player4.dpr_change(np.rint(fighterYData[self.spinBox_4.value()-1]))
                player4.hp_change(np.rint(fighterHpYdata[self.spinBox_4.value()-1]))
                self.players.append(player4)

            elif(self.enemyComboBox_4.currentText() == "Ranger"):
                player4 = dummyRanger.Ranger()
                player4.lvl_change(self.spinBox_4.value())
                player4.dpr_change(np.rint(rangerYData[self.spinBox_4.value()-1]))
                player4.hp_change(np.rint(rangerHpYData[self.spinBox_4.value()-1]))
                self.players.append(player4)

            elif(self.enemyComboBox_4.currentText() == "Rogue"):
                player4 = dummyRogue.Rogue()
                player4.lvl_change(self.spinBox_4.value())
                player4.dpr_change(np.rint(rogueYData[self.spinBox_4.value()-1]))
                player4.hp_change(np.rint(rogueHpYData[self.spinBox_4.value()-1]))
                self.players.append(player4)

            elif(self.enemyComboBox_4.currentText() == "Wizard"):
                player4 = dummyWizard.Wizard()
                player4.lvl_change(self.spinBox_4.value())
                player4.dpr_change(np.rint(wizardYData[self.spinBox_4.value()-1]))
                player4.hp_change(np.rint(wizardHpYData[self.spinBox_4.value()-1]))
                self.players.append(player4)

            print("ATTENTION: Player 4 : ", player4.name, "Level:", str(player4.lvl), "DPR:", str(player4.dmg_per_rnd),"HP:", str(player4.hp))

        else:
            print("Player 4 is Blank")

        print(*self.players)
        #comSim = combat.combatSimulation(self.test_creature, self.players)
        #comSim.combatSim()
        compSim = compare.compareCRandEC(self.test_creature, self.players)
        compSim.final_solution()



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
        self.runTestButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents,clicked=lambda: self.runTest())
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
        # self.pushButton.setEnabled(False)
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

        self.enemyComboBox_2.currentIndexChanged.connect(self.enemyValChange)

        self.spinBox.valueChanged.connect(self.enemyLevelChange)

    def retranslateUi(self, testModWindow):
        _translate = QtCore.QCoreApplication.translate
        testModWindow.setWindowTitle(_translate("testModWindow", "Battle Modification Screen"))
        self.enemyComboBox_4.setItemText(0, _translate("testModWindow", "-"))
        self.enemyComboBox_4.setItemText(1, _translate("testModWindow", "Fighter"))
        self.enemyComboBox_4.setItemText(2, _translate("testModWindow", "Ranger"))
        self.enemyComboBox_4.setItemText(3, _translate("testModWindow", "Rogue"))
        self.enemyComboBox_4.setItemText(4, _translate("testModWindow", "Wizard"))
        self.label_4.setText(_translate("testModWindow", "Level"))
        self.label.setText(_translate("testModWindow", "Creature"))
        self.label_5.setText(_translate("testModWindow", "Generated Simulated CR"))
        self.runTestButton.setText(_translate("testModWindow", "Run Test!"))
        self.pushButton.setText(_translate("testModWindow", "Generate"))
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
    def enemyValChange(self, value):
        print("Enemy value changed!")
        print("New Enemy: ", str(self.enemyComboBox.currentText()))
        if(self.enemyComboBox_2.currentText != "-" and self.enemyComboBox_3.currentText != "-" and self.enemyComboBox_4.currentText != "-"):
            self.pushButton.setEnabled(True)

    # Notice:
    # I am using made up numbers for the enemy DPR
    # Barbarian level 1: 7, Level 20: 50
    # Fighter Level 1: 7, Level 20: 53
    # Ranger Level 1: 5, Level 20: 44
    # Rogue Level 1: 5, level 20: 40
    # Wizard Level 1: 3, level 20: 44

    def enemyLevelChange(self, value):
        if(self.enemyComboBox.currentText() == "Barbarian"):
            print("Enemy: ", self.enemyComboBox.currentText())
            print("Enemy level: ", str(
                barbarianXData[int(self.spinBox.value())-1]))
            print("Enemy Damage/Round: ",
                  str(np.rint(barbarianYData[self.spinBox.value()-1])))

        elif(self.enemyComboBox.currentText() == "Fighter"):
            print("Enemy: ", self.enemyComboBox.currentText())
            print("Enemy level: ", str(
                fighterXData[int(self.spinBox.value())-1]))
            print("Enemy Damage/Round: ",
                  str(np.rint(fighterYData[self.spinBox.value()-1])))

        elif(self.enemyComboBox.currentText() == "Ranger"):
            print("Enemy: ", self.enemyComboBox.currentText())
            print("Enemy level: ", str(
                rangerXData[int(self.spinBox.value())-1]))
            print("Enemy Damage/Round: ",
                  str(np.rint(rangerYData[self.spinBox.value()-1])))

        elif(self.enemyComboBox.currentText() == "Rogue"):
            print("Enemy: ", self.enemyComboBox.currentText())
            print("Enemy level: ", str(
                rogueXData[int(self.spinBox.value())-1]))
            print("Enemy Damage/Round: ",
                  str(np.rint(rogueYData[self.spinBox.value()-1])))

        elif(self.enemyComboBox.currentText() == "Wizard"):
            print("Enemy: ", self.enemyComboBox.currentText())
            print("Enemy level: ", str(
                wizardXData[int(self.spinBox.value())-1]))
            print("Enemy Damage/Round: ",
                  str(np.rint(wizardYData[self.spinBox.value()-1])))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    testModWindow = QtWidgets.QMainWindow()
    ui = Ui_testModWindow(creature)
    ui.setupUi(testModWindow)
    testModWindow.show()
    sys.exit(app.exec_())
