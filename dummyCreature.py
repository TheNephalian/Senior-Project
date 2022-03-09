import random

class creature():
	def __init__(self):
		self.name = "Dummy Creature"
		self.challnge_rtg = 0
        #We'll need to keep track of two hp values in order to perform combat.
        #   one represents the creature/player's hp before combat/at the beginning of the round
		self.hit_pts = 0
        #   the other represents the creature/players hp after the end of the round
		self.curr_hp = self.hit_pts
		self.armor_cls = 0
		self.prof_bns = 0
		self.is_defeated = False
		self.initative = 0
		
		#The following attribute scores are all default values
   		#   These will vary based on the creature/player class
		self.strength = 10
		self.dexterity = 10
		self.constitution = 10
		self.intelligence = 10
		self.wisdom = 10
		self.charisma = 10

		self.dex_bns = 0
		self.atk_bns = 0
		self.dmg_per_rnd = 0

	def roll_init(self):
		init = random.randint(1,20) + self.dex_bns
		return init

	def attack(self):
		#find player

		atk_roll = self.attack_roll()

	def attack_roll(self):
		atk_roll = random.randint(1,20) + self.atk_bns #+ attr_bns. This will vary depending on the creature/player class
		return atk_roll

	def take_dmg(self, dmg):
		self.curr_hp = self.hit_pts - dmg
		self.hit_pts = self.curr_hp

		if (self.hit_pts <= 0):
			self.is_defeated = True
			
		return