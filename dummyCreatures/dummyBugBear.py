from dummyCreature import *

class bugBear (creature):
	def __init__(self):
		bugBear.__init__

		self.armor_cls = 16
		self.hit_pts = 27
		self.curr_hp = self.hit_pts
		self.challnge_rtg = 1
		self.prof_bns = 2
		self.is_defeated = False

		self.strength = 15
		self.dexterity = 14
		self.constitution = 13
		self.intelligence = 8
		self.wisdom = 11
		self.charisma = 9

		self.dex_bns = 2
		self.atk_bns = 4
		self.dmg_per_rnd = 13