from dummyCreature import *

class Zombie (creature):
	def __init__(self):
		self.name = "Zombie"
		self.armor_cls = 8
		self.hit_pts = 22
		self.curr_hp = self.hit_pts
		self.challnge_rtg = 1/4
		self.prof_bns = 2
		self.is_defeated = False
		self.initative = 0

		self.strength = 13
		self.dexterity = 6
		self.constitution = 16
		self.intelligence = 3
		self.wisdom = 6
		self.charisma = 5

		self.dex_bns = -2
		self.atk_bns = 3
		self.dmg_per_rnd = 4

	def roll_init(self):
		return super().roll_init()

	def takes_dmg(self, dmg):
		super().takes_dmg(dmg)

	def attack(self, enemy):
		totalDmg = 0

		totalDmg = self.slam()

		super().attack(enemy, totalDmg)

	def slam(self):
		dmgRoll = 0

		dmgRoll = dmgRoll + random.randint(1,6)

		dmgRoll = dmgRoll + 1

		return dmgRoll