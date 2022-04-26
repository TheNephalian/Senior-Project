import math

from mainScreen_WIP import *

class dpr_calculation():
	def __init__(self, ui):
		self.dpr_calculator(ui)


	def dpr_calculator(self, ui):
		dpr = 0

		atk_bns1 = self.set_atk_bns1(ui)
		atk_bns2 = 0
		atk_bns3 = 0
		atk_bns4 = 0

		num_dmg_dice1 = 0
		num_dmg_dice2 = 0
		num_dmg_dice3 = 0
		num_dmg_dice4 = 0

		die_type1 = 0
		die_type2 = 0
		die_type3 = 0
		die_type4 = 0

		atk_attr1 = ""
		atk_attr2 = ""
		atk_attr3 = ""
		atk_attr4 = ""

	def cal_attr_bns(self, value):
		atr_bns = math.floor((value - 10) / 2)

		return atr_bns

	def set_atk_bns1(self, window):
		if (window.attrComboBox_1.currentIndex() == 0):
			self.atk_bns1 = self.cal_attr_bns(window.strSpinBox.value())
			
			print("STR", self.atk_bns1)
			
		elif (window.attrComboBox_1.currentIndex() == 1):
			self.atk_bns1 = self.cal_attr_bns(window.dexSpinBox.value())
			
			print("DEX", self.atk_bns1)

		elif (window.attrComboBox_1.currentIndex() == 2):
			self.atk_bns1 = self.cal_attr_bns(window.conSpinBox.value())

			print("CON", self.atk_bns1)

		elif (window.attrComboBox_1.currentIndex() == 3):
			self.atk_bns1 = self.cal_attr_bns(window.intSpinBox.value())

			print("INT", self.atk_bns1)

		elif (window.attrComboBox_1.currentIndex() == 4):
			self.atk_bns1 = self.cal_attr_bns(window.wisSpinBox.value())

			print("WIS", self.atk_bns1)

		elif (window.attrComboBox_1.currentIndex() == 5):
			self.atk_bns1 = self.cal_attr_bns(window.chaSpinBox.value())

			print("CHA", self.atk_bns1)
	
	def firstAttack_SpinBoxChange(self, value):
		return