from dummyCreature import *

class BugBear (creature):
	def __init__(self):
		self.name = "Bugbear"
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
		
		self.surprise_Attack = True

	def roll_init(self):
		return super().roll_init()

	def takes_dmg(self, dmg):
		super().takes_dmg(dmg)

	def attack(self, enemy):
		totalDmg = 0

		totalDmg = self.morningstar()

		super().attack(enemy, totalDmg)

	def morningstar(self):
		dmgRoll = 0

		#if hits, rolls 2d8 + 2
		for i in range(2):
			dmgRoll = dmgRoll + random.randint(1,8)
			
			dmgRoll = dmgRoll + 2

		#checks if surprise attack (beginning of combat)
		if (self.surprise_Attack == True):
			for i in range(2):
				dmgRoll = dmgRoll + random.randint(1,6)

			self.surprise_Attack = False

		return dmgRoll
