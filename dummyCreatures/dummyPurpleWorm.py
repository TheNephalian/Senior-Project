from dummyCreature import *

class purpleWorm (creature):
	def __init__(self):
		purpleWorm.__init__

		self.armor_cls = 18
		self.hit_pts = 247
		self.curr_hp = self.hit_pts
		self.challnge_rtg = 15
		self.prof_bns = 5
		self.is_defeated = False

		self.strength = 28
		self.dexterity = 7
		self.constitution = 22
		self.intelligence = 1
		self.wisdom = 8
		self.charisma = 4

		self.dex_bns = -2
		self.atk_bns = 14
		self.dmg_per_rnd = 104