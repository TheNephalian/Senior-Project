from dummyCreature import *

class giantRat (creature):
	def __init__(self):
		giantRat.__init__

		self.armor_cls = 12
		self.hit_pts = 7
		self.curr_hp = self.hit_pts
		self.challnge_rtg = 1/8
		self.prof_bns = 2
		self.is_defeated = False

		self.strength = 7
		self.dexterity = 15
		self.constitution = 11
		self.intelligence = 2
		self.wisdom = 10
		self.charisma = 4

		self.dex_bns = 2
		self.atk_bns = 4
		self.dmg_per_rnd = 4