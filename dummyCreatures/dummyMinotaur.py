from dummyCreature import *

class minotaur (creature):
	def __init__(self):
		minotaur.__init__

		self.armor_cls = 14
		self.hit_pts = 76
		self.curr_hp = self.hit_pts
		self.challnge_rtg = 3
		self.prof_bns = 2
		self.is_defeated = False

		self.strength = 18
		self.dexterity = 11
		self.constitution = 16
		self.intelligence = 6
		self.wisdom = 16
		self.charisma = 19

		self.dex_bns = 0
		self.atk_bns = 6
		self.dmg_per_rnd = 22