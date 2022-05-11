# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testRun.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import time
import timeit
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy
from testModScreen import *
from StatBlockScreen import *
from testRunScreen import *
from simulatedResults_WIP import * 
import compare



class testRunDialog(object):
    def __init__(self, creature, players, which_button, rounds):
        self.test_creature = creature
        self.test_players = players
        self.buttonPushed = which_button
        self.num_rounds = rounds
        self.cr_simulate = 0
        self.rounds_won = 0
        self.rounds_loss = 0
        self.w_l_percetage = 0
        self.ratio = " "
        self.arry_info = []
        
        
    def showDetails(self):
        self.window = QtWidgets.QMainWindow()
        if (self.buttonPushed == False):
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.ui.numRoundsLabel.setText(str(self.cr_simulate))
            self.ui.numRoundsWonLabel.setText(str(self.rounds_won))
            self.ui.numRoundsLostLabel.setText(str(self.rounds_loss))
            percentage_w_l = str(self.w_l_percetage)
            percentage_w_l += "%"
            self.ui.winPercentageLabel.setText(percentage_w_l)
            self.ui.ratioLabel.setText(str(self.ratio))
            self.window.show()
        else:
            self.ui = Ui_simulatedWindow()
            self.ui.setupUi(self.window)
            final_string = " "
            for i in self.arry_info:
                lvl = i["lvl"]
                wins = i["wins"]
                rounds = i["rounds"]
                creature_wins = rounds - wins 
                win_rate = creature_wins / rounds
                win_rate = win_rate * 100
                win_rate = "{:.2f}".format(win_rate)
                final_string += "   " + str(rounds) + " Combats simulated against Player Level: " +str(lvl) 
                final_string += "\n"
                final_string += " Player Wins: " + str(wins) + "  Creature wins: " + str(creature_wins) + "  Creature winrate: " + str(win_rate) + "%"
                final_string += "\n"
                final_string += "\n"
            final_string += "\n" + "   Creature CR: " + str(self.test_creature.challnge_rtg) + "  Simulated CR: " + str(self.ratio)
            self.ui.label_2.setText(final_string)
            self.window.show()

    def runProgressbar(self):
        self.progressBar.setMaximum(100_000)
        compSim = compare.compareCRandEC(self.test_creature, self.test_players)
        if (self.buttonPushed == False):
            compSim.generate_cr_simulation(self.numRounds)
        elif(self.buttonPushed == True):
            rp = 1
            num_rounds_won = 0
            arry_lvls = []
            compSim.final_solution(rp, num_rounds_won, arry_lvls)
        for i  in range(100_000):
            self.progressBar.setValue(i+1)
        if(self.progressBar.value()==self.progressBar.maximum()):
            self.cr_simulate = compSim.num_rounds
            self.rounds_won = compSim.num_rounds - compSim.players_wins
            self.rounds_loss = compSim.players_wins
            self.w_l_percetage = self.rounds_won / self.cr_simulate
            self.w_l_percetage = self.w_l_percetage * 100
            self.w_l_percetage = "{:.2f}".format(self.w_l_percetage)
            self.ratio = compSim.sim_cr 
            self.arry_info = compSim.store_info
            self.testCompleteLabel.show()
            self.showDetails()

    def setupUi(self, Dialog):
        self.numRounds = 12
        Dialog.setObjectName("Run Test")
        Dialog.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets/Images/icon_2.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.scrollArea.setFont(font)
        self.scrollArea.setStyleSheet("\n"
                                      "QProgressBar {\n"
                                      "      border: 2px solid grey;\n"
                                      "      border-radius: 5px;\n"
                                      "  }\n"
                                      "\n"
                                      "  QProgressBar::chunk {\n"
                                      "      background-color: rgb(232, 74, 95);\n"
                                      "      width: 20px;\n"
                                      "  }\n"
                                      "QProgressBar {\n"
                                      "      border: 2px solid grey;\n"
                                      "      border-radius: 5px;\n"
                                      "      text-align: center;\n"
                                      "  }\n"
                                      "QPushButton{\n"
                                      "    color: black;\n"
                                      "    background-color: #ccc;\n"
                                      "     padding: .25em;\n"
                                      "     border: 1px solid black;\n"
                                      "     border-radius: 0.4em;\n"
                                      "}\n"
                                      "\n"
                                      "")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 380, 280))
        self.scrollAreaWidgetContents.setStyleSheet(
            "background-color: rgb(216, 208, 160);")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_5.hide()
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(
            self.scrollAreaWidgetContents)
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
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_2.hide()
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(
            self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(30)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 2, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_3.hide()
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.calculatedCRLabel = QtWidgets.QLabel(
            self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.calculatedCRLabel.setFont(font)
        self.calculatedCRLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.calculatedCRLabel.setObjectName("calculatedCRLabel")
        self.calculatedCRLabel.hide()
        self.gridLayout.addWidget(self.calculatedCRLabel, 1, 0, 1, 1)
        self.testCompleteLabel = QtWidgets.QLabel(
            self.scrollAreaWidgetContents)
        self.testCompleteLabel.setEnabled(True)
        self.testCompleteLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.testCompleteLabel.hide()
        font = QtGui.QFont()
        font.setFamily("Merriweather")
        self.testCompleteLabel.setFont(font)
        self.testCompleteLabel.setStyleSheet("")
        self.testCompleteLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.testCompleteLabel.setObjectName("testCompleteLabel")
        self.gridLayout.addWidget(self.testCompleteLabel, 3, 0, 1, 2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.runProgressbar)
        self.pushButton.clicked.connect(Dialog.close)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Run Test"))
        self.label_5.setText(_translate("Dialog", "Calculating..."))
        self.pushButton.setText(_translate("Dialog", "Run Test"))
        self.label_2.setText(_translate("Dialog", "Calculated CR:"))
        self.label_3.setText(_translate("Dialog", "Simulated CR:"))
        self.calculatedCRLabel.setText(_translate("Dialog", "CR GOES HERE"))
        self.testCompleteLabel.setText(_translate(
            "Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Test Complete !</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = testRunDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
