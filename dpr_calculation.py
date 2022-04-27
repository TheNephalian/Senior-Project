import math

from mainScreen_WIP import *

class dpr_calculation():
	def __init__(self, ui):
		self.atk_bns = [3]
		self.num_dmg_dice = [3]
		self.type_dmg_dice = [3]
		self.atk_attr = [3]

		self.set_atk_bns_arr(ui)

	def set_atk_bns_arr(self, ui):
		print(ui.strSpinBox.value())

		self.atk_bns.append(self.set_atk_bns1(ui))
		self.atk_bns.append(self.set_atk_bns2(ui))
		self.atk_bns.append(self.set_atk_bns3(ui))
		self.atk_bns.append(self.set_atk_bns4(ui))

		self.print_stats()

	def print_stats(self):
		print("First attack:")
		print("	Attack Bonus:", self.atk_bns[0])

		print("Second attack:")
		print("	Attack Bonus:", self.atk_bns[1])

		print("Third attack:")
		print("	Attack Bonus:", self.atk_bns[2])

		print("Fourth attack:")
		print("	Attack Bonus:", self.atk_bns[3])

	def cal_attr_bns(self, value):
		atr_bns = math.floor((value - 10) / 2)

		return atr_bns

	def set_atk_bns1(self, window):
		if (window.attrComboBox_1.currentIndex() == 0):
			self.atk_bns[0] = (self.cal_attr_bns(window.strSpinBox.value()))
			
		elif (window.attrComboBox_1.currentIndex() == 1):
			self.atk_bns[0] = (self.cal_attr_bns(window.dexSpinBox.value()))

		elif (window.attrComboBox_1.currentIndex() == 2):
			self.atk_bns[0] = (self.cal_attr_bns(window.conSpinBox.value()))

		elif (window.attrComboBox_1.currentIndex() == 3):
			self.atk_bns[0] = (self.cal_attr_bns(window.intSpinBox.value()))

		elif (window.attrComboBox_1.currentIndex() == 4):
			self.atk_bns[0] = (self.cal_attr_bns(window.wisSpinBox.value()))

		elif (window.attrComboBox_1.currentIndex() == 5):
			self.atk_bns[0] = (self.cal_attr_bns(window.chaSpinBox.value()))

	def set_atk_bns2(self, window):
		if (window.attrComboBox_2.currentIndex() == 0):
			self.atk_bns[1] = (self.cal_attr_bns(window.strSpinBox.value()))
			
		elif (window.attrComboBox_2.currentIndex() == 1):
			self.atk_bns[1] = (self.cal_attr_bns(window.dexSpinBox.value()))

		elif (window.attrComboBox_2.currentIndex() == 2):
			self.atk_bns[1] = (self.cal_attr_bns(window.conSpinBox.value()))

		elif (window.attrComboBox_2.currentIndex() == 3):
			self.atk_bns[1] = (self.cal_attr_bns(window.intSpinBox.value()))

		elif (window.attrComboBox_2.currentIndex() == 4):
			self.atk_bns[1] = (self.cal_attr_bns(window.wisSpinBox.value()))

		elif (window.attrComboBox_2.currentIndex() == 5):
			self.atk_bns[1] = (self.cal_attr_bns(window.chaSpinBox.value()))

	def set_atk_bns3(self, window):
		if (window.attrComboBox_3.currentIndex() == 0):
			self.atk_bns[2] = (self.cal_attr_bns(window.strSpinBox.value()))
			
		elif (window.attrComboBox_3.currentIndex() == 1):
			self.atk_bns[2] = (self.cal_attr_bns(window.dexSpinBox.value()))

		elif (window.attrComboBox_3.currentIndex() == 2):
			self.atk_bns[2] = (self.cal_attr_bns(window.conSpinBox.value()))

		elif (window.attrComboBox_3.currentIndex() == 3):
			self.atk_bns[2] = (self.cal_attr_bns(window.intSpinBox.value()))

		elif (window.attrComboBox_3.currentIndex() == 4):
			self.atk_bns[2] = (self.cal_attr_bns(window.wisSpinBox.value()))

		elif (window.attrComboBox_3.currentIndex() == 5):
			self.atk_bns[2] = (self.cal_attr_bns(window.chaSpinBox.value()))

	def set_atk_bns4(self, window):
		if (window.attrComboBox_4.currentIndex() == 0):
			self.atk_bns[3] = (self.cal_attr_bns(window.strSpinBox.value()))
			
		elif (window.attrComboBox_4.currentIndex() == 1):
			self.atk_bns[3] = (self.cal_attr_bns(window.dexSpinBox.value()))

		elif (window.attrComboBox_4.currentIndex() == 2):
			self.atk_bns[3] = (self.cal_attr_bns(window.chaSpinBox.value()))

		elif (window.attrComboBox_4.currentIndex() == 3):
			self.atk_bns[3] = (self.cal_attr_bns(window.intSpinBox.value()))

		elif (window.attrComboBox_4.currentIndex() == 4):
			self.atk_bns[3] = (self.cal_attr_bns(window.wisSpinBox.value()))

		elif (window.attrComboBox_4.currentIndex() == 5):
			self.atk_bns[3] = (self.cal_attr_bns(window.chaSpinBox.value()))
	
	def firstAttack_SpinBoxChange(self, value):
		return