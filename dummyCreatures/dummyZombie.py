from dummyCreature import *

class zombie (creature):
	def __init__(self):
		zombie.__init__

		self.armor_cls = 8
		self.hit_pts = 22
		self.curr_hp = self.hit_pts
		self.challnge_rtg = 1/4
		self.prof_bns = 2
		self.is_defeated = False

		self.strength = 13
		self.dexterity = 6
		self.constitution = 16
		self.intelligence = 3
		self.wisdom = 6
		self.charisma = 5

		self.dex_bns = -2
		self.atk_bns = 3
		self.dmg_per_rnd = 4