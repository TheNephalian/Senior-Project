import random

from player import *

class Fighter (Player):
	def __init__(self):
		self.name = "Artificer"
		self.lvl = 1
		self.hp = 10
		self.curr_hp = self.hp
		self.ac = 14
		self.prof_bns = 2
		self.is_defeated = False
		self.initative = 0
        
		self.strength = 10
		self.dexterity = 14
		self.constitution = 14
		self.intelligence = 18
		self.wisdom = 13
		self.charisma = 12
        
		self.dex_bns = 2
		self.atk_bns = 5
		self.dmg_per_rnd = 5

	def lvl_change(self, lvls):
		return super().lvl_change(lvls)

	def roll_init(self):
		return super().roll_init()

	def takes_dmg(self, dmg):
		super().takes_dmg(dmg)

	def attack(self, enemy):
		super().attack(enemy)