from dummyCreature import *

class behir (creature):
	def __init__(self):
		behir.__init__

		self.armor_cls = 17
		self.hit_pts = 168
		self.curr_hp = self.hit_pts
		self.challnge_rtg = 11
		self.prof_bns = 4
		self.is_defeated = False

		self.strength = 23
		self.dexterity = 16
		self.constitution = 18
		self.intelligence = 7
		self.wisdom = 14
		self.charisma = 11

		self.dex_bns = 3
		self.atk_bns = 10
		#self.dmg_per_rnd = 56
		self.lbRecharge = True

		def attack():
			lightningBreath()
		
			multiAttack()
			return

		def multiAttack():
			bite()

			claw()
			return

		def bite():
			self.attack_roll()

			dmgRoll = random.randint(1,10) + random.randint(1,10) + 10

			return dmgRoll

		def claw():
			self.attack_roll()

			dmgRoll = random.randint(1,6) + random.randint(1,6) + 10
			return dmgRoll

		def lightningBreath():
			if (self.fbRecharge == False):
				rechargeRoll = random.randint(1,6)
				if (rechargeRoll == 5 | rechargeRoll == 6):
					self.fbRecharge = True

			dmgRoll = 0

			if (self.fbRecharge == True):
				for i in range(26):
					dmgRoll = dmgRoll + random.randint(1,6)

				self.fbRecharge = False

			return dmgRoll