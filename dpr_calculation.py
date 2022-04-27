import math

from mainScreen_WIP import *

class dpr_calculation():
	def __init__(self, ui):
		self.num_multi_atk = [3]
		self.num_dmg_dice = [3]
		self.type_dmg_dice = [3]
		self.avg_dmg_dice = [3]
		self.atk_attr = [3]
		self.atk_dmgBns = [3]

		self.atk_dmg = [3]
		
		self.total_dpr = ui.dprSpinBox.value()

		self.cal_dpr(ui)

	def cal_dpr(self, ui):
		self.check_attacks(ui)

	def check_attacks(self, ui):
		multi_atk_checked = ui.multiAttackCheckBox.isChecked()

		if (multi_atk_checked == True):
			print("Multiattack is checked!")

			self.cal_dpr_withMulti(ui)

		elif (multi_atk_checked == False):
			print("Multiattack is unchecked!")

			self.cal_dpr_noMulti(ui)

		else:
			print("Error. Can't determine ui.multiAttackCheckBox.isChecked()")

	def clearData(self):
		self.num_multi_atk.clear()
		self.num_dmg_dice.clear()
		self.type_dmg_dice.clear()
		self.avg_dmg_dice.clear()
		self.atk_attr.clear()
		self.atk_dmgBns.clear()
		self.atk_dmg.clear()
		
		self.total_dpr = 0

	def fillData(self, ui):
		self.num_multi_atk.append(ui.spinBox.value())
		self.num_multi_atk.append(ui.spinBox_2.value())
		self.num_multi_atk.append(ui.spinBox_3.value())
		self.num_multi_atk.append(ui.spinBox_4.value())

		self.num_dmg_dice.append(ui.numDieSpinBox.value())
		self.num_dmg_dice.append(ui.numDieSpinBox_2.value())
		self.num_dmg_dice.append(ui.numDieSpinBox_3.value())
		self.num_dmg_dice.append(ui.numDieSpinBox_4.value())

		self.type_dmg_dice.append(ui.actionDice_1.currentText())
		self.type_dmg_dice.append(ui.actionDice_2.currentText())
		self.type_dmg_dice.append(ui.actionDice_3.currentText())
		self.type_dmg_dice.append(ui.actionDice_4.currentText())

		for i in range(0, 4):
			if (self.type_dmg_dice[i] == "4"):
				self.avg_dmg_dice.append(2.5)
			
			elif (self.type_dmg_dice[i] == "6"):
				self.avg_dmg_dice.append(3.5)

			elif (self.type_dmg_dice[i] == "8"):
				self.avg_dmg_dice.append(4.5)

			elif (self.type_dmg_dice[i] == "10"):
				self.avg_dmg_dice.append(5.5)

			elif (self.type_dmg_dice[i] == "12"):
				self.avg_dmg_dice.append(6.5)

		self.atk_attr.append(ui.attrComboBox_1.currentIndex())
		self.atk_attr.append(ui.attrComboBox_2.currentIndex())
		self.atk_attr.append(ui.attrComboBox_3.currentIndex())
		self.atk_attr.append(ui.attrComboBox_4.currentIndex())

		for i in range(0, 4):
			if (self.atk_attr[i] == 0):
				self.atk_dmgBns.append(self.cal_attr_bns(ui.strSpinBox.value()))
			
			elif (self.atk_attr[i] == 1):
				self.atk_dmgBns.append(self.cal_attr_bns(ui.dexSpinBox.value()))

			elif (self.atk_attr[i] == 2):
				self.atk_dmgBns.append(self.cal_attr_bns(ui.conSpinBox.value()))
			
			elif (self.atk_attr[i] == 3):
				self.atk_dmgBns.append(self.cal_attr_bns(ui.intSpinBox.value()))

			elif (self.atk_attr[i] == 4):
				self.atk_dmgBns.append(self.cal_attr_bns(ui.wisSpinBox.value()))
			
			elif (self.atk_attr[i] == 5):
				self.atk_dmgBns.append(self.cal_attr_bns(ui.chaSpinBox.value()))

			else:
				print("Could not determine element", i, "of dpr_calculation.atk_attr[3]")

	def cal_dpr_withMulti(self, ui):
		print("Should calculate dpr considering multiattack.")
		print()

		self.clearData()
		self.fillData(ui)

		for i in range(0, 4):
			print("Performing:", self.num_multi_atk[i], "* (", self.num_dmg_dice[i], "*", self.avg_dmg_dice[i], "+", self.atk_dmgBns[i], ")")

			dmg = math.floor(self.num_multi_atk[i] * (self.num_dmg_dice[i] * self.avg_dmg_dice[i] + self.atk_dmgBns[i]))

			print("Result:", dmg)
			print()

			self.atk_dmg.append(dmg)

		#self.print_stats()

		for i in range(0, 4):
			self.total_dpr += self.atk_dmg[i]

		print("Total dpr =", self.total_dpr)

		ui.dprSpinBox.setValue(self.total_dpr)

	def cal_dpr_noMulti(self, ui):
		print("Should calculate dpr without multiattack.")
		print()

		self.clearData()

		self.fillData(ui)

		#self.total_dpr = ui.dprSpinBox.value()

		#if (len(self.atk_dmg) != 0):
		#for i in range(0, 4):
		print("Action 1 Name:", ui.actionName_1.text())

		if (ui.actionName_1.text() != ""):
			print("Performing:", self.num_dmg_dice[0], "*", self.avg_dmg_dice[0], "+", self.atk_dmgBns[0])

			dmg = math.floor(self.num_dmg_dice[0] * self.avg_dmg_dice[0] + self.atk_dmgBns[0])

			if (dmg > self.total_dpr):
				self.total_dpr = dmg

		if (ui.actionName_2.text() != ""):
			print("Performing:", self.num_dmg_dice[1], "*", self.avg_dmg_dice[1], "+", self.atk_dmgBns[1])

			dmg = math.floor(self.num_dmg_dice[1] * self.avg_dmg_dice[1] + self.atk_dmgBns[1])

			if (dmg > self.total_dpr):
				self.total_dpr = dmg

		if (ui.actionName_3.text() != ""):
			print("Performing:", self.num_dmg_dice[2], "*", self.avg_dmg_dice[2], "+", self.atk_dmgBns[2])

			dmg = math.floor(self.num_dmg_dice[2] * self.avg_dmg_dice[2] + self.atk_dmgBns[2])

			if (dmg > self.total_dpr):
				self.total_dpr = dmg

		if (ui.actionName_4.text() != ""):
			print("Performing:", self.num_dmg_dice[3], "*", self.avg_dmg_dice[3], "+", self.atk_dmgBns[3])

			dmg = math.floor(self.num_dmg_dice[3] * self.avg_dmg_dice[3] + self.atk_dmgBns[3])

			if (dmg > self.total_dpr):
				self.total_dpr = dmg

		print("Total dpr =", self.total_dpr)

		ui.dprSpinBox.setValue(self.total_dpr)

		#self.print_stats()

	def print_stats(self):
		print("Printing creature dpr-concerned stats")

		for i in range(0, 4):
			print("Attack", i + 1, ": MULTIATTACKs:", self.num_multi_atk[i])
			print("Attack", i + 1, ": NUMBER of damage dice:", self.num_dmg_dice[i])
			#print("Attack", i + 1, ": TYPE of damage dice:", self.type_dmg_dice[i])
			print("Attack", i + 1, ": DIE AVERAGE:", self.avg_dmg_dice[i])
			
			'''
			if (self.atk_attr[i] == 0):
				print("Attack", i + 1, ": ATTRIBUTE: STR")

			elif (self.atk_attr[i] == 1):
				print("Attack", i + 1, ": ATTRIBUTE: DEX")

			elif (self.atk_attr[i] == 2):
				print("Attack", i + 1, ": ATTRIBUTE: CON")

			elif (self.atk_attr[i] == 3):
				print("Attack", i + 1, ": ATTRIBUTE: INT")

			elif (self.atk_attr[i] == 4):
				print("Attack", i + 1, ": ATTRIBUTE: WIS")

			elif (self.atk_attr[i] == 5):
				print("Attack", i + 1, ": ATTRIBUTE: CHA")

			else:
				print("Error. Could not determine element", i, "of dpr_calculation.atk_attr[3]")
			'''

			print("Attack", i + 1, ": DAMAGE BONUS:", self.atk_dmgBns[i])

			print("Attack", i + 1, ": DAMAGE:", self.atk_dmg[i])
			
			print()

	def cal_attr_bns(self, value):
		atr_bns = math.floor((value - 10) / 2)

		return atr_bns