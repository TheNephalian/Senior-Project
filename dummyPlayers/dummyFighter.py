import random

from player import *
from testModScreen import *


class Fighter (Player):
	def __init__(self):
		self.name = "Fighter"
		self.lvl = 1
		self.hp = 10
		self.curr_hp = self.hp
		self.ac = 14
		self.prof_bns = 2
		self.is_defeated = False
		self.initiative = 0
		self.hasattacked = False
        
		self.strength = 16
		self.dexterity = 14
		self.constitution = 14
		self.intelligence = 10
		self.wisdom = 8
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
	
	def has_attacked(self):
		return super().has_attacked()

	def has_not_attacked(self):
		return super().has_not_attacked()