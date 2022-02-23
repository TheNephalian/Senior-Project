from dummyCreature import *

class terrasque (creature):
	def __init__(self):
		terrasque.__init__

		self.armor_cls = 25
		self.hit_pts = 676
		self.curr_hp = self.hit_pts
		self.challnge_rtg = 30
		self.prof_bns = 9
		self.is_defeated = False

		self.strength = 30
		self.dexterity = 11
		self.constitution = 30
		self.intelligence = 3
		self.wisdom = 11
		self.charisma = 11

		self.dex_bns = 0
		self.atk_bns = 19
		self.dmg_per_rnd = 148